return {
  {
    "neovim/nvim-lspconfig",
    opts = function(_, opts)
      opts.servers = opts.servers or {}
      opts.ensure_installed = opts.ensure_installed or {}

      table.insert(opts.ensure_installed, "basedpyright")
      table.insert(opts.ensure_installed, "ruff")
      table.insert(opts.ensure_installed, "lua_ls")
      table.insert(opts.ensure_installed, "taplo")

      opts.servers.pyright = nil

      vim.o.updatetime = 300

      -----------------------------------------------------------------------
      -- PYTHON
      -----------------------------------------------------------------------
      opts.servers.basedpyright = {
        settings = {
          basedpyright = {
            analysis = {
              typeCheckingMode = "basic",
              autoSearchPaths = true,
              useLibraryCodeForTypes = true,
              diagnosticMode = "openFilesOnly",
            },
          },
        },
      }

      opts.servers.ruff = {
        on_attach = function(client)
          client.server_capabilities.hoverProvider = false
        end,
      }

      -----------------------------------------------------------------------
      -- LUA
      -----------------------------------------------------------------------
      opts.servers.lua_ls = {
        settings = {
          Lua = {
            diagnostics = {
              globals = { "vim" },
            },
          },
        },
      }

      -----------------------------------------------------------------------
      -- TOML
      -----------------------------------------------------------------------
      opts.servers.taplo = {}
    end,
  },
}

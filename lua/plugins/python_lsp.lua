return {
  {
    "neovim/nvim-lspconfig",
    opts = function(_, opts)
      opts.servers = opts.servers or {}

      ----------------------------------------------------------------------
      -- Disable Pyright completely
      ----------------------------------------------------------------------
      opts.servers.pyright = nil

      ----------------------------------------------------------------------
      -- Modern Hover UI (no deprecated APIs)
      -- Hover only appears when you press K
      ----------------------------------------------------------------------

      -- Manual trimming (because trimempty + trim_empty_lines are deprecated)
      local function trim_empty(lines)
        local out = {}
        for _, line in ipairs(lines) do
          if line ~= "" then
            table.insert(out, line)
          end
        end
        return out
      end

      vim.lsp.handlers["textDocument/hover"] = function(err, result, _, _)
        if err then
          vim.notify("Hover error: " .. tostring(err), vim.log.levels.ERROR)
          return
        end

        if not (result and result.contents) then
          return
        end

        local raw = vim.lsp.util.convert_input_to_markdown_lines(result.contents)
        local markdown_lines = trim_empty(raw)

        return vim.lsp.util.open_floating_preview(markdown_lines, "markdown", {
          border = "rounded",
          max_width = 80,
          max_height = 20,
          focusable = true,
          title = " Hover ",
        })
      end

      -- No CursorHold hover spam
      vim.o.updatetime = 300

      ----------------------------------------------------------------------
      -- BasedPyright (main Python LSP)
      ----------------------------------------------------------------------
      opts.servers.basedpyright = {
        settings = {
          basedpyright = {
            analysis = {
              typeCheckingMode = "basic", -- clean, minimal noise
              autoSearchPaths = true,
              useLibraryCodeForTypes = true,
              diagnosticMode = "openFilesOnly", -- fast + responsive
            },
          },
        },
      }

      ----------------------------------------------------------------------
      -- Ruff (linting + formatting)
      -- Disable hover so BasedPyright handles documentation
      ----------------------------------------------------------------------
      opts.servers.ruff = {
        on_attach = function(client)
          client.server_capabilities.hoverProvider = false
        end,
      }
    end,
  },
}

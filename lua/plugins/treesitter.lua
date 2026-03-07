return {
  "nvim-treesitter/nvim-treesitter",
  version = false, -- last release is way too old and doesn't work on Windows
  build = ":TSUpdate",
  lazy = false, -- load immediately
  dependencies = {
    {
      "nvim-treesitter/nvim-treesitter-textobjects",
      init = function()
        -- PERF: no need to load the plugin, if we only need its queries for mini.ai
        local plugin = require("lazy.core.config").spec.plugins["nvim-treesitter"]
        local opts = require("lazy.core.plugin").values(plugin, "opts", false)
        local enabled = false
        if opts.textobjects then
          for _, mod in ipairs({ "move", "select", "swap", "lsp_interop" }) do
            if opts.textobjects[mod] and opts.textobjects[mod].enable then
              enabled = true
              break
            end
          end
        end
        if not enabled then
          require("lazy.core.loader").disable_rtp_plugin("nvim-treesitter-textobjects")
        end
      end,
    },
  },
  keys = {
    { "<c-space>", desc = "Increment selection" },
    { "<bs>", desc = "Decrement selection", mode = "x" },
  },
  ---@type TSConfig
  opts = {
    highlight = {
      enable = true,
      additional_vim_regex_highlighting = false,
    },
    indent = { enable = true },
    context_commentstring = { enable = true, enable_autocmd = false },
    ensure_installed = {
      "bash",
      "c",
      "html",
      "javascript",
      "json",
      "lua",
      "luadoc",
      "luap",
      "markdown",
      "markdown_inline",
      "python",
      "query",
      "regex",
      "tsx",
      "typescript",
      "vim",
      "vimdoc",
      "yaml",
    },
    incremental_selection = {
      enable = true,
      keymaps = {
        init_selection = "<C-space>",
        node_incremental = "<C-space>",
        scope_incremental = false,
        node_decremental = "<bs>",
      },
    },
    auto_install = true,
  },
  ---@param opts TSConfig
  config = function(_, opts)
    if type(opts.ensure_installed) == "table" then
      local added = {}
      opts.ensure_installed = vim.tbl_filter(function(lang)
        if added[lang] then
          return false
        end
        added[lang] = true
        return true
      end, opts.ensure_installed)
    end

    local ok, ts = pcall(require, "nvim-treesitter.configs")
    if ok then
      ts.setup(opts)

      -- Attach highlight to all currently open buffers
      for _, buf in ipairs(vim.api.nvim_list_bufs()) do
        local ft = vim.api.nvim_buf_get_option(buf, "filetype")
        if ft ~= "" then
          pcall(require("nvim-treesitter.highlighter").attach, buf, ft)
        end
      end

      -- Auto-attach highlight to any future buffer
      vim.api.nvim_create_autocmd({ "BufReadPost", "BufNewFile" }, {
        callback = function()
          local buf = vim.api.nvim_get_current_buf()
          local ft = vim.api.nvim_buf_get_option(buf, "filetype")
          if ft ~= "" then
            pcall(require("nvim-treesitter.highlighter").attach, buf, ft)
          end
        end,
      })
    end
  end,
}

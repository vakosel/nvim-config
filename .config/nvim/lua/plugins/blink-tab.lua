return {
  "saghen/blink.cmp",
  dependencies = {
    {
      "Exafunction/codeium.nvim",
    },
  },
  opts = {
    sources = {
      default = { "codeium", "copilot", "lsp", "path", "snippets", "buffer" },
      providers = {
        codeium = {
          name = "Codeium",
          module = "codeium.blink",
          score_offset = 200,
          async = true,
          enabled = true, -- start disabled since Copilot is active
        },
      },
    },
    signature = { enabled = true },
    keymap = {
      ["<Tab>"] = {
        "select_next",
        "snippet_forward",
        "fallback",
      },
      ["<S-Tab>"] = {
        "select_prev",
        "snippet_backward",
        "fallback",
      },
      ["<CR>"] = {
        "accept",
        "fallback",
      },
      ["<C-space>"] = { "show", "show_documentation", "hide_documentation" },
      ["<C-e>"] = { "hide" },
      ["<C-u>"] = { "scroll_documentation_up", "fallback" },
      ["<C-d>"] = { "scroll_documentation_down", "fallback" },
      preset = "super-tab",
    },
  },
}

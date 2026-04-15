return {
  "saghen/blink.cmp",
  opts = {
    sources = {
      default = { "copilot", "lsp", "path", "snippets", "buffer" },
    },

    signature = { enabled = true },

    keymap = {
      preset = "super-tab",

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
    },
  },
}

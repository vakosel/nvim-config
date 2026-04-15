return {
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
  },
  opts = {
    strategies = {
      chat = {
        adapter = "ollama",
        roles = {
          llm = "CodeCompanion",
          user = "Me",
        },
      },
      inline = { adapter = "ollama" },
    },
    adapters = {
      ollama = function()
        return require("codecompanion.adapters").extend("ollama", {
          env = {
            url = "http://127.0.0.1:11434",
          },
          schema = {
            model = {
              default = "qwen2.5-coder:1.5b",
            },
            num_ctx = {
              default = 2048, -- Keep it low so the Pi CPU doesn't choke
            },
            num_thread = {
              default = 4, -- Utilize all 4 Pi cores
            },
          },
        })
      end,
    },
  },
}

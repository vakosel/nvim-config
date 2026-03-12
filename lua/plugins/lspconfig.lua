return {

  {
    "neovim/nvim-lspconfig",
    ---@class PluginLspOpts
    opts = {
      servers = {
        -- pyright will be automatically installed with mason and loaded with lspconfig
        pyright = {
          settings = {
            pyright = {
              -- Using Ruff's import organizer
              disableOrganizeImports = true,
            },
            python = {
              {
                settings = {
                  python = {
                    analysis = {
                      typeCheckingMode = "basic", -- τέλειο για PySide6, ήσυχο για PicoW
                      autoSearchPaths = true, -- βρίσκει modules στο uv environment
                      useLibraryCodeForTypes = true, -- καλύτερο autocompletion για PySide6
                      diagnosticMode = "workspace", -- αναλύει μόνο το project, όχι όλο το σύστημα

                      -- 🔽 Αυτά είναι κρίσιμα για να μην σε ενοχλεί στο Pico/MicroPython
                      reportMissingImports = "none", -- δεν γκρινιάζει για machine, rp2, network
                      reportMissingModuleSource = "none", -- δεν ζητάει source για micropython modules
                      reportMissingTypeStubs = "none", -- δεν ζητάει stubs για modules χωρίς hints
                    },
                  },
                },
              },
            },
          },
        },
      },
    },
  },
}

require("bunny"):setup({
	hops = {
		{ key = "/", path = "/" },
		{ key = "w", path = "~/workspace", desc = "workspace" },
		{ key = "d", path = "~/dotfiles", desc = "dotfiles" },
		{ key = "D", path = "~/Documents", desc = "Documents" },
		{ key = "c", path = "~/.config", desc = "Config files" },
		{ key = "n", path = "~/.config/nvim", desc = "nvim" },
		{ key = "f", path = "~/.config/fish", desc = "fish" },
		{ key = "y", path = "~/.config/yazi", desc = "yazi" },
		{ key = "q", path = "~/.config/qtile", desc = "qtile" },
		{ key = { "l", "s" }, path = "~/.local/share", desc = "Local share" },
		{ key = { "l", "b" }, path = "~/.local/bin", desc = "Local bin" },
		{ key = { "l", "t" }, path = "~/.local/state", desc = "Local state" },
		-- key and path attributes are required, desc is optional
	},
	desc_strategy = "path", -- If desc isn't present, use "path" or "filename", default is "path"
	ephemeral = true, -- Enable ephemeral hops, default is true
	tabs = true, -- Enable tab hops, default is true
	notify = false, -- Notify after hopping, default is false
	fuzzy_cmd = "fzf", -- Fuzzy searching command, default is "fzf"
})

require("git"):setup({})
require("smart-enter"):setup({})
require("full-border"):setup({})

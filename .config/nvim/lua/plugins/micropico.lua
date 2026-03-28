return {
  "jim-at-jibba/micropython.nvim",
  config = function()
    require("micropython_nvim").setup({
      device = "/dev/ttyACM0",
      baudrate = 115200,
    })
  end,
}

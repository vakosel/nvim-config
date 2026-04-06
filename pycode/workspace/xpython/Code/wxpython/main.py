import wx
from CalcFrame import CalculatorFrame

app = wx.App(False)
frame = CalculatorFrame(None)

frame.Show()


app.MainLoop()





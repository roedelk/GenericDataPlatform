import wx
import wx.html2

class PyBrowser(wx.Frame):

  def __init__(self, *args, **kwds):
    wx.Frame.__init__(self, *args, **kwds)
    self.SetTitle('PyBrowser')
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
    #Element Variables
    self.browser = wx.html2.WebView.New(self)
    #Adding elements
    sizer.Add(addressarea, proportion = 0, flag = wx.EXPAND, border = 0)
    sizer.Add(self.browser, 1, wx.EXPAND, 10)
    #Menu bar stuff
    #File Menu
    self.fileMenu = wx.Menu()
    self.New = self.fileMenu.Append(wx.ID_ANY, 'New Window')
    #...
    #Help Menu
    self.helpMenu = wx.Menu()
    self.Help = self.helpMenu.Append(wx.ID_ANY, 'Help')
    #...
    self.Bind(wx.EVT_MENU,self.OnHelp,self.Help)
    #...
    #Adding the actual Menu Bar

    self.menuBar = wx.MenuBar()
    self.menuBar.Append(self.fileMenu, 'File')
    self.menuBar.Append(self.helpMenu, 'Help')
    self.SetMenuBar(self.menuBar)

    self.SetSizer(sizer)
    self.SetSize((1000, 700))

  def OnHelp(self, event):
    pass

  def OnCloseWindow(self, event):
    print("[wxpython.py] OnClose called")
    if not self.browser:
       return
    self.browser.ParentWindowWillClose()
    event.Skip()
    self.browser = None

if __name__ == '__main__':
    app = wx.App()
    dialog = PyBrowser(None, -1)
    print(dialog.browser.SetPage(open('gui2.html','r').read(),"")) #LoadURL("gui2.html")
    dialog.Show()
    app.MainLoop()
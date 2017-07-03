# https://wxpython.org/Phoenix/docs/html/wx.Menu.html
# GUI: cef & wxPython, später erweiterbar mit cherryPy(Webserver)
#(Connection, Object, Attribute, Process, ProcessGroup)

import os
import wx
import wx.html
import code.util.Settings as s

SETTINGS_PATH = "../../settings/GUI.yml"

class MainGUI(wx.Frame):

    menuDict = {}
    startURL = ""

    def __init__(self, *args, **kwds):
        _settings = s.Settings.read(SETTINGS_PATH)
        wx.Frame.__init__(self,
                          parent=None,
                          id=wx.ID_ANY,
                          title=_settings['TITLE'],
                          size=(_settings['APP_WIDTH'], _settings['APP_HEIGHT']))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Content
        self.browser = wx.html.HtmlWindow(self)  #wx.html2.WebView.New(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        # Icon
        self.setupIcon(_settings['ICON'])
        # Menu
        self.createMenu(_settings['MENUBAR'])

    def setupIcon(self, ICON):
        if os.path.exists(ICON) and hasattr(wx, "IconFromBitmap"):
            # TODO: logging
            icon = wx.IconFromBitmap(wx.Bitmap(ICON, wx.BITMAP_TYPE_PNG))
            self.SetIcon(icon)

    def createMenu(self, menubar_settings):
        menubar = wx.MenuBar()
        for mbar in menubar_settings:
            for menu in mbar.values():
                m = wx.Menu()
                for item in menu['ITEMS']:
                    self.Bind(wx.EVT_MENU, self.loadContent, m.Append(item['ID'], item['TEXT']))
                    self.menuDict[item['ID']] = item['HTML']
                    if 'START' in item.keys() and item['START'] == True:
                        self.startURL = item['HTML']
                menubar.Append(m, menu['TEXT'])
        self.SetMenuBar(menubar)

    def loadContent(self,event):
        menuItemId = event.GetId()
        print(menuItemId)
        print(self.menuDict[menuItemId])
        # TODO: if file exists else error
        self.browser.LoadFile('../../' + self.menuDict[menuItemId])


    def OnClose(self, event):
        print("[wxpython.py] OnClose called")
        if not self.browser:
            return
        event.Skip()
        self.browser = None

if __name__ == '__main__':
    app = wx.App()
    dialog = MainGUI(None, -1)
    # TODO: if file exists else error
    print(dialog.browser.LoadFile('../../' + dialog.startURL))
    dialog.Show()
    app.MainLoop()

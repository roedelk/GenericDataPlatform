# https://wxpython.org/Phoenix/docs/html/wx.Menu.html
# GUI: cef & wxPython, später erweiterbar mit cherryPy(Webserver)
#()

import os
import wx
import wx.html
import wx.grid
import code.util.Settings as s

SETTINGS_PATH = "../../settings/GUI.yml"

# Define the tab content as classes:
class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (20, 20))


class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20, 20))


class TabThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the third tab", (20, 20))


class TabFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the fourth tab", (20, 20))


class TabFive(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20, 20))


class GenericTable(wx.grid.GridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None):
        wx.grid.GridTableBase.__init__(self)
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]

    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass


data = (("A", "B"),
        ("C", "D"),
        ("E", "F"),
        ("G", "G"),
        ("F", "F"),
        ("Q", "Q"))

colLabels = ("Last", "First")
rowLabels = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        tableBase = GenericTable(data, rowLabels, colLabels)
        self.SetTable(tableBase)

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

        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)




        # Create the tab windows
        tab1 = TabOne(nb)
        tab2 = TabTwo(nb)
        tab3 = TabThree(nb)
        tab4 = TabFour(nb)
        tab5 = TabFive(nb)
        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Connections")
        nb.AddPage(tab2, "Objects")
        nb.AddPage(tab3, "Attributes")
        nb.AddPage(tab4, "Processes")
        nb.AddPage(tab5, "ProcessGroups")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer() #wx.VERTICAL)
        sizer.Add(nb, 1, wx.EXPAND)

        # Content
        #self.browser = wx.html.HtmlWindow(self)  #wx.html2.WebView.New(self)
       # sizer = wx.BoxSizer(wx.VERTICAL)
       # sizer.Add(self.browser, 1, wx.EXPAND, 10)
        p.SetSizer(sizer)
        # Icon
        self.setupIcon(_settings['ICON'])
        # Menu
        self.createMenu(_settings['MENUBAR'])

        #self.grid = SimpleGrid(self,p)

        self.grid = SimpleGrid(p, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

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
      #  self.browser.LoadFile('../../' + self.menuDict[menuItemId])


    def OnClose(self, event):
        print("[wxpython.py] OnClose called")
        #if not self.browser:
        #    return
        event.Skip()
        #self.browser = None

if __name__ == '__main__':
    app = wx.App()
    dialog = MainGUI(None, -1)
    # TODO: if file exists else error
    #print(dialog.browser.LoadFile('../../' + dialog.startURL))
    dialog.Show()
    app.MainLoop()

import wx,os,xlrd
from IPy import IP
class SiteLog(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='SiteLog', size=(640, 480))
        self.SelBtn = wx.Button(self, label='>>', pos=(305, 5), size=(80, 25))
        self.SelBtn.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        self.OkBtn = wx.Button(self, label='OK', pos=(405, 5), size=(80, 25))
        self.OkBtn.Bind(wx.EVT_BUTTON, self.ReadFile)
        self.SelBtn = wx.Button(self, label='>>', pos=(305, 5), size=(80, 25))
        self.SelBtn.Bind(wx.EVT_BUTTON, self.)
        self.FileName = wx.TextCtrl(self, pos=(5, 5), size=(230, 25))
        self.FileContent = wx.TextCtrl(self, pos=(5, 35), size=(620, 480), style=(wx.TE_MULTILINE))

    def OnOpenFile(self, event):
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.FileName.SetValue(dialog.GetPath())
            dialog.Destroy

    def ReadFile(self, event):
        file = xlrd.open_workbook(self.FileName.GetValue())
        class VlanConfig:
            vlan = ""
            floor = ""
            ipaddr = ""
            netmask = ""
            network_number = ""
            virtual_gateway = ""
            master_gateway = ""
            backup_gateway = ""
        sheet = file.sheet_by_name('IP-Planing')
        nrows = sheet.nrows
        dict = {}
        for n in range(1, nrows):
            t = VlanConfig()
            t.vlan = str(int((sheet.row(n)[1].value)))
            if sheet.row(n)[3].value == '':
                t.floor = 'emtpy'
            else:
                t.floor = str(int((sheet.row(n)[3].value)))
            t.ipaddr = IP(sheet.row(n)[0].value)
            t.netmask = str(t.ipaddr.netmask())
            t.network_number = IP(t.ipaddr.strNormal(0)).int()
            t.virtual_gateway = IP(t.network_number + 1).strNormal(0)
            t.master_gateway = IP(t.network_number + 2).strNormal(0)
            t.backup_gateway = IP(t.network_number + 3).strNormal(0)
            if t.floor in dict:
                dict[t.floor].append(t);''
            else:
                dict[t.floor] = []
                dict[t.floor].append(t)
if __name__ == '__main__':
    app = wx.App()
    SiteFrame = SiteLog()
    SiteFrame.Show()
    app.MainLoop()


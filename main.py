import wx
import menu
import parameter

class MainFrame( menu.MainMenu ):
    def __init__( self, menu_parameter ):
        menu.MainMenu.__init__( self, menu_parameter )

class MainApp( wx.App ):
    def __init__( self ):
        wx.App.__init__( self )

    def OnInit(self):
        self.main_frame = MainFrame( parameter.designer_parm )
        self.SetTopWindow( self.main_frame )

        self.main_frame.Show()
        return True

    def OnExit(self):
        return True

if __name__ == '__main__':
    main_app = MainApp()
    main_app.MainLoop()

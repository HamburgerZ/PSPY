import wx
import cv2
import os
import parameter
import dlg
import interpreter

class MainMenu( wx.Frame ):
    def __init__( self, designer_parm ):
        wx.Frame.__init__( self, parent = None, id = -1, title = 'PSPY', size=( 600, 58 ) )

        self.image_ico = wx.Icon( 'ico.ico', wx.BITMAP_TYPE_ICO )
        self.SetIcon( self.image_ico )

        self.frame_menu = wx.MenuBar()
        self.file_menu = wx.Menu()
        self.frame_menu.Append( self.file_menu, 'file' )
        self.imgpro_menu = wx.Menu()
        self.frame_menu.Append( self.imgpro_menu, 'imgpro' )
        self.fork_menu = wx.Menu()
        self.frame_menu.Append( self.fork_menu, 'fork' )

        self.mmenu_parm = designer_parm
        self.temp_option = []
        self.dlg_name = []
        self.drawimg_dlg = None
        self.ctrl_handler = None
        self.ctrls_handlers = {}
        self.menu_draw()

    def menu_draw( self ):
        for i in self.mmenu_parm.menus_parms: # i is a tuple
            if( i[0] == 'file' ):
                if( i[1] == 'open image' ):
                    self.temp_option.append( self.file_menu.Append( -1, i[1] ) )
                    self.Bind( wx.EVT_MENU, self.openimg_handler, self.temp_option[-1] )
                elif( i[1] == 'save image' ):
                    self.temp_option.append( self.file_menu.Append( -1, i[1] ) )
                    self.Bind( wx.EVT_MENU, self.saveimg_handler, self.temp_option[-1] )
            elif( i[0] == 'imgprocess' ):
                self.temp_option.append( self.imgpro_menu.Append( -1, i[1] ) )
                self.dlg_name = i[1]
                self.ctrl_handler = lambda event, dlg_name = i[1]: \
                self.adjustpram_handler( event, dlg_name )
                self.ctrls_handlers[ self.dlg_name ] = self.ctrl_handler
                self.Bind( wx.EVT_MENU, self.ctrls_handlers[ self.dlg_name ], \
                           self.temp_option[-1] )
        self.SetMenuBar( self.frame_menu )

    def adjustpram_handler( self, event, dlg_name ): #draw the image in the list output_image according the name
        parameter.adjustparm_dlg[ dlg_name ]  \
                = dlg.AdjparmDlg( dlg_name, self )

    def openimg_handler( self, event ):
        self.FILE_TYPE1 = "image source (*.bmp; *.jpg; *.png)|*.bmp;*.jpg;*.png"
        self.FILE_TYPE2 = "image source (*.bmp; *.jpg; *.png)|*.bmp;*.jpg;*.png"
        self.image_dict = {}
        #create the dialog
        openimg_dlg = wx.FileDialog( self, message="Choose a file", defaultFile="",
            wildcard=self.FILE_TYPE1, style=wx.FD_OPEN )
        #message handle
        if ( openimg_dlg.ShowModal() == wx.ID_OK ):
            #collect_parameter
            self.img_name = 'original_img'
            self.temp_path = ""
            self.image_path = openimg_dlg.GetPaths()
            for i in self.image_path:
                self.temp_path = self.temp_path + i
            self.dlg_userparm = [ 'openimg', self.image_path, self.img_name ]
            parameter.user_parm.funcs_parms.append( self.dlg_userparm )
            parameter.user_parm.imgs_names.append( self.dlg_userparm[-1] )
            #interprete
            interpreter.parm_inper( parameter.user_parm )
            #draw_image
            self.img_draw( parameter.user_parm.imgs[ \
            parameter.user_parm.imgs_names[-1] ], parameter.user_parm.imgs_names[ -1 ] )
        #destroy the dialog
        openimg_dlg.Destroy()

    def saveimg_handler( self, event ):
        if( len( parameter.user_parm.imgs_names ) == 1 ):
            cv2.imwrite( parameter.user_parm.imgs_names[ -1 ] + '.bmp',\
        cv2.cvtColor( parameter.user_parm.imgs[ parameter.user_parm.imgs_names[ -1 ] ],\
         cv2.COLOR_BGR2RGB ) )

    def img_draw( self, draw_img, img_name ):
        self.img_heigth, self.img_width = draw_img.shape[ :2 ]

        if(  len( draw_img.shape )  == 3  ):
            self.temp_bitmap = wx.Bitmap.FromBuffer( self.img_width, self.img_heigth, \
            draw_img  )
        elif( len( draw_img.shape )  == 2  ):
            cv2.imwrite( 'temp.bmp', draw_img )
            self.temp_image = cv2.imread( 'temp.bmp' )
            self.temp_bitmap = wx.Bitmap.FromBuffer( self.img_width, self.img_heigth, \
         self.temp_image )
            os.remove( os.path.split(os.path.realpath(__file__))[0] + '\\temp.bmp' )
        if( self.drawimg_dlg == None ):
            self.drawimg_dlg = wx.Dialog( self, title = 'image', \
                        size = ( self.img_width + 6, self.img_heigth + 29 ) )
        dc = wx.BufferedDC( wx.ClientDC( self.drawimg_dlg ), self.temp_bitmap )
        dc.DrawBitmap( self.temp_bitmap, 0, 0 )
        #show the dialog used for showing
        self.drawimg_dlg.Show()
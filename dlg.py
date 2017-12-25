import wx
import cv2
import parameter
import interpreter

class AdjparmDlg( wx.Dialog ):
    def __init__( self, extend_parm, parent ):
        #parent is the MainMenu
        self.parent = parent
        self.dlg_name = extend_parm
        wx.Dialog.__init__( self, None, -1,  \
                  title = self.dlg_name, size = ( 190 + 40,
        len( parameter.designer_parm.dlgs_parms[self.dlg_name] ) * 65 + 12 + 35 ) )
        self.dlg_userparm = []                    #list of userparm from dlg with controls
        self.drawimg_dlg = None                   #the dlg with image
        self.preview_timer = wx.Timer( self )     #the timer
        self.parm_inper = interpreter.parm_inper  #interprete the parameter
        self.img_draw = self.parent.img_draw      #draw the dlg with image
        self.control_draw()                       #draw the dlg with controls
        self.collect_parm()                       #collect the parm from dlg with controls

    def control_draw( self ):
        self.label_set = []
        self.control_set = []
        j = 0
        for i in parameter.designer_parm.dlgs_parms[ self.dlg_name ]:
            if( i[0] == 'ChoiceCtrl' ):
                if( len(i) == 2 ):
                    self.label_set.append( wx.StaticText( self, -1, i[1], ( 10, j*65 + 12 ) ) )
                    self.control_set.append( wx.Choice( self, -1, ( 60,  \
            j*65 + 10 ), size = ( 140, 25 ),  choices = parameter.user_parm.imgs_names ) )
                else:
                    self.label_set.append( wx.StaticText( self, -1, i[1], (10, j*65 + 12 ) ) )
                    self.control_set.append( wx.Choice( self, -1, ( 60, j*65 + 10 ), \
                    size = ( 140, 25 ),  choices = i[2] ) )

            if( i[0] == 'TextCtrl' ):
                self.label_set.append( wx.StaticText( self, -1, i[1], ( 10, j*65 + 12 ) ) )
                self.control_set.append( wx.TextCtrl( self, -1, pos = ( 60,
            j*65 + 10 ), size=( 140, 25 ), style = wx.TE_PROCESS_ENTER ) )
                #self.bsdlgs_parameters.controls_parameter.append( \
                #self.control_set[-1].GetValue() )

            if( i[0] == 'Slider' ):
                self.label_set.append( wx.StaticText( self, -1, i[1], ( 10, j*65 + 12 ) ) )
                self.control_set.append( wx.Slider( self, -1, 1, i[2], i[3], pos=( 60, \
            j*65 + 10 ), size=( 140, 40 ), style = wx.SL_AUTOTICKS|wx.SL_LABELS ) )#control about slider
                self.control_set[ -1 ].SetTickFreq( i[4] ) #scale about slider

            if( i[0] == 'Preview' ):
                self.control_set.append( wx.CheckBox( self, label = 'Preview',pos = ( 80, j*65 ) ) )
                self.Bind( wx.EVT_CHECKBOX,self.checkbox_handler )
                self.Bind( wx.EVT_TIMER, self.preview_handler )

            if( i[0] == 'OkCancel' ):
                self.control_set.append( wx.Button( self, wx.ID_OK, 'OK', pos=( 10, \
            j*65  ), size=( 80, 25 ) ) )
                self.control_set.append( wx.Button( self, wx.ID_CANCEL, 'Cancel', pos = ( 120, \
            j*65  ), size=( 80, 25 ) ) )
            j = j + 1

    def collect_parm( self ):
        self.dlg_userparm.append( self.dlg_name )
        #when the Okbutton is pressed
        if( self.ShowModal() == wx.ID_OK ):
            j = 0
            for i in parameter.designer_parm.dlgs_parms[ self.dlg_name ]:
                if( i[0] == 'ChoiceCtrl' ):
                    if( len(i) == 2 ):
                        self.dlg_userparm.append( \
                          self.control_set[ j ].GetSelection() )
                    else:
                        self.dlg_userparm.append( \
                         i[2][ self.control_set[ j ].GetSelection() ]  )
                elif( i[0] == 'TextCtrl' or i[0] == 'Slider' ):
                    self.dlg_userparm.append( \
                     self.control_set[ j ].GetValue() )
                else:
                    break
                j = j + 1
            #collect the parameter of user
            parameter.user_parm.funcs_parms.append( self.dlg_userparm )
            if( len( parameter.user_parm.funcs_parms[-1] ) >= 3 ):
                if ( parameter.designer_parm.dlgs_parms[ self.dlg_name ][-3][0] == 'TextCtrl' ):
                    parameter.user_parm.imgs_names.append( self.dlg_userparm[ -1 ] )
            else:
                #parameter.user_parm.imgs_names.append( parameter.user_parm.imgs_names[ \
                #self.dlg_userparm[ -1 ] ] )
                pass
            self.parm_inper( parameter.user_parm )
            self.img_draw( parameter.user_parm.imgs[ \
                              parameter.user_parm.imgs_names[ -1 ] ],\
                       parameter.user_parm.imgs_names[ -1 ] )
            self.preview_timer.Stop()
            self.preview_timer.Destroy()
        else:
            self.img_draw( parameter.user_parm.imgs[ \
            parameter.user_parm.imgs_names[ -1 ] ], parameter.user_parm.imgs_names[ -1 ] )
            self.preview_timer.Stop()
            self.preview_timer.Destroy()

    def checkbox_handler( self, event ):
        if( self.control_set[ -3 ].GetValue() == 1 ):
            self.preview_timer.Start(50./15)
        elif( self.control_set[ -3 ].GetValue() == 0 ):
            self.preview_timer.Stop()
            self.img_draw( parameter.user_parm.imgs[ \
            parameter.user_parm.imgs_names[ -1 ] ], \
            parameter.user_parm.imgs_names[ -1 ] )

    def preview_handler( self, event ):
        user_tempparm = parameter.UserParm()
        func_tempparam = []
        func_tempparam.append( self.dlg_name )
        j = 0
        for i in parameter.designer_parm.dlgs_parms[ self.dlg_name ]:
            if( i[0] == 'ChoiceCtrl' ):
                if( len(i) == 2 ):
                    func_tempparam.append( \
                      self.control_set[ j ].GetSelection() )
                else:
                    func_tempparam.append( \
                    i[2][ self.control_set[ j ].GetSelection() ] )
            elif( i[0] == 'TextCtrl' or i[0] == 'Slider' ):
                func_tempparam.append( \
                 self.control_set[ j ].GetValue() )
            else:
                break
            j = j + 1
        #collect the parameter of user
        user_tempparm.funcs_parms.append( func_tempparam )
        self.img_draw( self.parm_inper( user_tempparm ).imgs[ \
        func_tempparam[ -1 ] ], func_tempparam[ -1 ] )






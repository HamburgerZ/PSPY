# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        fuction_dialog
# Purpose:
#
# Author:      John
#
# Created:     12/10/2017
# Copyright:   (c) John 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
import cv2

#############
##please import neccessary library

#transform one type of color_space to another type.
class CvtcolorDlg( wx.Dialog ):
    #initialize dialog
    def __init__( self, image_name, system_task, image_dict, show_dlg, temp_bitmap ):
        wx.Dialog.__init__( self, None, -1, 'cvtcolor', size = ( 300, 300 ) )
##initialization
        self.CVTCOLOR_NAME = [ 'cv2.COLOR_BGR2GRAY', 'cv2.COLOR_BGR2RGB' ]
        self.cvtcolor_ID = 1
        self.input_name = ''
        self.cvtcolor_method = 0
        self.output_name = ''
        self.handle_data = []
        self.preview_timer = wx.Timer( self )
##interface
        #drop_down list box about image inputted.
        self.input_label = wx.StaticText( self, -1, 'Input:', (10, 10) )
        self.cvtcolor_choice1 = wx.Choice( self, -1, ( 110, 10 ), size = ( 100, 30 ),  choices = image_name )
        #drop_down list box about transforming the color_space.
        wx.StaticText( self, -1, 'way:', (10, 110 ) )
        self.cvtcolor_choice2 = wx.Choice( self, -1, ( 110, 110 ), size = ( 100, 30 ), choices = self.CVTCOLOR_NAME )
        #drop_down list box about image outputted
        self.output_label = wx.StaticText( self, -1, "Output:", ( 10, 150 ) )
        self.output_label = wx.TextCtrl( self, -1, pos = ( 110, 150 ), size=( 80, 30 ), style = wx.TE_PROCESS_ENTER )
        #OK and CANCEL button
        self.ok_button = wx.Button( self, wx.ID_OK, 'OK', pos=( 10, 210 ) )
        self.cancel_button = wx.Button( self, wx.ID_CANCEL, 'Cancel', pos = ( 110, 210 ) )
        #checkbox aobut preview
        self.cvtcolor_checkbox1 = wx.CheckBox( self, label = 'Preview',pos = ( 110, 240 ) )
        #show the interface
        self.Show(1)
##logic proceesing
        #bound control
        self.Bind( wx.EVT_CHECKBOX, lambda event, image_name = image_name, image_dict = image_dict, \
                    temp_bitmap = temp_bitmap, show_dlg = show_dlg : self.checkbox1_handler( event, \
                    image_name, image_dict, temp_bitmap, show_dlg ) )
        self.Bind( wx.EVT_TIMER, lambda event, image_name = image_name, image_dict = image_dict, \
                    temp_bitmap = temp_bitmap, show_dlg = show_dlg : self.preview_handler( event, \
                    image_name, image_dict, temp_bitmap, show_dlg ) )
        #close the dialog
        #when you touch the OK button
        if( self.ShowModal() == wx.ID_OK ):
            #collect the data from control
            self.input_name = image_name[ self.cvtcolor_choice1.GetSelection() ]
            self.cvtcolor_method = eval( self.CVTCOLOR_NAME[ self.cvtcolor_choice2.GetSelection() ] )
            self.output_name = self.output_label.GetValue()
            self.cvtcolor_data = [ self.cvtcolor_ID, self.input_name, self.cvtcolor_method, self.output_name ]
            #transfer data to the variable 'system_task'
            system_task.append( self.cvtcolor_data )
            image_name.append( self.output_name )
            #call function in opencv library
            image_dict[ self.output_name ] = cv2.cvtColor( image_dict[ self.input_name ], self.cvtcolor_method )
            cv2.imwrite( 'temp.bmp',  image_dict[ self.output_name ] )
            self.temp_image = cv2.imread( 'temp.bmp' )      #for saveing
            temp_bitmap.CopyFromBuffer( self.temp_image )
            dc = wx.BufferedDC( wx.ClientDC( show_dlg ), temp_bitmap )
            dc.DrawBitmap( temp_bitmap, 0, 0 )
            #destroy the timer and dialog
            self.preview_timer.Destroy()
            self.Destroy()
        #when you touch the cancel button.
        else:
            
            #self.temp_image = image_dict[ self.input_name ]
            #temp_bitmap.CopyFromBuffer( self.temp_image )
            #dc = wx.BufferedDC( wx.ClientDC( show_dlg ), temp_bitmap )
            #dc.DrawBitmap( temp_bitmap, 0, 0 )
            
            #destroy the timer and dialog
            self.preview_timer.Destroy()
            self.Destroy()
            
    #preview
    def checkbox1_handler( self, event, image_name, image_dict, temp_bitmap, show_dlg ):
        #select the checkbox
        if( self.cvtcolor_checkbox1.GetValue() == 1 ):
            self.preview_timer.Start( 50./15 )
        #unselect the checkbox
        elif( self.cvtcolor_checkbox1.GetValue() == 0 ):
            #stop timer
            self.preview_timer.Stop()
            #draw image
            self.temp_image = image_dict[ self.input_name ]
            temp_bitmap.CopyFromBuffer( self.temp_image )
            dc = wx.BufferedDC( wx.ClientDC( show_dlg ), temp_bitmap )
            dc.DrawBitmap( temp_bitmap, 0, 0 )
    #preview
    def preview_handler( self, event, image_name, image_dict, temp_bitmap, show_dlg ):
        #collect the data from controls
        self.input_name = image_name[ self.cvtcolor_choice1.GetSelection() ]
        self.cvtcolor_method = eval( self.CVTCOLOR_NAME[ self.cvtcolor_choice2.GetSelection() ] )
        self.temp_image = cv2.cvtColor( image_dict[ self.input_name ], self.cvtcolor_method )
        #draw the image
        cv2.imwrite( 'temp.bmp',  self.temp_image )
        self.temp_image = cv2.imread( 'temp.bmp' )
        temp_bitmap.CopyFromBuffer( self.temp_image )
        dc = wx.BufferedDC( wx.ClientDC( show_dlg ), temp_bitmap )
        dc.DrawBitmap( temp_bitmap, 0, 0 )

#########################################################################
##################    please add your class   ###########################
#thresholding
class ThresholdDlg( wx.Dialog ):
    #initialize dialog
    def __init__( self, image_name, system_task, image_dict, show_dlg, temp_bitmap ):
        wx.Dialog.__init__( self, None, -1, 'cvtcolor', size = ( 300, 600 ) )
##initialization
        self.THRESHOLD_NAME = [ 'cv2.THRESH_BINARY', 'cv2.THRESH_BINARY_INV' ]
        self.threshold_ID = 2
        self.input_name = ''
        self.threshold_yuzhi = 127
        self.threshold_max = 255
        self.threshold_method = 0
        self.output_name = ''
        self.preview_timer = wx.Timer(self)
##interface
        #drop_down list about image inputted.
        wx.StaticText( self, -1, 'Input:', (10, 10) )
        self.threshold_choice1 = wx.Choice( self, -1, ( 110, 10 ), size = ( 100, 30 ),  choices = image_name )
        #slider about threshold value
        self.threshold_slider1 = wx.Slider( self,-1,50,1,255,pos=( 10, 60 ),size=(250,-1),style = wx.SL_AUTOTICKS|wx.SL_LABELS )#control about slider
        self.threshold_slider1.SetTickFreq( 1 ) #scale about slider
        #slider about max value
        self.threshold_slider2 = wx.Slider( self,-1,50,1,255,pos=( 10, 110 ),size=(250,-1),style = wx.SL_AUTOTICKS|wx.SL_LABELS )#control about slider
        self.threshold_slider2.SetTickFreq( 1 ) #scale about slider
        #the way of thresholding
        wx.StaticText( self, -1, 'way:', (10, 160 ) )
        self.threshold_choice2 = wx.Choice( self, -1, ( 110, 160 ), size = ( 100, 30 ), choices = self.THRESHOLD_NAME )
        #input text used for naming the image.
        self.output_label = wx.StaticText( self, -1, "Output:", ( 10, 210 ) )
        self.output_text = wx.TextCtrl( self, -1, pos = ( 110, 210 ), size=( 80, 30 ), style = wx.TE_PROCESS_ENTER )
        #OK and Cancel button
        self.ok_button = wx.Button( self, wx.ID_OK, 'OK', pos=( 50, 260 ) )
        self.cancel_button = wx.Button( self, wx.ID_CANCEL, 'Cancel', pos = ( 200, 260 ) )
        #checkbox
        self.threshold_checkbox1 = wx.CheckBox( self, label = 'Preview',pos = ( 10, 310 ) )
##logical processing
##bound control
        #checkbox
        self.Bind( wx.EVT_CHECKBOX, lambda event, image_name = image_name, image_dict = image_dict, \
                    temp_bitmap = temp_bitmap, show_dlg = show_dlg : self.checkbox1_handler( event, \
                    image_name, image_dict, temp_bitmap, show_dlg ) )
        self.Bind( wx.EVT_TIMER, lambda event, image_name = image_name, image_dict = image_dict, \
                    temp_bitmap = temp_bitmap, show_dlg = show_dlg : self.preview_handler( event, \
                    image_name, image_dict, temp_bitmap, show_dlg ) )
        #show
        self.Show(1)
        #when you touch the OK button
        if( self.ShowModal() == wx.ID_OK ):

            self.input_name = image_name[ self.threshold_choice1.GetSelection() ]
            self.threshold_yuzhi = self.threshold_slider1.GetValue()
            self.threshold_max = self.threshold_slider2.GetValue()
            self.threshold_method = eval( self.THRESHOLD_NAME[ self.threshold_choice2.GetSelection() ] )
            self.output_name = self.output_text.GetValue()
            self.threshold_data = [ self.threshold_ID, self.input_name, self.threshold_yuzhi, self.threshold_max, \
            self.threshold_method, self.output_name ]
            #transfer the data to variable 'system_task'
            system_task.append( self.threshold_data )
            image_name.append( self.output_name )
            #show the image
            ret, image_dict[ self.output_name ] = cv2.threshold( image_dict[ self.input_name ], self.threshold_yuzhi, \
            self.threshold_max, self.threshold_method )
            cv2.imwrite( 'temp.bmp',  image_dict[ image_name[ len( image_name ) - 1 ] ] )
            temp_image = cv2.imread( 'temp.bmp' )
            temp_bitmap.CopyFromBuffer( temp_image )
            dc = wx.BufferedDC( wx.ClientDC( show_dlg ), temp_bitmap )
            dc.DrawBitmap( temp_bitmap, 0, 0 )
            #destroy the timer and dialog
            self.preview_timer.Destroy()
            self.Destroy()
        else:
            self.preview_timer.Destroy()
            self.Destroy()
    #the function link up the checkbox
    def checkbox1_handler( self, event, image_name, image_dict, temp_bitmap, show_dlg ):
        if( self.threshold_checkbox1.GetValue() == 1 ):
            #start the timer
            self.preview_timer.Start(50./15)
        elif( self.threshold_checkbox1.GetValue() == 0 ):
            self.preview_timer.Stop()
    #the sub-function
    def preview_handler( self, event, image_name, image_dict, temp_bitmap, show_dlg ):

        self.input_name = image_name[ self.threshold_choice1.GetSelection() ]
        self.threshold_yuzhi = self.threshold_slider1.GetValue()
        self.threshold_max = self.threshold_slider2.GetValue()
        self.threshold_method = eval( self.THRESHOLD_NAME[ self.threshold_choice2.GetSelection() ] )
        ret, temp_image = cv2.threshold( image_dict[ self.input_name ], self.threshold_yuzhi, self.threshold_max, \
        self.threshold_method )
        cv2.imwrite( 'temp.bmp', temp_image )
        temp_image = cv2.imread( 'temp.bmp' )
        temp_bitmap.CopyFromBuffer( temp_image )
        dc = wx.BufferedDC( wx.ClientDC( show_dlg ), temp_bitmap )
        dc.DrawBitmap( temp_bitmap, 0, 0 )


if __name__ == "__main__":
    pass





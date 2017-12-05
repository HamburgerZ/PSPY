# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        MenuFrame
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
import handle_interpreter
import function_dialog

##MainPanel
class MainPanel(wx.Panel):
    def __init__(self, parent, ico ):
        wx.Panel.__init__(self, parent )
        self.frame = parent

##Main Dialog
class MainMenu(wx.Frame):
    #initialization
    def __init__(self):
        wx.Frame.__init__(self, None, size=( 600, 58 ), title = "Hamburger" )
        self.ICO_NAME = 'ico.ico'  #the name of  ico
        self.FILE_TYPE1 = "image source (*.bmp; *.jpg; *.png)|*.bmp;*.jpg;*.png"
        self.FILE_TYPE2 = "image source (*.bmp; *.jpg; *.png)|*.bmp;*.jpg;*.png"
        self.FILE_TYPE3 = "hamburger source (*.txt)|*.txt"
        self.FILE_TYPE4 = "hamburger source (*.txt)|*.txt"
        self.system_task = []      #list about task
        self.read_program = ''     #string which is read from file
        self.write_program = ''    #string which is written to file
        self.image_name = []       #list about images'name
        self.image_dict = {}       #dictionary about images
        self.temp_bitmap = wx.Bitmap() #the bitmap used for showing
        self.image_width = 0       #the width of image
        self.image_heigth = 0      #the heigth of image
###interface
        #show the icon
        self.image_ico = wx.Icon( self.ICO_NAME, wx.BITMAP_TYPE_ICO )
        self.SetIcon( self.image_ico )
        self.panel = MainPanel(self, ico = self.image_ico )
###show the mainmenu
        #submenu1
        menu_submenu1 = wx.Menu()
        open_image_option = menu_submenu1.Append( -1, 'open image' )
        save_image_option = menu_submenu1.Append( -1, 'save image' )
        open_file_option = menu_submenu1.Append( -1, 'open file' )
        save_file_option = menu_submenu1.Append( -1, 'save file' )
        execute_option = menu_submenu1.Append( -1, 'execute' )
        #submenu2
        menu_submenu2 = wx.Menu()
        cvtcolor_option = menu_submenu2.Append( -1, 'cvtcolor' )
        threshold_option = menu_submenu2.Append( -1, 'threshold' )

        ##########################################################
        ######################please add the submenu##################

        #submenu3
        menu_submenu3 = wx.Menu()
        undo_option = menu_submenu3.Append( -1, 'undo' )
        #main menu
        frame_menu = wx.MenuBar()
        frame_menu.Append( menu_submenu1, 'file' )
        frame_menu.Append( menu_submenu2, 'process' )
        frame_menu.Append( menu_submenu3, 'tool' )
        self.SetMenuBar( frame_menu )

##logic processing
###bound control
        self.Bind( wx.EVT_MENU, self.open_image_handler, open_image_option )
        self.Bind( wx.EVT_MENU, self.save_image_handler, save_image_option )
        self.Bind( wx.EVT_MENU, self.open_file_handler, open_file_option )
        self.Bind( wx.EVT_MENU, self.save_file_handler, save_file_option )
        self.Bind( wx.EVT_MENU, self.threshold_handler, threshold_option )
        self.Bind( wx.EVT_MENU, self.undo_handler, undo_option )
        self.Bind( wx.EVT_MENU, self.execute_handler, execute_option )
        self.Bind( wx.EVT_MENU, self.cvtcolor_handler, cvtcolor_option )

        ####################################################################
        ##############please buoud controls##################

###message handle
    #open the image
    def open_image_handler(self, event):
        #create the dialog
        open_image_dlg = wx.FileDialog( self, message="Choose a file", defaultFile="",
            wildcard=self.FILE_TYPE1, style=wx.FD_OPEN )
        #message handle
        if ( open_image_dlg.ShowModal() == wx.ID_OK ):
            #initialization about data
            self.open_image_ID = 3
            self.temp_path = ""
            self.image_path = open_image_dlg.GetPaths()
            for i in self.image_path:
                self.temp_path = self.temp_path + i
            self.handle_data = [ self.open_image_ID, 'image_original', self.temp_path ]
            self.image_name.append( 'image_original' )
            self.system_task.append( self.handle_data )
            #transform color_space type to the type 'RGB'
            self.temp_image = cv2.imread( self.temp_path )
            self.temp_image = cv2.cvtColor( self.temp_image, cv2.COLOR_BGR2RGB )
            #get the data about images
            self.image_dict[ 'image_original' ] = self.temp_image
            self.image_heigth, self.image_width = self.image_dict['image_original'].shape[:2]
            self.temp_bitmap = wx.Bitmap.FromBuffer( self.image_width, self.image_heigth, self.image_dict['image_original'] )
            #create the dialog and draw the image
            self.show_dlg = wx.Dialog( self, title = 'Catchimage', size = ( self.image_width + 6, self.image_heigth + 29 ) )
            dc = wx.BufferedDC( wx.ClientDC( self.show_dlg ), self.temp_bitmap )
            dc.DrawBitmap(self.temp_bitmap, 0, 0)
            #show the dialog used for showing
            self.show_dlg.Show()
        #destroy the dialog
        open_image_dlg.Destroy()
    #save the image
    def save_image_handler(self,event):
        #create the dialog
        save_image_dlg = wx.FileDialog( self, message = "select the Save file style", defaultFile = "",
        wildcard = self.FILE_TYPE2, style=wx.FD_SAVE )
        #when you touch the OK button
        if save_image_dlg.ShowModal() == wx.ID_OK:
            #remind: distinguish varialbe 'picture_name' from variable 'image_name'
            self.picture_name = ""
            self.image_path = save_image_dlg.GetPaths()
            for i in self.image_path:
                self.picture_name = self.picture_name + i
            cv2.imwrite( self.picture_name, self.temp_image )
        #destroy the dialog
        save_image_dlg.Destroy()
    #open the file
    def open_file_handler( self, event ):
        #create the dialog
        open_file_dlg = wx.FileDialog( self, message="Choose a file", defaultFile="",
            wildcard = self.FILE_TYPE3, style=wx.FD_OPEN )
        #message handle
        if open_file_dlg.ShowModal() == wx.ID_OK:
            self.temp_path = ""
            self.file_path = open_file_dlg.GetPaths()
            for i in self.file_path:
                self.temp_path = self.temp_path + i
            self.file_txt = open( self.temp_path )
            self.read_program = self.file_txt.read()
            self.file_txt.close()
        #destroy the dialog
        open_file_dlg.Destroy()
        #transform string to list
        self.image_name, self.system_task = handle_interpreter.file_task( self.read_program )
    #save the file
    def save_file_handler( self, event ):
        #create the dialog
        save_file_dlg = wx.FileDialog( self, message="select the Save file style", defaultFile="",
        wildcard = self.FILE_TYPE4, style = wx.FD_SAVE )
        #when you touch the OK button
        if save_file_dlg.ShowModal() == wx.ID_OK:
            self.file_name = ""
            self.image_path = save_file_dlg.GetPaths()
            for i in self.image_path:
                self.file_name = self.file_name + i
            #transform list to string and save it as a file
            self.txt_file = open( self.file_name, 'w' )
            self.write_program = handle_interpreter.task_file( self.system_task )
            self.txt_file.write( self.write_program )
            self.txt_file.close()
        #destroy the dialog
        save_file_dlg.Destroy()
    #undo handle
    def undo_handler( self, event ):
        #pop to undo
        self.system_task.pop()
        self.image_name.pop()
        #draw the image after undoing
        cv2.imwrite( 'temp.bmp',  self.image_dict[ self.image_name[ len(self.image_name) - 1 ] ] )
        self.temp_image = cv2.imread( 'temp.bmp' )
        self.temp_bitmap.CopyFromBuffer( self.temp_image )
        dc = wx.BufferedDC( wx.ClientDC( self.show_dlg ), self.temp_bitmap )
        dc.DrawBitmap(self.temp_bitmap, 0, 0)
    #execute the file
    def execute_handler( self, event ):
        #import system_task and execute according the ID
        handle_interpreter.handle_explain( self.system_task, self.image_dict )
        #initialize the variable
        self.image_heigth, self.image_width = self.image_dict['image_original'].shape[:2]
        self.temp_bitmap = wx.Bitmap.FromBuffer( self.image_width, self.image_heigth, self.image_dict['image_original'] )
        self.show_dlg = wx.Dialog( self, title = 'Catchimage', size = ( self.image_width + 6, self.image_heigth + 29 ) )
        cv2.imwrite( 'temp.bmp',  self.image_dict[ self.image_name[ len( self.image_name ) - 1 ] ] )
        self.temp_image = cv2.imread( 'temp.bmp' )
        self.temp_bitmap.CopyFromBuffer( self.temp_image )
        #draw the image
        dc = wx.BufferedDC( wx.ClientDC( self.show_dlg ), self.temp_bitmap )
        dc.DrawBitmap(self.temp_bitmap, 0, 0)
        #show the image
        self.show_dlg.Show(1)
    #transform the color_space type
    def cvtcolor_handler( self, event ):
        try:
            #create the dialog
            cvtcolor_dlg = function_dialog.CvtcolorDlg( self.image_name, self.system_task, self.image_dict, \
            self.show_dlg, self.temp_bitmap )
        except Exception as e:
            wx.MessageBox( "You may not open the images or do some other neccessary operation before do that!", 'error' )

    ###########################################################################
    #######################please add the new function########################

    #threshold
    def threshold_handler( self, event ): 
        try:
            #create the dialog
            threshold_dlg = function_dialog.ThresholdDlg( self.image_name, self.system_task, self.image_dict, \
            self.show_dlg, self.temp_bitmap )
        except Exception as e:
            wx.MessageBox( "You may not open the images or do some other neccessary operation before do that!", 'error' )

if __name__ == '__main__':
    pass





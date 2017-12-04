# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        MainUI
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
import numpy as np
import menu_frame

#Application Framework

class MainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        main_dlg = menu_frame.MainMenu()
        main_dlg.Show()

if __name__ == "__main__":
    main_app = MainApp()
    main_app.MainLoop()

















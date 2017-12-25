#this file's function is drawing some graph
import matplotlib.pyplot as plt
import cv2

#you need to transfer a picture whose type is RGB
def colorhist( extend_img, extend_cspace ):
    if( extend_cspace == 'RGB' ):
        plt.figure( figsize=(5,5), dpi=100 )
        plt.subplot( 3, 1, 1 )
        plt.hist( extend_img[:,:,0][0], bins=70, range = [ 0, 255 ] )
        plt.subplot( 3, 1, 2 )
        plt.hist( extend_img[:,:,1][0], bins=70, range = [ 0, 255 ] )
        plt.subplot( 3, 1, 3 )
        plt.hist( extend_img[:,:,2][0], bins=70, range = [ 0, 255 ] )
        plt.show()
    elif( extend_cspace == 'HSV' ):
        plt.figure( figsize=(5,5), dpi=100 )
        hsv_img = cv2.cvtColor( extend_img, cv2.COLOR_RGB2HSV )
        plt.subplot( 3, 1, 1 )
        plt.hist( hsv_img[:,:,0][0], bins=70, range = [ 0, 255 ] )
        plt.subplot( 3, 1, 2 )
        plt.hist( hsv_img[:,:,1][0], bins=70, range = [ 0, 255 ] )
        plt.subplot( 3, 1, 3 )
        plt.hist( hsv_img[:,:,2][0], bins=70, range = [ 0, 255 ] )
        plt.show()
    elif( extend_cspace == 'GRAY' ):
        gray_img = cv2.cvtColor( extend_img, cv2.COLOR_RGB2GRAY )
        plt.figure( figsize=( 5, 2.5 ), dpi=100 )
        plt.subplot( 1, 1, 1 )
        plt.hist( gray_img[0], bins=70, range = [ 0, 255 ] )
        plt.show()

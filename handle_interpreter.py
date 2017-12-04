# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        handle_interpreter
# Purpose:
#
# Author:      John
#
# Created:     12/10/2017
# Copyright:   (c) John 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cv2

############
##import neccessary library

#transform 'system_task' to the 'write' whose type is stirng.
#we will save the 'write' as a file.
def task_file( system_task ):
    write = ''
    for i in system_task:
        for j in i:
            if(  isinstance( j, str ) == 1 ):
                write = write + j + ' '
                #print write
            else:
                write = write + str( j ) + ' '
                #print write
        write = write + '\n'
#    print write
    return write
#transform 'read_program' whose type is string to 'name' and 'prog'
def file_task( read_program ):
    prog = []
    prog_little = []
    name = []
    temp1 = read_program.split('\n')
    for i in temp1:
        k = i.split()
        if( k == [] ):
            break
        else:
            for j in k:
                if( j.isdigit() == 1 ):
                    prog_little.append( int( j ) )
                else:
                    prog_little.append( j )
            name.append( prog_little[ len( prog_little ) - 1 ] )
            prog.append( prog_little )
            prog_little = []
    name[0] = 'image_original'
    return name,prog
#explain the 'system_task' and execute it
def handle_explain( system_task, image_dict ):
    for i in system_task:
        #transform one type of color_space to another.
        if( i[0] == 1 ):
            image_dict[ i[3] ] = cv2.cvtColor( image_dict[ i[1] ], i[2] )
        #threshold
        elif( i[0] == 2 ):
            ret, image_dict[ i[5] ] = cv2.threshold( image_dict[ i[1] ], i[2], i[3], i[4] )
        #read image
        elif( i[0] == 3 ):
            image_dict['image_original'] = cv2.imread( i[2] )
            image_dict['image_original'] = cv2.cvtColor( image_dict['image_original'], cv2.COLOR_BGR2RGB )

        ############################################################
        #################please add your code#########################

if __name__ == "__main__":
    pass

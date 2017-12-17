import cv2
import parameter

def parm_inper( user_parm ): #input the instance of class UserParm
    #user_parm maybe a single list or set of list
    result = user_parm

    if( user_parm.funcs_parms[-1][0] == 'cvtcolor' ):
        user_parm.imgs[ user_parm.funcs_parms[-1][3] ] = \
    cv2.cvtColor( parameter.user_parm.imgs[ \
    parameter.user_parm.imgs_names[ \
    user_parm.funcs_parms[-1][1] ] ], \
    user_parm.funcs_parms[-1][2] )

    elif( user_parm.funcs_parms[-1][0] == 'openimg' ):
        user_parm.imgs[ user_parm.funcs_parms[-1][2] ] = \
    cv2.imread( user_parm.funcs_parms[-1][1][0] )
        user_parm.imgs[ user_parm.funcs_parms[-1][2] ] = \
    cv2.cvtColor( parameter.user_parm.imgs[ \
        user_parm.funcs_parms[-1][2] ], cv2.COLOR_BGR2RGB )

    elif( user_parm.funcs_parms[-1][0] == 'threshold' ):
        threshold, user_parm.imgs[ user_parm.funcs_parms[-1][5] ] = \
    cv2.threshold( parameter.user_parm.imgs[ \
    parameter.user_parm.imgs_names[ user_parm.funcs_parms[-1][1] ] ], \
    user_parm.funcs_parms[-1][2], \
    user_parm.funcs_parms[-1][3], \
    user_parm.funcs_parms[-1][4] )

    elif( user_parm.funcs_parms[-1][0] == 'reimage' ):
        parameter.user_parm.imgs_names.append( \
        parameter.user_parm.imgs_names[ parameter.user_parm.funcs_parms[-1][1] ] )
        print( parameter.user_parm.imgs_names )
        del parameter.user_parm.imgs_names[ \
        parameter.user_parm.funcs_parms[-1][1] ]
        parameter.user_parm.funcs_parms.pop()

    return result


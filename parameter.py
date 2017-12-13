
class UserParm:
    def __init__( self ):
        self.imgs_names = []
        self.imgs = {}
        self.funcs_parms = []

class DesignerParm:
    def __init__( self ):
        self.menus_parms = []
        self.ctrls_parms = []
        self.dlgs_parms = {}

adjustparm_dlg = {}
designer_parm = DesignerParm()
user_parm = UserParm()

# add the open image parameter

designer_parm.menus_parms.append( [ 'File', 'open image' ] )
designer_parm.menus_parms.append( [ 'File', 'save image' ] )
designer_parm.menus_parms.append( [ 'Edit', 'undo' ] )

designer_parm.menus_parms.append( [ 'Preprocess', 'BasicOperation', 'cvtcolor' ] )
designer_parm.menus_parms.append( [ 'Preprocess', 'BasicOperation', 'threshold' ] )

designer_parm.dlgs_parms[ 'cvtcolor' ] = \
( [ [ 'ChoiceCtrl','Input:' ], \
[ 'ChoiceCtrl', 'Way:', \
[ 'cv2.COLOR_BGR2GRAY', 'cv2.COLOR_BGR2RGB' ] ], \
[ 'TextCtrl', 'Output:' ], \
[ 'OkCancelPreview' ] ]  )

designer_parm.menus_parms.append( [ 'imgprocess', 'threshold' ] )

designer_parm.dlgs_parms[ 'threshold' ] = \
( [ [ 'ChoiceCtrl', 'Input:' ],\
[ 'Slider', 'Thres:', 1, 255, 1 ],\
[ 'Slider', 'MaxVal:', 1, 255, 1 ], \
[ 'ChoiceCtrl', 'Way:', \
[ 'cv2.THRESH_BINARY', 'cv2.THRESH_BINARY_INV' ] ],\
[ 'TextCtrl', 'Output:' ],
[ 'OkCancelPreview' ] \
] )
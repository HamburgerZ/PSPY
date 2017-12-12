# PSPY
PSPY is a digital image processing framework developed by python. You can use PSPY to process digital image conveniently like photoshop and add your own funcitons and interfaces easily by python. 
PSPY is suitalbe for friends who start to study the knowledge of opencv.
# Installtion
- You should install python3.</br> 
- You should install two lib:</br>
  - opencv_python</br>
  - wxpython</br>
- If you use the Windows, you could open the cmd and input:</br>
`
pip install opencv_python 
`</br>
`
pip install wxpython 
`
# Use conveniently like PS
- You can clone down the project and open the 'Main_UI.py' to run the software.</br>

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/PSPY_menu.PNG/></div>

- If you touch the 'file' in the menu and select the 'open image' in the list, the image will be shown in the window</br>
And we can process the digital image easily.</br>
- for example, you can touch the 'imgprocess' in the menu and select the 'cvtcolor' in the list, 
the image will transform type of RGB to type of gray.

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/cvt_process.PNG/></div>

- After that, you can select the 'threshold' in the same list and djust the parameter by yourself, 
you will see the different binary image when you use different parameters.</br>

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/thres_process.PNG/></div>

# Add your interface conveniently by python
**In fact,you can add your interface conveniently by python according the rule and you just only add the designer's parameter and your function.**
- you could add your option in the menu easily by adding the parameter.For example, If I want to add the option 'file' and the option 'imgprocess' to the menu, I can add these parameter.

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/file_parm.PNG/></div>
<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/imgprocess_parm.PNG/></div>

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/file_menu.png/></div>
<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/imgprocess_menu.png/></div>

- For example, I want to add a function to change the colorspace of image from one type to another type. I just add these code to their file.

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/cvt_parm.PNG/></div>

- And I want to add a function to draw an binary image. I just add these code to their file.

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/thres_parm.PNG/></div>

# Design thought

<div align=center><img src=https://github.com/HamburgerZ/PSPY/blob/master/picture/design_thought.PNG/></div>

          




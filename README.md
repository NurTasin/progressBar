# progressBar
A simple GUI progress bar to use in your python projects. This progress bar is based on tkinter library.

This package contains a progress bar. You can customize the functions of the progress bar.

This progress bar is completely based on graphics.py module.
And the graphics.py is a wrapper for tkinter.
graphics.py is python2 and python3 compatible.

basic syntax for loading function is written below:
    loading(title,screenWidth,screenHeight,timeToWait,successfull_text="Finished",back_anim=True,invert=False)

You can call the function by adding these line into your code:

import loadingScreen
loading(title,screenWidth,screenHeight,timeToWait,successfull_text="Finished",back_anim=True,invert=False)

N.B: You have to put this package on the path of your project. Otherwise you can't import this module into your project.

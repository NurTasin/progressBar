from graphics import *
import time
import random
def loading(title,screenWidth,screenHeight,timeToWait,successfull_text="Finished",back_anim=True,invert=False):
	win=GraphWin(str(title),int(screenWidth),int(screenHeight))
	if(invert==False):
		win.setCoords(0,0, screenWidth, screenHeight)
	elif(invert==True):
		win.setCoords(screenWidth,screenHeight,0,0)
	mainRect=Rectangle(Point(0,0), Point(screenWidth,screenHeight))
	mainRect.setFill(color_rgb(30,30,30))
	mainRect.draw(win)
	lstOfsubRect=[]
	global txt
	txt=Text(Point(screenWidth/2,screenHeight/2),"")
	global color
	color=color_rgb(0, 255, 0)
	for i in range(101):
		txt.undraw()
		txt=Text(Point(screenWidth/2,screenHeight/2), str(i)+"%")
		txt.setSize(30)
		txt.setTextColor(color_rgb(255,255,255))
		subRect=Rectangle(Point(0, 0),Point((screenWidth/100)*i, screenHeight))
		subRect.setFill(color_rgb(0,255,20))
		subRect.setOutline(color_rgb(0,255,20))
		lstOfsubRect.append(subRect)
		subRect.draw(win)
		txt.draw(win)
		time.sleep(timeToWait)

	txt.undraw()
	txt=Text(Point(screenWidth/2,screenHeight/2),successfull_text)
	txt.setTextColor(color_rgb(255,255,255))
	txt.setSize(30)
	txt.draw(win)
	if back_anim==True:
		for i in range(len(lstOfsubRect)):
			lstOfsubRect[-i].undraw()
			time.sleep(0.5/len(lstOfsubRect))
	win.close()
	
	
if __name__=="__main__":
	loading("Loading..", 700, 40,0.5,successfull_text="!!!!!")

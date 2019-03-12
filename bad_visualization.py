import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import time

class Point():
	def __init__(self, x, y):
		self.x=x
		self.y=y
		int(self.x)
		int(self.y)
	def move(self,x,y):
		self.x=self.x+x
		self.y=self.y+y
	def _str_(self):
		return "Print(%s,%s)"%(self.x,self.y)
	def getx(self):
		return self.x
	def gety(self):
		return self.y


roomx=1000
roomy=1000
hchos=[]
random.seed(1)
	

def wind_move():
	global hchos
	tmphchos=[]
	for i in hchos:
		if i.getx()>0 and i.getx()<300 and i.gety()>((1/3)*i.getx()+200) and i.gety()<((1/3)*i.getx()+300):
			i.x=i.x-3
			i.y=i.y-1
			if i.x>0:
				tmphchos.append(i)
		elif i.getx()>300 and i.getx()<900 and i.gety()>((1/7)*i.getx()+1800/7) and i.gety()<((1/2)*i.getx()+250):
			ax=i.getx()
			ay=i.gety()
			headforx=350
			#headforx=300+100*((1/2)*ax+250)/((1/7)*ax+1800/7)
			i.x=i.getx()-4*math.cos(math.atan((ay-headforx)/(ax-300)))
			i.y=i.gety()-4*math.sin(math.atan((ay-headforx)/(ax-300)))
			tmphchos.append(i)
		elif i.getx()>=900 and i.gety()>((1/7)*i.getx()+1800/7) and i.gety() < 700:
			i.x=i.getx()-4
			tmphchos.append(i)
		elif i.getx()>=900 and i.gety() >= 700 and i.gety() < (2*i.getx()-1100):
			i.y=i.gety()-4
			tmphchos.append(i)
		else:
			tmphchos.append(i)
	hchos=tmphchos
	
def point_move(i):
	x=i.getx()
	y=i.gety()
	if x==1 and y==101:
		if random.random()<0.5:
			i.x=2
		else:
			i.y=2
	elif x==1 and y==399:
		if random.random()<0.5:
			i.x=2
		else:
			i.y=398
	elif x==1 and y==399:
		if random.random()<0.5:
			i.x=2
		else:
			i.y=398
	elif x==299 and y==101:
		if random.random()<0.5:
			i.x=298
		else:
			i.y=102
	elif x==301 and y==1:
		if random.random()<0.5:
			i.x=302
		else:
			i.y=2
	elif x==301 and y==299:
		if random.random()<0.5:
			i.x=302
		else:
			i.y=298
	elif x==599 and y==1:
		if random.random()<0.5:
			i.x=598
		else:
			i.y=2
	elif x==601 and y==1:
		if random.random()<0.5:
			i.x=602
		else:
			i.y=2
	elif x==601 and y==299:
		if random.random()<0.5:
			i.x=602
		else:
			i.y=298
	elif x==999 and y==1:
		if random.random()<0.5:
			i.x=998
		else:
			i.y=2
	elif x==999 and y==299:
		if random.random()<0.5:
			i.x=998
		else:
			i.y=299
	elif x==999 and y==301:
		if random.random()<0.5:
			i.x=998
		else:
			i.y=301
	elif x==101 and y==401:
		if random.random()<0.5:
			i.x=102
		else:
			i.y=402
	elif x==101 and y==699:
		if random.random()<0.5:
			i.x=102
		else:
			i.y=698
	elif x==701 and y==701:
		if random.random()<0.5:
			i.x=702
		else:
			i.y=702
	elif x==701 and y==999:
		if random.random()<0.5:
			i.x=702
		else:
			i.y=998
	elif x==999 and y==999:
		if random.random()<0.5:
			i.x=998
		else:
			i.y=998
	elif x==101 and y>401 and y<699:
		tmp=random.random()*3
		if tmp<1:
			i.x=102
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==1 and y>100 and y<399:
		tmp=random.random()*3
		if tmp<1:
			i.x=2
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==299 and y>100 and y<299:
		tmp=random.random()*3
		if tmp<1:
			i.x=298
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==301 and y>1 and y<299:
		tmp=random.random()*3
		if tmp<1:
			i.x=302
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==599 and y>1 and y<301:
		tmp=random.random()*3
		if tmp<1:
			i.x=598
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==601 and y>1 and y<300:
		tmp=random.random()*3
		if tmp<1:
			i.x=602
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==299 and y>1 and y<299:
		tmp=random.random()*3
		if tmp<1:
			i.x=298
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==999 and y>1 and y<299:
		tmp=random.random()*3
		if tmp<1:
			i.x=998
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==999 and y>301 and y<699:
		tmp=random.random()*3
		if tmp<1:
			i.x=998
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==999 and y>701 and y<999:
		tmp=random.random()*3
		if tmp<1:
			i.x=998
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==701 and y>701 and y<999:
		tmp=random.random()*3
		if tmp<1:
			i.x=702
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x>1 and x<299 and y==101:
		tmp=random.random()*3
		if tmp<1:
			i.y=102
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>301 and x<599 and y==1:
		tmp=random.random()*3
		if tmp<1:
			i.y=2
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>601 and x<999 and y==1:
		tmp=random.random()*3
		if tmp<1:
			i.y=2
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1  
	elif x>301 and x<501 and y==299:
		tmp=random.random()*3
		if tmp<1:
			i.y=298
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>301 and x<501 and y==301:
		tmp=random.random()*3
		if tmp<1:
			i.y=302
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>600 and x<700 and y==301:
		tmp=random.random()*3
		if tmp<1:
			i.y=302
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>600 and x<700 and y==299:
		tmp=random.random()*3
		if tmp<1:
			i.y=298
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>800 and x<1000 and y==301:
		tmp=random.random()*3
		if tmp<1:
			i.y=302
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>1 and x<301 and y==399:
		tmp=random.random()*3
		if tmp<1:
			i.y=398
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>101 and x<301 and y==401:
		tmp=random.random()*3
		if tmp<1:
			i.y=402
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>101 and x<901 and y==699:
		tmp=random.random()*3
		if tmp<1:
			i.y=698
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>701 and x<901 and y==701:
		tmp=random.random()*3
		if tmp<1:
			i.y=702
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x>701 and x<999 and y==999:
		tmp=random.random()*3
		if tmp<1:
			i.y=998
		elif tmp<2:
			i.x=i.getx()+1
		else:
			i.x=i.getx()-1
	elif x==301 and y==400:
		tmp=random.random()*3
		if tmp<1:
			i.x=302
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==501 and y==300:
		tmp=random.random()*3
		if tmp<1:
			i.x=502
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==701 and y==300:
		tmp=random.random()*3
		if tmp<1:
			i.x=702
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==799 and y==300:
		tmp=random.random()*3
		if tmp<1:
			i.x=798
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	elif x==901 and y==700:
		tmp=random.random()*3
		if tmp<1:
			i.x=902
		elif tmp<2:
			i.y=i.gety()+1
		else:
			i.y=i.gety()-1
	else:
		tmp=random.random()*4
		if tmp<1:
			i.x=i.getx()+1
		elif tmp<2:
			i.y=i.gety()+1
		elif tmp<3:
			i.y=i.gety()-1
		else:
			i.x=i.getx()-1



def produce_point():
	global hchos,roomx,roomy
	for i in range(100):#one
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(1,100+i)
			hchos.append(a)
	for i in range(100):#two
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(1,300+i)
			hchos.append(a)
	for i in range(298):#three
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(102,400+i)
			hchos.append(a)
	for i in range(300):#four
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(301,i)
			hchos.append(a)
	for i in range(200):#four
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(299,i+100)
			hchos.append(a)
	for i in range(300):#five
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(600,i)
			hchos.append(a)
	for i in range(300):#six
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(701,700+i)
			hchos.append(a)
	for i in range(99):#seven
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(999,900+i)
			hchos.append(a)
	for i in range(200):#eight
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(999,i+600)
			hchos.append(a)
	for i in range(399):#nine
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(999,i+1)
			hchos.append(a)
	for i in range(298):#ten
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i,101)
			hchos.append(a)
	for i in range(699):#eleven
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+300,1)
			hchos.append(a)
	for i in range(200):#twelve
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+300,301)
			hchos.append(a)
	for i in range(199):#twelve
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+301,299)
			hchos.append(a)
	for i in range(100):#threeteen
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+600,300)
			hchos.append(a)
	for i in range(200):#fourteen
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+800,300)
			hchos.append(a)
	for i in range(300):#fifteen
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i,400)
			hchos.append(a)
	for i in range(600):#sixteen
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+100,699)
			hchos.append(a)
	for i in range(200):#seventeen
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+700,700)
			hchos.append(a)
	for i in range(300):#eighteen
		pr=0.00002                   #waiting for the function for the probility of producint HCHO molecles
		tmp=random.random()
		if(pr>tmp):
			a=Point(i+700,999)
			hchos.append(a)

#figure drawing and set
fig = plt.figure()   
ax = plt.axes(xlim=(0, roomx), ylim=(0, roomy))   
greenyellow, = ax.plot([],[],'ro',lw=0.1,color='greenyellow')
yellow, = ax.plot([],[],'ro',lw=0.1,color='yellow')
red, = ax.plot([],[],'ro',lw=0.1,color='red')
blue, = ax.plot([],[],'ro',lw=0.1,color='blue')

#-----------wall--------------
x1=np.array([0,0])
y1=np.linspace(100,200,2)
plt.plot(x1,y1,lw=8,color='black')

x2=np.array([0,0])
y2=np.linspace(300,400,2)
plt.plot(x2,y2,lw=8,color='black')

x3=np.array([100,100])
y3=np.linspace(400,700,2)
plt.plot(x3,y3,lw=8,color='black')

x4=np.array([300,300])
y4=np.linspace(0,300,2)
plt.plot(x4,y4,lw=8,color='black')

x5=np.array([600,600])
y5=np.linspace(000,300,2)
plt.plot(x5,y5,lw=8,color='black')

x6=np.array([700,700])
y6=np.linspace(700,1000,2)
plt.plot(x6,y6,lw=8,color='black')

x7=np.array([1000,1000])
y7=np.linspace(900,1000,2)
plt.plot(x7,y7,lw=8,color='black')

x8=np.array([1000,1000])
y8=np.linspace(600,800,2)
plt.plot(x8,y8,lw=8,color='black')

x9=np.array([1000,1000])
y9=np.linspace(0,400,2)
plt.plot(x9,y9,lw=8,color='black')

x10=np.linspace(0,300,2)
y10=np.array([100,100])
plt.plot(x10,y10,lw=8,color='black')

x11=np.linspace(300,1000,2)
y11=np.array([0,0])
plt.plot(x11,y11,lw=8,color='black')

x12=np.linspace(300,500,2)
y12=np.array([300,300])
plt.plot(x12,y12,lw=8,color='black')

x13=np.linspace(600,700,2)
y13=np.array([300,300])
plt.plot(x13,y13,lw=8,color='black')

x14=np.linspace(800,1000,2)
y14=np.array([300,300])
plt.plot(x14,y14,lw=8,color='black')

x15=np.linspace(0,300,2)
y15=np.array([400,400])
plt.plot(x15,y15,lw=8,color='black')

x16=np.linspace(100,900,2)
y16=np.array([700,700])
plt.plot(x16,y16,lw=8,color='black')

x18=np.linspace(700,1000,2)
y18=np.array([1000,1000])
plt.plot(x18,y18,lw=8,color='black')
#.........finally completed..........


def init():   
	greenyellow.set_data([],[] )
	yellow.set_data([],[] )
	red.set_data([],[] )
	blue.set_data([],[] )   
	return greenyellow,yellow,red,blue,  
  
def animate(ii):
	global roomx,roomy,looping,hchos   
	for i in hchos:
		point_move(i)
	produce_point()
	wind_move()
	
	thishchos=[]
	for i in hchos:
		if i.getx()>0 and i.getx()<1000 and i.gety()>0 and i.gety()<1000:
			thishchos.append(i)
	hchos=thishchos

	pointsize=25
	droomx=int(roomx/pointsize)
	droomy=int(roomy/pointsize)
	color=[[0 for i in range(droomx+1)] for i in range(droomy+1)]
	for i in hchos:
		color[int(i.getx()/pointsize)][int(i.gety()/pointsize)]=color[int(i.getx()/pointsize)][int(i.gety()/pointsize)]+1
	greenyellowx=[]
	greenyellowy=[]
	yellowx=[]
	yellowy=[]
	redx=[]
	redy=[]
	bluex=[]
	bluey=[]
	for i in hchos:
		if color[int(i.getx()/pointsize)][int(i.gety()/pointsize)]<2:
			greenyellowx.append(i.getx())
			greenyellowy.append(i.gety())
		elif color[int(i.getx()/pointsize)][int(i.gety()/pointsize)]<4:
			yellowx.append(i.getx())
			yellowy.append(i.gety())
		elif color[int(i.getx()/pointsize)][int(i.gety()/pointsize)]<6:
			redx.append(i.getx())
			redy.append(i.gety())
		else :
			bluex.append(i.getx())
			bluey.append(i.gety())

	thegreenyellowx=np.array(greenyellowx)
	thegreenyellowy=np.array(greenyellowy)
	greenyellow.set_data(thegreenyellowx, thegreenyellowy)

	theyellowx=np.array(yellowx)
	theyellowy=np.array(yellowy)
	yellow.set_data(theyellowx, theyellowy)

	theredx=np.array(redx)
	theredy=np.array(redy)
	red.set_data(theredx, theredy)

	thebluex=np.array(bluex)
	thebluey=np.array(bluey)
	blue.set_data(thebluex, thebluey)
	# print(ii)

	return greenyellow, yellow, red, blue,   
 
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=50, blit=True) 
plt.show()
  
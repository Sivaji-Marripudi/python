from matplotlib import pyplot as plt
x = [1,2,3,4,5,6]
y = [4,6,7,3,9,6]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y_axis")
plt.title("sivaji")
plt.show()

'''   USING STYLEPLOT TO DRAW NORMAL PLOT   '''

from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x = [1,2,3,4,5,6]
y = [3,2,6,8,8,4]
x1 = [2,4,6,8,10]
y1 = [3,4,2,5,3]
plt.plot(x,y,'g',label = "line one",linewidth = 5)
plt.plot(x1,y1,'c',label = "line two",linewidth = 5)
plt.title("2-d")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()
plt.legend()

'''      BAR GRAPHS     '''

from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x = [1,2,3,4,5,6,7,8,9]
y = [2,4,5,3,6,1,7,8,5]
plt.bar(x,y,linewidth = 5,label = "bars")
plt.title("bar graph")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()
#plt.legend()

from matplotlib import pyplot as plt
from matplotlib import style
x = [1,2,3,4,5]
y = [2,4,6,8,9]
x1 = [2,4,6,8,10,12,14]
y1 = [1,3,5,7,9,11,13]
x2 = [1,5,10,15,20,25,30,35]
y2 = [10,20,30,40,50,60,70,80]
plt.bar(x,y,color = "g",label = "example one",linewidth = 6)
plt.bar(x1,y1,color = "k",label = "example two",linewidth = 5)
plt.bar(x2,y2,color = "c",label = "example three",linewidth = 4)
plt.title("bar graph")
plt.legend()
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()

'''     Scatter graphs   '''
from matplotlib import pyplot as plt
from matplotlib import style
x = [1,2,3,4,5,6,7,8,9]
y = [2,4,6,8,10,12,14,16,18]
plt.scatter(x,y,label = "skit",marker = 1)
plt.title("scatter graph")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()

'''     Stack_plot (or) Area plot  '''
from matplotlib import pyplot as plt
days  = [1,2,3,4,5]
sleeping = [2,3,4,5,6]
eating = [1,2,3,4,5]
working = [3,4,5,6,7]
plt.plot([],[],color = "g",linewidth = 5)
plt.plot([],[],color = "r",linewidth= 6)
plt.plot([],[],color = "b",linewidth = 5)
plt.plot([],[],color = "c",linewidth = 5)
plt.stackplot(days,sleeping,eating,working,colors = ["m","c","g","r"])
plt.title("stack plot")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()

''' pie chart '''

from matplotlib import pyplot as plt
from matplotlib import style
labels = "python","c","c++","java"
sizes = [90,30,40,70]
colors = ["green","red","yellow","black"]
explode = (0,0.1,0,0)
plt.pie(sizes,labels,colors = colors,shadow = True,labels = labels,explode = explode,startangle = 100)
plt.title("pie charts")
plt.axis("equal")
plt.show()

import matplotlib.pyplot as plt
# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

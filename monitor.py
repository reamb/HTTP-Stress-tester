from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil
from itertools import count
import time

def plot():
    fig, (ax1, ax2) = plt.subplots(2)

    y1 = []
    y2 = []
    x = []

    def animate(i):
        t = time.time()
        x.append(t)
		
        y1.append(psutil.cpu_percent())
        y2.append((psutil.virtual_memory().used >> 20)/1000)
		
        ax1.cla()
        ax2.cla()
        ax1.grid()
        ax2.grid()
		    # grid 
		
        ax1.set_title("CPU Usage")
		    # cpu usage
        ax2.set_title("Memory Usage")
        fig.subplots_adjust(hspace=0.4)
        ax1.set(ylabel="% Usage")
        ax2.set(ylabel="Memory in GB", xlabel="time")
		
		
        ax1.plot(x,y1)
        ax2.plot(x,y2)
        ax1.annotate('%0.2f' % y1[-1], xy=(1, y1[-1]), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
        ax2.annotate('%0.2f' % y2[-1], xy=(1, y2[-1]), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
    
	
	ani = FuncAnimation(fig, animate, interval=(1000))
    plt.show()

plot()

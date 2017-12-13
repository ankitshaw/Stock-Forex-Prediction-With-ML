import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick
import matplotlib.dates as mdates
import numpy as np
import time as t

def bytedate2num(fmt):
	def converter(b):
		return mdates.strpdate2num(fmt)(b.decode('ascii'))
	return converter

date,bid,ask = np.loadtxt('GBPUSD1d.txt',unpack=True,
			delimiter=',',
			converters={0:bytedate2num('%Y%m%d%H%M%S')})

def changePercent(start, end):
	return ((end-start)/start)*100

def getPattern():
	avgLine = ((bid+ask)/2)
	x = len(avgLine)-30
	y = 11

	while y < x:
		p = []
		for j in range(9,-1,-1):
			p.append(changePercent(avgLine[y-10], avgLine[y-j]))

		outcomeRange = avgLine[y+20:y+30]
		currentPoint = avgLine[y]
		print(np.mean(outcomeRange))
		print(currentPoint)
		print(p)
		t.sleep(5)
		print('___')
		y += 1

def graph():

		fig = plt.figure(figsize=(10,7))
		ax = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
		
		ax.set_color_cycle(['green', 'red'])
		ax.plot(date,bid)
		ax.plot(date,ask)
		ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

		ax2 = ax.twinx()
		ax2.fill_between(date, 0.0, (ask-bid), facecolor='cyan', alpha=0.3)

		plt.grid(True)
		plt.show()

def main():
	#graph()
 	getPattern()

main()
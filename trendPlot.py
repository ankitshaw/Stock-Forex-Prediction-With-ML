import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick
import matplotlib.dates as mdates
import numpy as np

def bytedate2num(fmt):
	def converter(b):
		return mdates.strpdate2num(fmt)(b.decode('ascii'))
	return converter

def graph():
		date,bid,ask = np.loadtxt('GBPUSD1d.txt',unpack=True,
			delimiter=',',
			converters={0:bytedate2num('%Y%m%d%H%M%S')})
		
		fig = plt.figure(figsize=(10,7))
		ax = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
		
		ax.set_color_cycle(['green', 'red'])
		ax.plot(date,bid)
		ax.plot(date,ask)
		
		ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

		plt.grid(True)
		plt.show()

def main():
	graph()

main()

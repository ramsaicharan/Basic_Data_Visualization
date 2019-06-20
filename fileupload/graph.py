import matplotlib.pyplot as plt
import openpyxl
from django.conf import settings as sb


def graph(x):

	book=openpyxl.load_workbook(sb.BASE_DIR+'/fileupload/static/upload/'+x)

	sheet=book.active

	max_rows=sheet.max_row

	l=[]
	m=[]
	for row in range(2,max_rows+1):
	    l.append(sheet[row][1].value)
	    m.append(sheet[row][2].value)
	    

	plt.figure(figsize=(13,6))

	plt.plot(l,m)
	plt.xlabel(sheet[1][1].value)
	plt.ylabel(sheet[1][2].value)
	plt.grid()
	plt.savefig('fileupload/static/upload/graph.png')
	

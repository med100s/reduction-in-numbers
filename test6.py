import sys
sys.setrecursionlimit(10000)

def triangle(row):
	if len(row) == 1:
		if type(row) == list:
			row = ''.join(row)
		print(type(row))	
		print(row)
		return row
	else:
		list(row)
		m = []
		for i in range(len(row)-1):
			if row[i] == 'R' and row[i+1] == 'R':
				m.append('R')
			elif row[i] == 'R' and row[i+1] == 'B':
				m.append('G')
			elif row[i] == 'R' and row[i+1] == 'G':
				m.append('B')
			elif row[i] == 'G' and row[i+1] == 'R':
				m.append('B')
			elif row[i] == 'G' and row[i+1] == 'B':
				m.append('R')
			elif row[i] == 'G' and row[i+1] == 'G':
				m.append('G')
			elif row[i] == 'B' and row[i+1] == 'R':
				m.append('G')
			elif row[i] == 'B' and row[i+1] == 'B':
				m.append('B')
			elif row[i] == 'B' and row[i+1] == 'G':
				m.append('R')
		row = m 
		triangle(row)
triangle('RGBR')
triangle('RBRGBRBGGRRRBGBBBGG')
triangle('GRB')

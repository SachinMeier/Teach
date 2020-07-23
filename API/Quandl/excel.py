import xlsxwriter as excel

class Excel:
	def __init__(self, name):
		self.name = name
		self.workbook = excel.Workbook(name)
		self.sheets = [self.workbook.add_worksheet()]

	def write_dict(self, sheet_idx, data):
		row = 0
		col = 0
		for k in data.keys():
			self.sheets[sheet_idx].write(row, col, k)
			self.sheets[sheet_idx].write(row, col+1, data[k])
			row += 1

	def write_2d_ist(self, sheet_idx, data):
		row = 0
		col = 0
		for i in data:
			for j in i:
				self.sheets[sheet_idx].write(row, col, j)
				col += 1
			row += 1

	def new_sheet(self):
		self.sheets.append(self.workbook.add_worksheet())

	def close(self):
		self.workbook.close()


import pandas as pd







class CreateExcel:


	def __init__(self, dict_df):
		total_length = 0
		mismatches = {}
		writer = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')
		workbook = writer.book

		# format5 = workbook.add_format({'bg_color': '#B9D3EE', 'border_color': '#BFBFBF', 'border': 1})  # dark blue
		# format6 = workbook.add_format({'bg_color': '#DBE8F0', 'border_color': '#BFBFBF', 'border': 1})  # light blue
		format5 = workbook.add_format({'bg_color': '#A3E7FF'})  # dark blue
		format6 = workbook.add_format({'bg_color': '#FFFFFF'})  # light blue

		current_color = 'Dark'

		for key in dict_df:
			df = dict_df[key]
			df = df.where(df.notnull(), None)
			if not df.empty:
				df.to_excel(writer, sheet_name=key, index=False)
				worksheet = writer.sheets[key]

				def format_row(row, color=current_color):
					if color == 'Dark':
						for column in range(0, 11):  # format the first 2 columns
							worksheet.write(row, column, df.iloc[row - 1, column], format5)

					elif color == 'Light':
						for column in range(0, 11):  # format the first 2 columns
							worksheet.write(row, column, df.iloc[row - 1, column], format6)

				# Format the 1st row
				format_row(1)
				# Start formatting from the 2nd row until the end of the df
				for row in range(2, df.shape[0] + 1):
					# if the id of the row is the same as the id of the previous row
					if df.iloc[row - 1, 0] == df.iloc[row - 2, 0]:
						format_row(row, color=current_color)
					# if it's different than that of the previous row switch the colors
					else:
						if current_color == 'Dark':
							current_color = 'Light'
						elif current_color == 'Light':
							current_color = 'Dark'
						format_row(row, color=current_color)

				for column in df:
					column_width = max(df[column].astype(str).map(len).max(), len(column))
					col_idx = df.columns.get_loc(column)
					worksheet.set_column(col_idx, col_idx, column_width)

				total_length += len(df)
				mismatches[key] = len(df)

		if total_length > 0:
			writer.close()
			print("Total Mismatches")
			for k, v in mismatches.items():
				print(f"{k}: {v}")

		else:
			print("No mismatches were found")



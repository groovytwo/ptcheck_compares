import pandas as pd

class CreateExcel:
	def __init__(self, dict_df):
		total_length = 0
		mismatches = {}
		writer = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')
		for key in dict_df:
			df = dict_df[key]
			if not df.empty:
				df.to_excel(writer, sheet_name=key, index=False)

				for column in df:
					column_width = max(df[column].astype(str).map(len).max(), len(column))
					col_idx = df.columns.get_loc(column)
					writer.sheets[key].set_column(col_idx, col_idx, column_width)

				total_length += len(df)
				mismatches[key] = len(df)

		if total_length > 0:
			writer.close()
			print("Total Mismatches")
			for k, v in mismatches.items():
				print(f"{k}: {v}")

		else:
			print("No mismatches were found")

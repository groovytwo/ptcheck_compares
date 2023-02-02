import pandas as pd

from my_convert import fetch_sister_val_in_cfg
from my_initialize import open_in_os



class CreateExcel:


	def __init__(self, dict_df, cfg):
		total_length = 0
		mismatches = {}
		writer = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')
		workbook = writer.book

		format1 = workbook.add_format({'bg_color': cfg.color.addition_bg, 'font_color': cfg.color.addition_txt})
		format2 = workbook.add_format({'bg_color': cfg.color.removal_bg, 'font_color': cfg.color.removal_txt})
		format3 = workbook.add_format({'bg_color': cfg.color.edit1_bg, 'font_color': cfg.color.edit_new_txt, 'bold': 'true'})
		format4 = workbook.add_format({'bg_color': cfg.color.edit1_bg, 'font_color': cfg.color.edit_old_txt})
		format5 = workbook.add_format({'bg_color': cfg.color.edit2_bg, 'font_color': cfg.color.edit_new_txt,'bold': 'true'})
		format6 = workbook.add_format({'bg_color': cfg.color.edit2_bg, 'font_color': cfg.color.edit_old_txt})

		edit_color = 'Edit1'

		for key in dict_df:

			# Setup col variables
			merge_col = fetch_sister_val_in_cfg(cfg, cfg.dataframe.df_list, "name", key, "merge_col")
			dupes_col = fetch_sister_val_in_cfg(cfg, cfg.dataframe.df_list, "name", key, "dupes_col")

			df = dict_df[key]
			df = df.where(df.notnull(), None)

			if not df.empty:
				df.to_excel(writer, sheet_name=key, index=False, freeze_panes=(1, 0))
				worksheet = writer.sheets[key]

				def format_row(row, color=edit_color):

					if df.iloc[row - 1, dupes_col] == "no":
						if df.iloc[row - 1, merge_col] == cfg.file.ptcheck_new_tag:
							my_format = format1
						else:
							my_format = format2
					else:
						if color == 'Edit1':
							if df.iloc[row - 1, merge_col] == cfg.file.ptcheck_new_tag:
								my_format = format3
							else:
								my_format = format4
						elif color == 'Edit2':
							if df.iloc[row - 1, merge_col] == cfg.file.ptcheck_new_tag:
								my_format = format5
							else:
								my_format = format6
					for column in range(0, (dupes_col + 1)):
						worksheet.write(row, column, df.iloc[row - 1, column], my_format)

				format_row(1)
				# Start formatting from the 2nd row until the end of the df
				for row in range(2, df.shape[0] + 1):
					# if the id of the row is the same as the id of the previous row
					if df.iloc[row - 1, 0] == df.iloc[row - 2, 0]:
						format_row(row, color=edit_color)
					# if it's different than that of the previous row switch the colors
					else:
						if edit_color == 'Edit1':
							edit_color = 'Edit2'
						elif edit_color == 'Edit2':
							edit_color = 'Edit1'
						format_row(row, color=edit_color)

				header_format = workbook.add_format({
					'bold': True,
					'fg_color': cfg.color.header_bg,
					'border': 0,
					'size': 10})

				for col_num, value in enumerate(df.columns.values):
					worksheet.write(0, col_num, value, header_format)

				for column in df:
					column_width = max(df[column].astype(str).map(len).max(), len(column))
					col_idx = df.columns.get_loc(column)
					worksheet.set_column(col_idx, col_idx, column_width + 2)

				total_length += len(df)
				mismatches[key] = len(df)

		if total_length > 0:
			try:
				writer.close()

				open_in_os("output.xlsx")
			except PermissionError:
				print(f"[Errno 13] Permission denied.\nPlease close output.xlsx and try again.")
			# writer.close()
			# print("Total Mismatches")
			# for k, v in mismatches.items():
			# 	print(f"{k}: {v}")

		else:
			print("No mismatches were found")



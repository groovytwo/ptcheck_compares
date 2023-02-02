import re

# from pandas import Dataframe

import pandas as pd


def dataframe_difference(df1: pd.DataFrame, df2: pd.DataFrame, which=None):
	"""Find rows which are different between two DataFrames."""
	comparison_df = df1.merge(df2, indicator=True, how='outer')
	if which is None:
		diff_df = comparison_df[comparison_df['_merge'] != 'both']
	else:
		diff_df = comparison_df[comparison_df['_merge'] == which]
	return diff_df


class CreateDictDataframe:
	def __init__(self, cfg, file_path):
		self.dict_df = pd.read_excel(file_path, sheet_name=cfg.dataframe.names_list)
		self.parse_remote_info()
		for df_cfg in cfg.dataframe.df_list:
			df_cfg = getattr(cfg, df_cfg)
			df = self.dict_df[df_cfg.name]

			# Drop first eight rows
			df = df.drop(df.index[0:7])
			# Drop empty columns
			df = df.drop(df.columns[df_cfg.delete_col], axis=1)
			# Assign column names from first row
			df.columns = df_cfg.col_names
			# Drop first row that was used to name columns in previous step
			# df.drop(index=df.index[0], axis=0, inplace=True)
			# Drop rows that are all 'nan'
			df = df.dropna(axis=0, how='all')
			df.reset_index(drop=True, inplace=True)

			self.dict_df[df_cfg.name] = df

	def parse_remote_info(self):
		# Get the first dictionary value from dict_df
		first_key = list(self.dict_df.keys())[0]
		# Fetch remote info string (including name + desc)
		remote_info = self.dict_df[first_key].iat[5, 0]
		remote_string = re.match("(.*?)\s-\s(.*?)\s\((.*)\)", remote_info)
		self.remote_name = remote_string.group(1)
		self.remote_desc = remote_string.group(2)

class CreateDiffDataframe:
	def __init__(self, sheet1, sheet2, cfg):
		self.df = {}
		for df_cfg in cfg.dataframe.df_list:
			df_cfg = getattr(cfg, df_cfg)
			key_col = df_cfg.col_names[df_cfg.key_col]
			df1 = sheet1.dict_df[df_cfg.name]
			df2 = sheet2.dict_df[df_cfg.name]
			new_df = dataframe_difference(df1, df2)
			new_df['_dupes'] = new_df[key_col].duplicated(keep=False).astype(int).astype(str)
			new_df = new_df.replace({'_dupes': {'0': "no", '1': "yes"}})
			new_df = new_df.replace('left_only', cfg.file.ptcheck1_tag)
			new_df = new_df.replace('right_only', cfg.file.ptcheck2_tag)
			new_df = new_df.sort_values(key_col)
			self.df[df_cfg.name] = new_df


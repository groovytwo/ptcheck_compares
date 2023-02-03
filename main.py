from my_dataframe import CreateDictDataframe, CreateDiffDataframe
from my_excel import CreateExcel
from my_initialize import ConfigParser

import easygui as gui


cfg = ConfigParser()

open1_title = f"Select {cfg.file.ptcheck_old_tag} Excel file to compare."
file1_type = "*.xlsx"
file1_path = gui.fileopenbox(title=open1_title, default=fr"{cfg.file.ptcheck_old_path}")

open2_title = f"Select {cfg.file.ptcheck_new_tag} Excel file to compare."
file2_type = "*.xlsx"
file2_path = gui.fileopenbox(title=open2_title, default=fr"{cfg.file.ptcheck_new_path}")

sheet1 = CreateDictDataframe(cfg, file1_path)
sheet2 = CreateDictDataframe(cfg, file2_path)

diff_df = CreateDiffDataframe(sheet2, sheet1, cfg)

CreateExcel(diff_df.df, cfg)


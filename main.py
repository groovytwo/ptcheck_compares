from my_dataframe import CreateDictDataframe, CreateDiffDataframe
from my_excel import CreateExcel
from my_initialize import ConfigParser

import easygui as gui

open1_title = f"Select old Excel file to compare.."
file1_type = "*.xlsx"
file1_path = gui.fileopenbox(title=open1_title, default=file1_type)

open2_title = f"Select new Excel file to compare.."
file2_type = "*.xlsx"
file2_path = gui.fileopenbox(title=open2_title, default=file2_type)


cfg = ConfigParser()

sheet1 = CreateDictDataframe(cfg, file2_path)
sheet2 = CreateDictDataframe(cfg, file1_path)

diff_df = CreateDiffDataframe(sheet1, sheet2, cfg)

CreateExcel(diff_df.df, cfg)


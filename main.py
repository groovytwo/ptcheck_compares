from my_dataframe import CreateDictDataframe, CreateDiffDataframe
from my_excel import CreateExcel
from my_initialize import ConfigParser

cfg = ConfigParser()

sheet1 = CreateDictDataframe(cfg, cfg.file.ptcheck1_path)
sheet2 = CreateDictDataframe(cfg, cfg.file.ptcheck2_path)

diff_df = CreateDiffDataframe(sheet1, sheet2, cfg)

CreateExcel(diff_df.df)


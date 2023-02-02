from my_dataframe import CreateDictDataframe, compare_cols
from my_initialize import ConfigParser

cfg = ConfigParser()

sheet1 = CreateDictDataframe(cfg, cfg.file.ptcheck1_path)
sheet2 = CreateDictDataframe(cfg, cfg.file.ptcheck2_path)

diff_df = compare_cols(sheet1, sheet2, cfg)

print("Ending")


from my_dataframe import test_df
from my_initialize import ConfigParser

cfg = ConfigParser()

sheet1 = test_df(cfg, cfg.file.ptcheck1_path)

print("Ending")


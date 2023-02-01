from my_dataframe import CreateDictDataframe
from my_initialize import ConfigParser

def dataframe_difference(df1, df2, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(
        df2,
        indicator=True,
        how='outer'
    )
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df.to_csv('data/diff.csv')
    return diff_df

cfg = ConfigParser()

sheet1 = CreateDictDataframe(cfg, cfg.file.ptcheck1_path)
sheet2 = CreateDictDataframe(cfg, cfg.file.ptcheck2_path)

df1 = sheet1.dict_df['Analog']
df2 = sheet1.dict_df['Analog']

check = df1.compare(df2)

check = dataframe_difference(df1, df2)


# https://www.statology.org/pandas-can-only-compare-identically-labeled-series-objects/
print("Ending")


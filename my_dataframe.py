import re
import pandas as pd


def parse_remote_info(dict_df):
    # Get the first dictionary value from dict_df
    first_key = list(dict_df.keys())[0]
    # Fetch remote info string (including name + desc)
    remote_info = dict_df[first_key].iat[5, 0]
    remote_string = re.match("(.*?)\s-\s(.*?)\s\((.*)\)", remote_info)
    remote_name = remote_string.group(1)
    remote_desc = remote_string.group(2)
    return remote_name, remote_desc

def test_df(cfg, file_path):
    dict_df = pd.read_excel(file_path, sheet_name=cfg.dataframe.names_list)

    # Get the first dictionary value from dict_df
    remote_name, remote_desc = parse_remote_info(dict_df)


    # Lookup the Remote Name & Description

    for df_cfg in cfg.dataframe.df_list:
        df_cfg = getattr(cfg, df_cfg)
        df = dict_df[df_cfg.name]

        # Drop first four rows
        df = df.drop(df.index[0:3])
        # Drop rows after Description
        df = df.drop(df.index[1:4])
        # Drop empty columns
        df = df.drop(df.columns[df_cfg.delete_col], axis=1)
        # Assign column names from first row
        df.columns = df.iloc[0]
        # Drop first row that was used to name columns in previous step
        df.drop(index=df.index[0], axis=0, inplace=True)
        # Drop rows that are all 'nan'
        df = df.dropna(axis = 0, how = 'all')
        df.reset_index(drop=True, inplace=True)

        if "defined" in (df.iat[0, 0]): # If dataframe is empty
            # Delete row that says points are not defined
            df.drop(index=df.index[0], axis=0, inplace=True)

        dict_df[df_cfg.name] = df
    return dict_df


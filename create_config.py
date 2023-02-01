import configparser

config = configparser.ConfigParser()
config.add_section('file')
config.set('file', '# section Purpose', 'General file settings')
config.set('file', 'assets_path', './assets')
config.set('file', 'config_path', './config')
config.set('file', 'doc_path', './documentation')
config.set('file', 'readme', 'Readme.pdf')

config.add_section('dataframe')
config.set('dataframe', '# section Purpose', 'General Dataframe Settings')

config.set('dataframe', 'excel_df_filter', 'sheet')

config.add_section('analog_sheet')
config.set('analog_sheet', 'name', 'Analog')

config.add_section('status_sheet')
config.set('status_sheet', 'name', 'Status')

config.add_section('rate_sheet')
config.set('rate_sheet', 'name', 'Rate')

with open(r"config.ini", 'w') as configfile:
    config.write(configfile)

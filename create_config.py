import configparser

config = configparser.ConfigParser()
config.add_section('file')
config.set('file', '# section Purpose', 'General file settings')
config.set('file', 'assets_path', './assets')
config.set('file', 'config_path', './config')
config.set('file', 'doc_path', './documentation')
config.set('file', 'readme', 'Readme.pdf')
config.set('file', 'ptcheck_new_path', 'H_SK_PRD.xlsx')
config.set('file', 'ptcheck_new_tag', 'PRD')
config.set('file', 'ptcheck_old_path', 'H_SK_TST.xlsx')
config.set('file', 'ptcheck_old_tag', 'TST')

config.add_section('dataframe')
config.set('dataframe', '# section Purpose', 'General Dataframe Settings')

config.set('dataframe', 'excel_df_filter', 'sheet')

config.add_section('analog_sheet')
config.set('analog_sheet', 'name', 'Analog')
config.set('analog_sheet', 'delete_col', '[13, 11, 10, 8, 7, 3, 0]')
config.set('analog_sheet', 'col_names', '["Analog Name", "Analog Description", "EGU Min", '
                                        '"EGU Max", "Units", "Address1", "Address2", "Display", "Group"]')
config.set('analog_sheet', 'key_col', '0')
config.set('analog_sheet', 'merge_col', '9')
config.set('analog_sheet', 'dupes_col', '10')

config.add_section('status_sheet')
config.set('status_sheet', 'name', 'Status')
config.set('status_sheet', 'delete_col', '[12, 9, 8, 5, 4, 3, 0]')
config.set('status_sheet', 'col_names','["Status Name",  "Status Description",  "Bit 1 Address",  '
                                  '"Bit 2 Address",  "Open/On/Start",  "Close/Off/Stop",  "Display",  "AlmTxt",  "Group"]')
config.set('status_sheet', 'key_col', '0')
config.set('status_sheet', 'merge_col', '9')
config.set('status_sheet', 'dupes_col', '10')

config.add_section('rate_sheet')
config.set('rate_sheet', 'name', 'Rate')
config.set('rate_sheet', 'delete_col', '[13, 11, 9, 7, 3, 0]')
config.set('rate_sheet', 'col_names', '["Rate Name", "Rate Description", "EGU Min", "EGU Max",  '
                                   '"Units", "Type", "Pulse Address", "Analog Address", "Display", "Group"]')
config.set('rate_sheet', 'key_col', '0')
config.set('rate_sheet', 'merge_col', '10')
config.set('rate_sheet', 'dupes_col', '11')

config.add_section('color')
config.set('color', '# section Purpose', 'Excel Color Codes')
config.set('color', 'header_bg', 'FFE66D') # gold
config.set('color', 'header_txt', '000000')  # black
config.set('color', 'addition_bg', 'CAFFBF') # green
config.set('color', 'addition_txt', '00642D')  # dark green
config.set('color', 'removal_bg', 'FFADAD') # red
config.set('color', 'removal_txt', '700000')  # dark red
config.set('color', 'edit1_bg', 'FFD6A5') # burnt orange
config.set('color', 'edit2_bg', 'FBF8CC') # pale yellow
config.set('color', 'edit_new_txt', '00823B')  # dark green
config.set('color', 'edit_old_txt', 'C00000')  # dark brown

with open(r"config.ini", 'w') as configfile:
	config.write(configfile)

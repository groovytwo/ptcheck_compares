import configparser

config = configparser.ConfigParser()
config.add_section('file')
config.set('file', '# section Purpose', 'General file settings')
config.set('file', 'assets_path', './assets')
config.set('file', 'config_path', './config')
config.set('file', 'doc_path', './documentation')
config.set('file', 'readme', 'Readme.pdf')
config.set('file', '# ptcheck_new_path', 'The path that you will be copying TO, reflecting the final state that you want.')
config.set('file', 'ptcheck_new_path', r'C:\Users\aellery\OneDrive - Pembina Pipeline Corporation\Desktop\*.xlsx')
config.set('file', 'ptcheck_new_tag', 'Production')
config.set('file', '# ptcheck_old_path', 'The path that you will be copying FROM')
config.set('file', 'ptcheck_old_path', r'C:\Users\aellery\OneDrive - Pembina Pipeline Corporation\Desktop\*.xlsx')
config.set('file', 'ptcheck_old_tag', 'Development')

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
config.set('color', 'header_bg', 'abb3ba')
config.set('color', 'header_txt', '000000') 
config.set('color', 'addition_bg', 'c6f0c2') 
config.set('color', 'addition_txt', '000000') 
config.set('color', 'removal_bg', 'f0c2c2') 
config.set('color', 'removal_txt', '000000')
config.set('color', 'edit1_bg', 'FFFFFF')
config.set('color', 'edit2_bg', 'e4edf6')
config.set('color', 'edit_new_txt', '184c7f') 
config.set('color', 'edit_old_txt', 'b22b08') 

with open(r"config.ini", 'w') as configfile:
	config.write(configfile)

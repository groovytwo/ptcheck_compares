import ast
import configparser
import os
import subprocess

from my_convert import stringlist_to_list, common_var_values_from_list_instance_names, list_filtered_instance_variables

def open_in_os(my_file_path):
    if os.name == 'nt':  # Windows only
        os.startfile(my_file_path, 'open')
    elif os.path.exists(my_file_path):  # Mac
        subprocess.call(["open", my_file_path])

class ConfigSubGroup:
    def __init__(self, section, conf, format_values):
        # Dynamically creating the subclass elements
        for (each_key, each_val) in conf.items(section):
            if format_values:
                if each_val.startswith("[") and each_val.endswith("]"):
                    each_val = stringlist_to_list(each_val)
                elif each_val.startswith("{") and each_val.endswith("}"):
                    each_val = ast.literal_eval(each_val)
                elif each_val == "True":
                    each_val = True
                elif each_val == "False":
                    each_val = False
                elif each_val.isdigit():
                    each_val = int(each_val)
            setattr(self, each_key, each_val)

class ConfigParser:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read("config.ini")
        for each_section in conf.sections():
            if each_section == "color":
                format_values = False
            else:
                format_values = True
            # Dynamically creating the sub class
            # https://stackoverflow.com/questions/12620602/creating-a-class-with-all-the-elements-specified-in-a-file-using-configparser
            setattr(self, each_section, ConfigSubGroup(each_section, conf, format_values))
        self.dataframe.df_list = list_filtered_instance_variables(self, self.dataframe.excel_df_filter)
        self.dataframe.names_list = common_var_values_from_list_instance_names(
            self.dataframe.df_list, self, "name")
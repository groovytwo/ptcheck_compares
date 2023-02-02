import ast


def stringlist_to_list(stringlist):
    return ast.literal_eval(stringlist)

def list_filtered_instance_variables(my_object, my_prefix):
	my_result = list(my_object.__dict__.keys())
	filtered_result = [x for x in my_result if my_prefix in x]
	return filtered_result

def common_var_values_from_list_instance_names(list_object_names, source, var_name):
	# Use this to get common variables across multiple dataframes
	final_list = []
	for x in list_object_names:
		my_object = (getattr(source, x))
		my_final_var = (getattr(my_object, var_name))
		final_list.append(my_final_var)
	return final_list

def fetch_sister_val_in_cfg(cfg_obj, scan_list, known_key, known_value, unknown_key):
	# Use this to parse through a series of subgroups to fina a sister value
	for subgroup_name in scan_list:
		subgroup = getattr(cfg_obj, subgroup_name)
		value = getattr(subgroup, known_key)
		if value == known_value:
			return getattr(subgroup, unknown_key)


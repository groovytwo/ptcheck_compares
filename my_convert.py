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
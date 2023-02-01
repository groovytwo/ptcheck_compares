import ast


def stringlist_to_list(stringlist):
    return ast.literal_eval(stringlist)

#!/usr/bin/python3
#a function that replaces all occurrences of an element by another in a new list
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))

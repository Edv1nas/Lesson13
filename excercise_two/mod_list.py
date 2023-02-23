from typing import List

def add_items_to_list(extended_list: List [str]) ->List:
    new_list = []
    for items in extended_list:
        new_list.append(items.upper())
    return new_list
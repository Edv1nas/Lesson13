from typing import List

# list_a = ['dasdas', 'dasdas', 'dasdasd']

# def unique_list(item_list: List [str]) -> List:

#     for a in item_list:
#         unique_list = (set(item_list))
#     return unique_list

# unique_list(item_list=unique_list)


def unique_values(str_list: List[str])-> List[str]:
    new_str_list = []
    for value in str_list:
        
        new_str_list.append(len(set(value)))
            
    return new_str_list
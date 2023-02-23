import mod_list
import mod_unique
import mod_str
import logging

# add sentence to list
sentence = "Hello world or not"
sentence_list = mod_str.convert(sentence)



# changes all list items letters to upper
upper_letters = mod_list.add_items_to_list(sentence_list)

# count unique letter in list
unique_letter_list = mod_unique.unique_values(upper_letters)
print(unique_letter_list)
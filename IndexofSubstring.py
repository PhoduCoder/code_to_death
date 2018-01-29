#!/usr/bin/python
#######################################################################
# Author : Gaurav Parashar
# Description : This is used to search a substring in a big string
#and then return the indexes of all substring as a list.

#For now, the value of the string is hard-coded
#as well as the value of substring is hard-coded
#But they can be easily taken as user-input
#######################################################################
#######################################################################

string_value = "abc us def abc xyz abc bca abcabc abca abcabcabc"
#another_string = "this is a test string that is created for test purpose. This is to test your understanding of what is taught. so good luc with the test"

#another_substring = "test"

substring_value = "abc"

length_of_substring = len(substring_value)
#another_length = len(another_substring)


first_index = string_value.index(substring_value)
#first_index = another_string.index(another_substring)

#print (first_index)

last_index = string_value.rindex(substring_value)
#last_index = another_string.rindex(another_substring)

#print (last_index)

i = first_index + length_of_substring
#i = first_index + another_length

#print (i)

index_list = []
index_list.append(first_index)
#index_list.append(last_index)

print (index_list)

while (i < last_index):
    next_index = string_value.index(substring_value, i)
    #next_index = another_string.index(another_substring, i)
    i = next_index+length_of_substring
    #i = next_index+another_length
    #print (next_index)
    #print ("=========")
    index_list.append(next_index)
else:
    index_list.append(last_index)
    print (index_list)

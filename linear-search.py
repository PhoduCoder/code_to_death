#!/usr/bin/python
#######################################################################
# Author : Gaurav Parashar
# Description : This is used to search for a particular element among
#		a given set of elements.
#######################################################################
#######################################################################

def linear_search(search_number):
    # This will take one parameter
    # This will return -1 if the element
    # is not present
    # When the element is present,
    # It should return a success message
    # alongwith the number of iterations

    print (' The number to be searched is %d' % search_number)
    # compare the search element with every element in the list.
    # For each element , one needs to set a flag, whose initial
    # value is set to False. If the element is found within the list
    # then the flag is set to True

    flag = False
    num_of_iterations = 0

    for x in range(len(number_list)):
        num_of_iterations = num_of_iterations + 1
        if (number_list[x] == search_number):
            # set the flag as True
            flag = True
            #print ("Executing True-IF")
            return flag, num_of_iterations
        else:
            flag = False
            #print ("Executing False-IF")
            # return flag

    return flag, num_of_iterations

number_list = [1, 9, 2, 8, 3, 7, 4, 6, 5]
print("Enter the number to find")
input_number = int(raw_input())

return_value, counter = linear_search(input_number)

# Check for the Return Value
if (return_value == False):
    print ('The number was not found!')
else:
    print ('The number is found!')

print ('The number of iterations were %d' %counter)

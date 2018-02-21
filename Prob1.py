#print all numbers from 2000 to 3200

num_list = []

num_list2 = []

for i in range(2000, 3201):
    num_list.append(i)
    if ((i%7)==0 and (i%5)!=0):
        #num_list2.append(i)
        num_list2.append(str(i))
        print i,

#print num_list.len()

print len(num_list2)
print len(num_list)

#print ','.join(num_list2)
# This will through a error 
# TypeError: sequence item 0: expected string, int found
print ','.join(num_list2)

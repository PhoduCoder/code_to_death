my_matrix=[[2,3],[100,200]]

my_sec_matrix=[[4,5],[7,9],[100,200]]

#Print the matrix

def print_matrix(m):
    for i in m:
        for j in i:
            print j,
        print ("\n")

print_matrix(my_matrix)

print_matrix(my_sec_matrix)

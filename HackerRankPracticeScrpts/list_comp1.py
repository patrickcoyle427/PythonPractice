#!usr/bin/python3

# Let's learn about list comprehensions! 
# You are given three integers x, y and z representing the dimensions 
# of a cuboid along with an integer . 
# You have to print a list of all possible coordinates 
# given by n on a 3D grid where the sum of is not equal to n.

def list_comp1(test_case)
	
    x, y, z, n = test_case

    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k) !=n)])

 
if __name__ == '__main__':

    cases = [(1,1,1,2), (2,2,2,2), (4,5,6,-10), (0,0,0,0), (2,3,4,5)]

    for case in cases:

        list_comp1(case)

        
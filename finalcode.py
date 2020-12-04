# A basic code for matrix input from user 
def main():
        R = int(input()) 
        C = 8

        # Initialize matrix 
        matrix = [] 
        list=[]
        for i in range(R):
            K=input().replace(" ","")
            list.append(K)
        for i in range(R):		 # A for loop for row entries 
            a =[] 
            for j in range(C):	 # A for loop for column entries 
                a.append(list[i][j])
            matrix.append(a)

        """
        # For user input 
        for i in range(R):		 # A for loop for row entries 
            a =[] 
            for j in range(C):	 # A for loop for column entries 
                a.append((input())) 
            matrix.append(a) """

        # For printing the matrix 
        """for i in range(R): 
            for j in range(C): 
                print(matrix[i][j], end = "") 
            print("\n") """

        list1=[]
        list2=[]
        for i in range(R): 
            for j in range(C): 
                    if matrix[i][j]=="M":
                            list1.append((i,j))
                    
        for i in range(R): 
            for j in range(C): 
                    if matrix[i][j]=="V":
                            list2.append((i,j))                 
        distance=[]
        for val in list1:
            if list2[0][1]>3:
                partition=2;
                if val[1]>3:
                    distance.append(abs(val[0]-list2[0][0]))
                else:
                    distance.append(abs(val[0]-list2[0][0])+2)
            else:
                if val[1]>3:
                    distance.append(abs(val[0]-list2[0][0])+2)
                else:
                    distance.append(abs(val[0]-list2[0][0]))


        distance.sort()
        print(distance)
main()
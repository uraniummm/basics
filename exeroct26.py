


M1 =  [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[2,3,4],[5,6,7],[8,9,10]]

#  Exercise 1: What is the output of following and why?

matrix_length = len(M1)
for i in range(matrix_length):
       print(M1[i][-1])

#     OUTPUT:
              3
              6
              9
              #This result is because print(M1[i][-1]) prints values of last column for different rows


#  Exercise 2: What is the result of print(M1+M2) and why?              

print(M1+M2)

#        OUTPUT:

        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 3, 4], [5, 6, 7], [8, 9, 10]]

        #This result is expected because (M1+M2) adds rows of M2 as new rows in M1.


M1 = [[8, 14, -6],[12,7,4]]
M2 = [[3, 16, -6],[9,7,-4]]


# Exercise 3 : Evaluate sum of following using range() and len() function in for loop


M3=[[0,0,0],[0,0,0]]
for i in range(len(M1)):
    for j in range(len(M2)):
        M3[i][j]=M1[i][j]+M2[i][j]

print("M3:",M3)


              # OUTPUT :

              M3: [[11, 30, 0], [21, 14, 0]]


#  Exercise 4 : Write a program to multiply two square matrics. 


M1 =  [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[2,3,4],[5,6,7],[8,9,10]]
M3=[[0,0,0],[0,0,0],[0,0,0]]
M1len=len(M1)
M2len=len(M2)
s=0
q=1
for i in range(M1len):
    for j in range(M2len):
        s=0
        for k in range(len(M3)):
            q=M1[i][k]*M2[k][j]
            s=s+q
            M3[i][j]=s


print("New matrix:")
print(M3)


             # OUTPUT :

             New matrix:
             [[36, 42, 48], [81, 96, 111], [126, 150, 174]]
             


## Name: Nikita Rana


# QUESTION 1 : Write a program to sum all even integers between 0-100.

s= 0
for i in range(0,51):
    s=s+i*2
print(s)

         

# QUESTION 2 : Complete the exercises (regarding Break and Continue) as given in slides of 05 October 2020. 

# FIND OUTPUT OF THE FOLLOWING

for n in range(2, 10):
   for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

                

# FIND OUTPUT OF THE FOLLOWING

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*',n//x)
            break
        else:
            print(n, 'is a prime number')

                   

# FIND OUTPUT OF THE FOLLOWING

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)  
        continue
    print("Found a number", num)

                    
# FIND OUTPUT OF THE FOLLOWING

for num in range(2, 10):
  if num % 2 == 0:
        print("Found an even number", num)
        continue
        print("Found a number", num)

                    

# QUESTION 3 : Write a program to generate the Fibonacci series (by use of function) up to a specified number of terms. 

n=input("Please enter a no.:\n")
n=int(n)
def fib(x):
   a, b=0, 1
   c=0
   print("\nSeries is given as follows:\n")
   while(c<x):
        print(a,end='.')
        a, b=b, a+b
        c+=1
fib(n)

                    
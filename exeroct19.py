



  # EXERCISE 1: Generate a list of having (x,x**2,x**3) where x is in range (1,10)

  # FIRST METHOD:


#list1=[]
#for x in range(1,10):
#    list1.append((x,x**2,x**3))    
#print(list1)

              # OUTPUT:
              [(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]

  # SECOND METHOD:              

#list1=[(x,x**2,x**3)for x in range(1,10)]
#print(list1)
      
              # OUTPUT:
              [(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]





   # EXERCISE 2 : Generete  a list of (x, factorial(x)) where x is in range (1,10)

#def facto(n):
#    if n<=1:
#        return 1
#    else:
#        return n*facto(n-1)
    
  # FIRST METHOD :

#list1=[(x,facto(x))for x in range(1,10)]
#print(list1)

        # OUTPUT:
        [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720), (7, 5040), (8, 40320), (9, 362880)]
 
  # SECOND METHOD:

#list1=[]
#for x in range(1,10):
#    list1.append((x,facto(x)))

#print(list1)

        # OUTPUT :
        [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720), (7, 5040), (8, 40320), (9, 362880)]

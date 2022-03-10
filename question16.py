t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11, 13, 15)

def half():     # Printing half Numbers
    length = int(len(t1)/2)
    print(t1[:length])
    print(t1[length:])

def even_printing():   #printing Even Numbers
    t10 = []
    for i in range(len(t1)):
        if i%2 == 0:
            t10.append(i)
        else:
            continue
    t10 = tuple(t10)
    print(t10)

def multi():   # for adding both tuples, prining maximum and minimum values            
    t3 = t1 + t2
    print("Newly made tuple names as t3 is : ", t3)
    l = len(t3)
    print("Minimum value in ", t3, "is : ", min(t3))
    print("Maximum value in ", t3, "is : ", max(t3))

print("""
#           a. Print half the values of tuple in one line and the other half in the next line.
#           b. Print another tuple whose values are even numbers in the given tuple.
#           c. Concatenate a tuple t2=(11,13,15) with t1 and return maximum and minimum value from this tuple.
""")
while True:
    x = input("Enter a choice : ")
    x = x.lower()
    if x == 'a':
        half()
    elif x == 'b':
        even_printing()
    elif x == 'c':
        multi()
    elif x == "stop":
        break
    else:
        print("Recheck the Inputs :)")

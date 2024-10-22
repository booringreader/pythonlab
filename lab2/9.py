def even_odd_segregation(sample):
    even=0; odd=0
    for i in range(sample+1):
        if(i%2 == 0):
            even += i
        else:
            odd += i
    print("even: ", even, "\n", "odd: ", odd)

even_odd_segregation(int(input("enter end: ")))

def H():
    n=int(input("Enter n for row :"))
    m=int(input("Enter n for col :"))
    for i in range(n):
        for j in range(m):
            if i%2==0:
                print("#*",end="")
            else:
                print("*#",end="")
        print()
H()

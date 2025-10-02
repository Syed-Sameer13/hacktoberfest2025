try:
    a,b=map(int,input().split())
    print(a/b)
except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")

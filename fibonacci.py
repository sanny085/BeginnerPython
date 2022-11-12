n = int(input("Enter the range  : "))


def fibonacciSeries(n):
    i = 0
    res = []
    while i <= n:
        if i < 2:
            res.append(i)
        else:
            x = res[i-1]
            y = res[i-2]
            res.append(x+y)
        i += 1
    print("Fibonacci : ", res)


if n > 0:
    fibonacciSeries(n)
else:
    print("Invalid Number, Please enter a valid number")

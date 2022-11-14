class Calculation:
    def withoutloop(self, n):
        if n > 0:
            self.withoutloop(n - 1)
            print(n, end = " ")


rangeN = int(input("Enter a number :"))
p = Calculation()
p.withoutloop(rangeN)

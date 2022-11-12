"""
Find sum of two prime number equal to number
Enter Your Number : 39


Output
answer is : Yes
All prime Number : [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


"""

number = int(input("Enter Your Number : "))
def findAllPrimeNumber(number):
    i = 1
    allPrimeNumber = {1}
    while i < number:
        if i <= 2:
            allPrimeNumber.add(2)
        else:
            j = 2
            Flag = False
            while j < i:
                if i % j == 0:
                    Flag = True
                    break
                j += 1
            if not Flag:
                allPrimeNumber.add(i)
        i += 1
    return list(allPrimeNumber)


def sumOfTwoPrimeNUmber(prime, number):
    answer = ''
    prime.sort()
    length = len(prime)
    for x in range(length):
        for y in range(length):
            if x != y and prime[x] + prime[y] == number:
                answer = "Yes"
                break
            else:
                answer = "No"
    print("answer is :", answer)


prime = findAllPrimeNumber(number)
print("Set of all prime number is",prime)
if len(prime) > 0:
    sumOfTwoPrimeNUmber(prime, number)

print("All prime Number :", prime)

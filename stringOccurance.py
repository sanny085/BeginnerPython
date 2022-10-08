string = input('Enter Your String :')
sub_string = input('Enter Your Sub String :')


def findStringCount(string, sub_string):
    i = 0
    count = 0
    while i < len(string):
        index = string[i:].find(sub_string)
        print(index)
        if index > 0:
            count += 1
            i += index
        i += 1
    return count


if string and sub_string:
    result = findStringCount(string, sub_string)
    print('Total Number is :', result)
else:
    print('Enter string and substring')



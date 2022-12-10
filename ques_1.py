def find_len(list):
    length = len(list)
    list.sort()
    print(list[5])
    print(list[0])
    print(list[4])
    print(list[1])
    print(list[3])
    print(list[2])

list = [1,2,3,4,5,6]
largest = find_len(list)
#print(list.sort(),end = " ")
print('sorted list:',list)
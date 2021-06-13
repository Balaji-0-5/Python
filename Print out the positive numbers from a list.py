list1 = input("Please input the list of numbers \n(use commas to separate each entry): ").split(",")
list2 = []
for number in list1 :
    if float(number) >= 0:
        list2.append(number)
print(list2)

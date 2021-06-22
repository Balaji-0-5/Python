my_string = str(input("Please enter the string : "))

def most_frequent(string):
    """ Prints the letters from a string in decreasing order of frequency"""
    string1 = string.casefold()
    my_dict ={}
    for letter in string1:
        if letter not in my_dict:
            my_dict[letter] = string1.count(letter)
            continue
    list1 = sorted(my_dict.items())
    list2 = [(count,letter) for (letter,count) in list1]
    sorted_list = sorted(list2,reverse=True)
    answer = ""
    for (freq,letter) in sorted_list:
        answer += "{} = {} \n".format(letter,freq) 
    print(answer)
    
most_frequent(my_string)

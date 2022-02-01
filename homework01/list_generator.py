# make list of integers

listOfIntegers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# function to check if the int is odd/even

def check(listOfIntegers):

    for i in listOfIntegers:
        if (i % 2) == 0:
            print(i,' is even')
        else:
            print(i,' is odd')

check(listOfIntegers)

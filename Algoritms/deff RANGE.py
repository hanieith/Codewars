#You're working in a number zoo, and it seems that one of the numbers has gone missing!

#Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.

#In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.

#Task:
#Write a function that takes a shuffled list of unique numbers from 1 to n with one element missing (which can be any number including n). Return this missing number.

#Note: huge lists will be tested.

def find_missing_number(numbers):
    a = sum(range(len(numbers)+2))
    b = sum(numbers)
    z = a - b
    if z == 0:
        return numbers[-1] + 1
    else:
        return z
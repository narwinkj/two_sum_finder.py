# Two Sum Write a function that returns the element from a list that add up to a specific target value.
def find(sum):
    global set
    for i in list:
        for j in list:
            if i+j==sum :
                set.add((i,j))
    if len(set)==0:
        return("There's no matchin sum.")
    else:
        return sorted(set)
list=eval(input("Enter the list to work with : "))
sum=eval(input('Enter the sum to check for : '))
set=set()
print(find(sum))

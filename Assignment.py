'''
# if --elif--else
marks = 70

if marks < 35:
    print(" exam Failed")
elif marks == 35:
    print("Just cleared")
elif marks >35 and marks <50:
    print("second grade")
elif marks >50 and marks < 75:
    print(" first grade")
else:
    print("successfully cleared the exam")



# continue - print all even no. from 1 to 10 ,
    # 1%2 = 1 , 2%2 = 0, 5%2 = 1

for x in range(11):
     if x % 2 != 0:
         continue
     print(x)

# break
# check if rollno = 8 is there or not

rollno = [1,2,4,6,8,10,20,50,40,8,606,606,8,8]
for num in rollno:
    if num == 8:
        print("Yes")
        break

# pass
for i in range(5):
    pass


# Functions/method
# code resuable
# cleaner/neat/undersstanability

# function not returning
def evenNumberCheck(num):
    if num % 2 == 0:
        print("even number")
    else:
        print(" odd number")

evenNumberCheck(6)


# function that's returning
def evenNumberCheck(num):
    if num % 2 == 0:
        print("even number")
        return "even number"
    else:
        print("odd  number")
        return "odd number"

result  = evenNumberCheck(7)
print(" result is :" ,result)

'''

# 2 list of common elements from 2 sets

def findCommonElement(set1,set2):
    set3 = set1 & set2
    return set3

set1 = {1,2,3,4}
set2 = {1,2,5,6,7,8}
result  = findCommonElement(set1,set2)
#print(result)

# 3 converst string in to list of character
#def convertStringToList(s):
    #return list(s)

#s = input("enter a string: ")
#result  = convertStringToList(s)
#print(result)

# count the occurence of each element

def count_elements(input_list):
    counts = {}
    for ele in input_list:
        if ele in counts:
            counts[ele] = counts[ele] + 1
        else:
            counts[ele] = 1
    return counts

input_list = [1,2,3,5,5,1,4,3,5]
ans = count_elements(input_list)
print(ans)









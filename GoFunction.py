#Question 1

def perfect(n):
  total=0
  for x in range(1, n):
    if(n%x == 0):
      total = total + x
  if (total == n):
    return True
  else:
    return False

n = int(input('Please enter a number '))
print (perfect(n))


#__________________________________________________________________________________
#Question 2

def add_col(A, v):
  x = 0
  for i in A:
    i.append(v[x])
    x = x + 1
  return(A)

def add_row(A, v):
  A.append(v)
  return(A)

A = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]
v = [7, 8, 9]
print(add_col(A, v))

A = [[1, 3, 5], [2, 4, 6], [3, 5, 7]]
v = [7, 8, 9]
print(add_row(A, v))


#__________________________________________________________________________________
#Question 3

This_List = [[[['f'], ['g']], [['h'], ['i']]], [[['w'], ['x']], [['y'], ['z']]]]
for i in This_List:
  for a in i:
    for b in a:
      for c in b:
        print(c)


#__________________________________________________________________________________
#Question 4

def MyFunction(start):
  words = start.split()
  R = [i[::-1] for i in start[::-1]]
  answer = ""
  punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", ' ']
  for character in R:
    if(character not in punctuation):
      answer += character
  return(answer)
start = "Remove all puncation (leave nums and letters)! Also reverse this string."
print(MyFunction(start))

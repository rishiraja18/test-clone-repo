def multiply_by2(item):
   return item*2

def only_odd(item):
  return item % 2 != 0 

my_list = [1,2,3]
 
your_list = [4,5,6]

print("New changes git master")
print("Next changes git master")
print(list(map(lambda item: item*5,[1,2,3])))  

print(list(filter(lambda item: item % 2 != 0 ,[1,2,3,5,6])))  
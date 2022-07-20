# import requests

# r = requests.patch('https://httpbin.org / patch', data ={'key':'value'})
# print(r)
# print(r.content)










from turtle import home


def sum(my_list):
   my_total = 0
   for i in my_list:
      if (type(i) == type([])):
         my_total = my_total + sum(i)
      else:
         my_total = my_total + i
   return my_total
my_list = [[2,3], [7,9], [11,45], [78,98]]
print(my_list)
print(sum(my_list))
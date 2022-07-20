import requests
import json

url=requests.get('https://api.merakilearn.org/courses')
r=json.loads(url.text)
# print(r)
with open("requts.json","w") as f:
    json.dump(r,f,indent=4)
i=0
while i<len(r):
    print(i+1,r[i]["name"],r[i]["id"])
    i+=1
course_no=int(input("select which course you want display  :"))
print(course_no,r[course_no-1]["name"])
course_id=r[course_no-1]["id"]

url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
r1=json.loads(url1.text)
with open("parent.json","w") as f2:
    json.dump(r1,f2,indent=6)
print(r[course_no-1]['name'],"-",r[course_no-1]["id"])
serial=1
serial1=1
list=[]
list1=[]
n=1
for i in r1["course"]["exercises"]:
    if i["parent_exercise_id"]==None:
        print(serial,i["name"])
        print(" ",serial1,i["slug"])
        serial+=1
        list.append(i)
        list1.append(i)
    elif i["parent_exercise_id"]==i["id"]:
        print(serial,i["name"])
        serial+=1
        list.append(i)
    elif i["parent_exercise_id"]!=i["id"]:
        print(" ",n,i["name"])
        n+=1
        list1.append(i)
t=open("l.json","w")
json.dump(list,t,indent=3)
t=open("l1.json","w")
json.dump(list1,t,indent=3)



parent_id=int(input("enter enter no: "))
serial=1
for i in list1:
    if i["parent_exercise_id"]==i["id"]:
        print(serial,list1[parent_id-1]["name"])
        serial+=1
        break
    else:
        if i["parent_exercise_id"]!=i["id"]:
            print(serial,list1[parent_id-1]["name"])
            print("",list1[parent_id-1]["content"])
            serial+=1
            break












# in keyword  and iterations in dictionaries.....

u = {'name': 'shivi', 'age': 20}
if 'name' in u:    #we can check only keys not value pairs(if 'shivi' in u:  -> it will throw error )
    print(u['name'])

#checking value pair .....
if 'shivi' in u.values():
    print(u['name'])


#looping......

for i in u:
    print(i)   #it will print all keys.
for i in u.keys():
    print(i)   #this keys method will also check keys.
for i in u.values():
    print(i)   #it will print all values pair.
for i in u:
    print(u[i]) #it will print all values pair.


#item methods...
v=u.items()
print(v)
print(type(v))


#items method used for looping ....
for i ,j in u.items():
    print(f"key is {i} and value is {j}")


#update method......
new_dict={'name':'shivani dubey','fav_movies':["bluesky","life of pi"],'fav_tunes':["fairy tale","hyy"]}
u.update(new_dict)      #if dict have same name of keys it will update them 
print(u)    


# add datas...
u['fav_movies']=["bluesky","life of pi"]
print(u)


#pop method....
popped=u.pop('fav_movies')
print(popped)
print(u)

#popitem method.....
popitem1=u.popitem()
print(popitem1)

#fromkeys method.....
d=dict.fromkeys(['name','age'],'unknown')   
print(d)
s=dict.fromkeys("abc",'unknown')
print(s)
h=dict.fromkeys(range(1,11),'unknown')
print(h)

#get method....
c={'name':'shivani','age':20}
print(c.get('names'))      #if given key does not match it will not throw error ,it will print none.

#more about get keys...
print(c.get('names','not found'))   #we can overrid on none or can print anything what we want.
#copy method....
c1=c.copy()
print(c1)

#clear method...
c.clear()
print(c)     #it will clear the dictionary.



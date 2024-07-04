"""1). why we use dictionaries?
 because of limitations of lists .lists are not enough to represent real data .
 
 2). what are dictionaries?
 
 dictionaries are unorderd collections of datas in key: value pair"""


# 1st methode to creat dictionaries....
user = {'name': 'shivani', 'age': 20, 'from': 'up'}
print(user, type(user))
# note:- there is no indexing because of unordered  collections of data, so we access data from dictionares like this->
print(user['name'], user['age'])

# 2nd methode to creat dictionaries....
user1 = dict(name='shivani', age=20, father_name='rakesh_dubey')
print(user1, type(user1))
print(user1['name'], user1['age'])


# which type of datas dictionaries can store?(ans->anythings(numbers ,lists,str,dictionaries,etc))
list = ["skyscrepers", "marvels"]
list1 = ["fairytail"]
d = {
    'name': 'shivani',
    'age': 20,
    'fav_movies': list,
    'fav_tunes':  list1,
    'info': user
}
print(d)

# dictionary inside dictionary....
u = {
    'g': {
        'name': 'shivani',
        'age': 20,
        'fav_movies': 'list',
        'fav_tunes':  'list1',
        'info': user
    },
    'h': {
        'name': 'shivani', 'age': 20, 'from': 'up'
    }
}
print(u)


#adding or updating .....

s={'name': 'shivi','age': 20,}
s['name']='shivani'
s['village']='fully'
print(s)

#items()method...
for i,j in s.items():
    print(s)

#keys()method
for i in s.keys():
    print(s)
#values()method
for i in s.values():
    print(s)
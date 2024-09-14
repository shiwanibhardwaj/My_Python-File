def maximum(name):
    m = [len(i) for i in name]
    return m


name = ['shivani', 'dubey', 'hyyyyyyyyyyyyyyy', 'fyy']
print(max(name, key=maximum))
print(max(name, key=lambda i: len(i)))  # by using lambda function..
print(min(name, key=maximum))


students1 = [
    {'name': 'harshita', 'score': 90, 'age': 20},
    {'name': 'shivani', 'score': 96, 'age': 20},
    {'name': 'shree', 'score': 91, 'age': 19}
]

students2 = {
    'harshita': {'score': 90, 'age': 20},
    'shivani': {'score': 96, 'age': 20},
    'shree': {'score': 91, 'age': 19}   
}

print(max(students2,key=lambda item:students2[item]['score']))  #output will be name according to maximum score.
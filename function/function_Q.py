def string(name, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [i[::-1].title() for i in name]
    else:
        return [i.title() for i in name]


name = ['shivani', 'dubey']
print(string(name))
print(string(name, reverse_str=True))

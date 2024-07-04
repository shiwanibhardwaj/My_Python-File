s={i  for i in range(1,11) if i%2==0}
print(type(s))
print(s)


names={'shi','vani','kumari'}
first={name[::-1] for name in names}
print(first)



names={'shi','vani','kumari'}
first={name[0] for name in names}
print(first)



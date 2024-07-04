# d={1:1,2:4,3:9}
s={f'square of{n}':n**2 for n in range(1,11)}
print(s)
for i,j in s.items():
    print(f"{i}:{j}")


h="shivani"
w={num:h.count(num)for num in h}
print(w)

f={i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(f)
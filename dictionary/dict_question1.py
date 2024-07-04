#word counter...
def word_counter(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
s=input("enter character:")
print(word_counter(s))
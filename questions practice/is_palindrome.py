def is_palindrome(word):
  reverse_word=word[::-1]
  if(word==reverse_word):
    return True
  else:
    return False
p=input("enter anything what u want: ")
print(is_palindrome(p))
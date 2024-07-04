user_info={}
name=input("enter the name: ")
age=int(input("enter the age: "))
fav_movie=(input("enter the fav_movie: : ")).split(",")
user_info['name']=name
user_info['age']=age
user_info['fav_movie']=list(fav_movie)
for i,j in user_info.items():
    print(f"{i}:{j}")
#sorted function...
name = ["shivani", "muskan", "priya"]
print(sorted(name))
name2= ("shivani", "muskan", "priya")
print(sorted(name))                #we can't sort a tuple because they are inmutable but using 
#                                  sorted function we can sort ,this function will sort and return the value in list.
name3= {"shivani", "muskan", "priya"}
print(sorted(name))




guitars=[
    {'model':'yamaha f310','price':8400},
    {'model':'faith naptune','price':89000},
    {'model':'toylor 814ce','price':10000}
]
print(sorted(guitars,key=lambda d:d['price']))
print(sorted(guitars,key=lambda d:d['price'],reverse=True))
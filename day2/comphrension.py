list=[2,3,4,5,6,7,8,9]
squared=[]
for num in list:
   squared.append( num**2)
   print(squared)

#
squared=[num**2 for num in list]
print(squared)


#dict
dict={}
for i in range (10):
    if i%2==0:
        dict[i]=i*i
        print(dict)
#

dict={i:i*i for i in range (10) if i%2==0}
print(dict)

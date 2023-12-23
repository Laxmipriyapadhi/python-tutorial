#nestedlist
list=[10,34,56,[6.7,8.7,98],23,45,56]
print(list[3][0:3])
print(list[:5])

#nested dictionary
student_data={
    "pinky":{"roll_no":20,"age":23,"course":"python"},
    "chinky":{"roll_no":22,"age":24,"course":"java"},
    }
print(student_data["pinky"])
student_data["chinky"] ["year"]=2023
print(student_data["chinky"])

#nested tuple
t=(10,20,3.0,(34,56,'erfhgv',8.9),'true','tgh',89)
print(t[3][:])
print(t[-5])
print(t[:6])      
             

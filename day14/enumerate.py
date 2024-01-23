names = ["pinky" , "chinky" , "guddy" , "sandhya"]
subjects = ["python" , "c++" , "java" , "php"]

marks = [ 80 , 90 , 97 , 60 ]
for i, t in enumerate(zip(names , subjects , marks)):
    print(i, t)

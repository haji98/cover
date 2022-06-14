def findOutAge(year):
    result = 2022 - year; 
    print(result); 


findOutAge(1998);

findOutAge(1967);
findOutAge(1953);
findOutAge(1995);

for x in range(1900,2000):
    print("people born in "+ str(x) + " are")
    findOutAge(x);
    print(" years old")
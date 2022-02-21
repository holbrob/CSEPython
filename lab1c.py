import math
#int1 = int(input("Please enter a positive integer: "))
#int2 =int1.length()
#int2 = math.gcd(555)
#print(int2)
#int1 =int1%int2

int1 = int(input("Please enter a positive integer: "))
print(len(str(int1)))
int1 =int(int1%math.pow(10,int(len(str(int1))-1)))
print("Without the first digit, that is equal to "+str(int1))

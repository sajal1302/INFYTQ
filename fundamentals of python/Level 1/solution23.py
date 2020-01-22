#PF-Prac-23
def divisible_by_sum(number):
    number = str(number)
    a=0
    for i in range(0,len(number)):
        a=a+int(number[i])
        
    if int(number)%a==0:
        return True
    else :
        return False
        
    #start writing your code here

    
number=42
print(divisible_by_sum(number))
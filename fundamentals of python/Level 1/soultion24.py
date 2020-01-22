#PF-Prac-24
def find_gcd(num1,num2):
    l=0
    if num1>num2:
        a=num1
    else :
        a=num2
        
    for i in range (1,a+1):  
        if num1 %i==0 and num2 %i==0 and i>l:
            l=i
    return l
                
                
        
            
    #start writing your code here
    

num1=45
num2=9
print(find_gcd(num1,num2))
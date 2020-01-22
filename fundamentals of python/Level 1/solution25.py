#PF-Prac-25
def list_of_count(word_list):
    l=[]
    
    for i in word_list:
        c=0
        for j in i[0:]:
            c=c+1
        l.append(c)
        
        
    #start writing your code here
    
    return l

word_list=["COme","here"]
print(list_of_count(word_list))
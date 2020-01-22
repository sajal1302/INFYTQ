#PF-Prac-40
def index_of_max_unique(num_list):
    l=[]
    for i in num_list:
        s=set(i)
        l.append(len(s))
        index=l.index(max(l))
            
    #start writing your code here
    return index

num_list=[[1, 3, 3], [12, 4, 12, 7, 4, 4], [41, 2, 4, 7, 1, 12], [1, 2, 3, 4, 5, 6]]
num_list1=[[4, 5], [12], [3,8]] 
print("Number list:",num_list)
output=index_of_max_unique(num_list)
print("The index of sub list containing maximum unique elements is:",output)
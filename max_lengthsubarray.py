#PF-Prac-40
def index_of_max_unique(num_list):
    #start writing your code here
    index =0
    for i in range(len(num_list)):
        found =0
        for j in range(len(num_list[i])):
            try:
                if num_list[j] == num_list[j+1]:
                    found=1
                    break
            except:
                flag=1
        if found == 0:
            index = max(index,len(num_list[i]))
            
    return index

num_list=[[1, 3, 3], [12, 4, 12, 7, 4, 4], [41, 2, 4, 7, 1, 12], [1, 2, 3, 4, 5, 6]]
num_list1=[[4, 5], [12], [3,8]] 
#print("Number list:",num_list)
output=index_of_max_unique(num_list)
print("The index of sub list containing maximum unique elements is:",output)

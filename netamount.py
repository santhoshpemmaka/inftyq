#PF-Prac-8
def calculate_net_amount(trans_list):
    #start writing your code here
    count = 0
    count1 = 0
    for i in range(len(trans_list)):
        string,number =map(str,trans_list[i].split(':'))
        if string == "D":
            count=count+int(number)
        else:
            count1=count1+int(number)
    
    
    return count-count1

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))

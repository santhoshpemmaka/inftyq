#PF-Prac-9
def generate_dict(number):
	#start writing your code here
	result = {}
	for i in range(1,number+1):
	    result[i]=i*i
	
	return result

number=20
"""Output"
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""
print(generate_dict(number))

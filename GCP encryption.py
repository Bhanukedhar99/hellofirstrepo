
def Arrangements(N): 

	result = 1

	for i in range(1, N + 1): 

		# Here, i for factorial and 
		# (2*i-1) for series 
		result = result * i * (2 * i - 1) 

	return result 

# Driver code 
N = 4; 
print(Arrangements(N)); 


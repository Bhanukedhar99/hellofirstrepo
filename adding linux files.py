// C++ implementation of the approach 
#include <bits/stdc++.h> 
using namespace std; 

// Function to return the count 
// of required arrangements 
int countWays(int n) 
{ 

	// Create a vector 
	vector<int> a; 
	int i = 1; 

	// Store numbers from 1 to n 
	while (i <= n) 
		a.push_back(i++); 

	// To store the count of ways 
	int ways = 0; 

	// Generate all the permutations 
	// using next_permutation in STL 
	do { 
		// Initialize flag to true if first 
		// element is 1 else false 
		bool flag = (a[0] == 1); 

		// Checking if the current permutation 
		// satisfies the given conditions 
		for (int i = 1; i < n; i++) { 

			// If the current permutation is invalid 
			// then set the flag to false 
			if (abs(a[i] - a[i - 1]) > 2) 
				flag = 0; 
		} 

		// If valid arrangement 
		if (flag) 
			ways++; 

		// Generate the next permutation 
	} while (next_permutation(a.begin(), a.end())); 

	return ways; 
} 

// Driver code 
int main() 
{ 
	int n = 6; 

	cout << countWays(n); 

	return 0; 
} 

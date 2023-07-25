43. Multiply Strings



25 July 2023



Medium



C++:



// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)












class Solution {
public:
    string multiply(string num1, string num2) {
        int n = num1.length();  // variable to store the length of the first string
        int m = num2.length();  // variable to store the length of the second string

        if(num1 == "0" || num2 == "0"){  // if any of the strings is zero
            return "0";  // return zero
        }

        vector<int> result(n + m);  // vector to store the result
        for(int i = n - 1; i >= 0; i--){  // iterate through the first string
            for(int j = m - 1; j >= 0; j--){  // iterate through the second string
                int product = (num1[i] - '0') * (num2[j] - '0');  // variable to store the product
                int sum = product + result[i + j + 1];  // variable to store the sum
                result[i + j + 1] = sum % 10;  // update the result
                result[i + j] += sum / 10;  // update the result
            }
        }
        
        string res = "";  // variable to store the result
        for(int i = 0; i < n + m; i++){  // iterate through the result
            if(result[i] == 0 && res.length() == 0){  // if the current value is zero and the result is empty
                continue;  // continue
            }
            res += to_string(result[i]);  // update the result
        }
        return res;  // return the result
    }
};


2nd Method using  "Long Multiplication" algorithm






// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)


#include <string>

class Solution {
public:
    string multiply(string num1, string num2) {
        int n = num1.length();
        int m = num2.length();
        string ans(n + m, '0'); // Initialize ans with appropriate size and '0' characters

        for (int i = n - 1; i >= 0; i--) {
            int carry = 0;
            for (int j = m - 1; j >= 0; j--) {
                int temp = (num1[i] - '0') * (num2[j] - '0') + (ans[i + j + 1] - '0') + carry;
                ans[i + j + 1] = (temp % 10) + '0'; // Store the unit's digit in ans
                carry = temp / 10; // Carry over the tens digit to the next iteration
            }
            ans[i] += carry; // Add any remaining carry to the current position
        }

        // Trim leading zeroes
        int start_pos = ans.find_first_not_of('0');
        return (start_pos != string::npos) ? ans.substr(start_pos) : "0";
    }
};





Java:



Python:



Python3:



C:



C#



JavaScript:




Swift:


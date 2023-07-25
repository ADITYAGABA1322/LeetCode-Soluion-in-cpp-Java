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



// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)







class Solution {
    public String multiply(String num1, String num2) {
        int n = num1.length();  // variable to store the length of the first string
        int m = num2.length();  // variable to store the length of the second string

        if(num1.equals("0") || num2.equals("0")){  // if any of the strings is zero
            return "0";  // return zero
        }

        int[] result = new int[n + m];  // array to store the result
        for(int i = n - 1; i >= 0; i--){  // iterate through the first string
            for(int j = m - 1; j >= 0; j--){  // iterate through the second string
                int product = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');  // variable to store the product
                int sum = product + result[i + j + 1];  // variable to store the sum
                result[i + j + 1] = sum % 10;  // update the result
                result[i + j] += sum / 10;  // update the result
            }
        }
        
        StringBuilder res = new StringBuilder();  // variable to store the result
        for(int i = 0; i < n + m; i++){  // iterate through the result
            if(result[i] == 0 && res.length() == 0){  // if the current value is zero and the result is empty
                continue;  // continue
            }
            res.append(result[i]);  // update the result
        }
        return res.toString();  // return the result
    }
}






Python:

// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)






class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = len(num1)  # variable to store the length of the first string
        m = len(num2)  # variable to store the length of the second string

        if num1 == "0" or num2 == "0":  # if any of the strings is zero
            return "0"  # return zero

        result = [0] * (n + m)  # list to store the result
        for i in range(n - 1, -1, -1):  # iterate through the first string
            for j in range(m - 1, -1, -1):  # iterate through the second string
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))  # variable to store the product
                sum = product + result[i + j + 1]  # variable to store the sum
                result[i + j + 1] = sum % 10  # update the result
                result[i + j] += sum // 10  # update the result

        res = ""  # variable to store the result
        for i in range(n + m):  # iterate through the result
            if result[i] == 0 and len(res) == 0:  # if the current value is zero and the result is empty
                continue  # continue
            res += str(result[i])  # update the result
        return res  # return the result








Python3:



    


// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)







class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)  # variable to store the length of the first string
        m = len(num2)  # variable to store the length of the second string

        if num1 == "0" or num2 == "0":  # if any of the strings is zero
            return "0"  # return zero

        result = [0] * (n + m)  # list to store the result
        for i in range(n - 1, -1, -1):  # iterate through the first string
            for j in range(m - 1, -1, -1):  # iterate through the second string
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))  # variable to store the product
                sum = product + result[i + j + 1]  # variable to store the sum
                result[i + j + 1] = sum % 10  # update the result
                result[i + j] += sum // 10  # update the result

        res = ""  # variable to store the result
        for i in range(n + m):  # iterate through the result
            if result[i] == 0 and len(res) == 0:  # if the current value is zero and the result is empty
                continue  # continue
            res += str(result[i])  # update the result
        return res  # return the result







C:




// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)





char * multiply(char * num1, char * num2){
    int n = strlen(num1);  // variable to store the length of the first string
    int m = strlen(num2);  // variable to store the length of the second string

    if(strcmp(num1, "0") == 0 || strcmp(num2, "0") == 0){  // if any of the strings is zero
        return "0";  // return zero
    }

    int * result = (int *)malloc(sizeof(int) * (n + m));  // array to store the result
    for(int i = n - 1; i >= 0; i--){  // iterate through the first string
        for(int j = m - 1; j >= 0; j--){  // iterate through the second string
            int product = (num1[i] - '0') * (num2[j] - '0');  // variable to store the product
            int sum = product + result[i + j + 1];  // variable to store the sum
            result[i + j + 1] = sum % 10;  // update the result
            result[i + j] += sum / 10;  // update the result
        }
    }
    
    char * res = (char *)malloc(sizeof(char) * (n + m + 1));  // variable to store the result
    int index = 0;  // variable to store the index
    for(int i = 0; i < n + m; i++){  // iterate through the result
        if(result[i] == 0 && index == 0){  // if the current value is zero and the result is empty
            continue;  // continue
        }
        res[index++] = result[i] + '0';  // update the result
    }
    res[index] = '\0';  // update the result
    return res;  // return the result
}



C#





// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)







public class Solution {
    public string Multiply(string num1, string num2) {
        int n = num1.Length;  // variable to store the length of the first string
        int m = num2.Length;  // variable to store the length of the second string

        if(num1 == "0" || num2 == "0"){  // if any of the strings is zero
            return "0";  // return zero
        }

        int[] result = new int[n + m];  // array to store the result
        for(int i = n - 1; i >= 0; i--){  // iterate through the first string
            for(int j = m - 1; j >= 0; j--){  // iterate through the second string
                int product = (num1[i] - '0') * (num2[j] - '0');  // variable to store the product
                int sum = product + result[i + j + 1];  // variable to store the sum
                result[i + j + 1] = sum % 10;  // update the result
                result[i + j] += sum / 10;  // update the result
            }
        }
        
        StringBuilder res = new StringBuilder();  // variable to store the result
        for(int i = 0; i < n + m; i++){  // iterate through the result
            if(result[i] == 0 && res.Length == 0){  // if the current value is zero and the result is empty
                continue;  // continue
            }
            res.Append(result[i]);  // update the result
        }
        return res.ToString();  // return the result
    }
}




JavaScript:



// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)




/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */


var multiply = function(num1, num2) {
    let n = num1.length;  // variable to store the length of the first string
    let m = num2.length;  // variable to store the length of the second string

    if(num1 == "0" || num2 == "0"){  // if any of the strings is zero
        return "0";  // return zero
    }

    let result = new Array(n + m).fill(0);  // array to store the result
    for(let i = n - 1; i >= 0; i--){  // iterate through the first string
        for(let j = m - 1; j >= 0; j--){  // iterate through the second string
            let product = (num1[i] - '0') * (num2[j] - '0');  // variable to store the product
            let sum = product + result[i + j + 1];  // variable to store the sum
            result[i + j + 1] = sum % 10;  // update the result
            result[i + j] += Math.floor(sum / 10);  // update the result
        }
    }
    
    let res = "";  // variable to store the result
    for(let i = 0; i < n + m; i++){  // iterate through the result
        if(result[i] == 0 && res.length == 0){  // if the current value is zero and the result is empty
            continue;  // continue
        }
        res += result[i];  // update the result
    }
    return res;  // return the result
};




2nd Method 



/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
     return (BigInt(num1)*BigInt(num2)).toString();

};





Swift:



// Time Complexity : O(n * m) where n is the length of the first string and m is the length of the second string and space complexity is O(n + m)







class Solution {
    func multiply(_ num1: String, _ num2: String) -> String {
        let n = num1.count  // variable to store the length of the first string
        let m = num2.count  // variable to store the length of the second string

        if num1 == "0" || num2 == "0" {  // if any of the strings is zero
            return "0"  // return zero
        }

        var result = Array(repeating: 0, count: n + m)  // array to store the result
        for i in stride(from: n - 1, through: 0, by: -1) {  // iterate through the first string
            for j in stride(from: m - 1, through: 0, by: -1) {  // iterate through the second string
                let index1 = num1.index(num1.startIndex, offsetBy: i)
                let index2 = num2.index(num2.startIndex, offsetBy: j)
                
                let digit1 = Int(String(num1[index1]))!
                let digit2 = Int(String(num2[index2]))!
                
                let product = digit1 * digit2  // variable to store the product
                let sum = product + result[i + j + 1]  // variable to store the sum
                result[i + j + 1] = sum % 10  // update the result
                result[i + j] += sum / 10  // update the result
            }
        }
        
        var res = ""  // variable to store the result
        for i in 0..<n + m {  // iterate through the result
            if result[i] == 0 && res.isEmpty {  // if the current value is zero and the result is empty
                continue  // continue
            }
            res += String(result[i])  // update the result
        }
        return res  // return the result
    }
}








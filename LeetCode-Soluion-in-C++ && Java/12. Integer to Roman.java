12. Integer to Roman

  

  
11 July 2023
  

  

Medium

  
  

C++:




// Time Complexity : O(n) where n is the length of the string and space complexity is O(1)





class Solution {
public:
    string intToRoman(int num) {
        string result = "";  // variable to store the result
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10 , 9, 5, 4, 1};  // vector to store the values
        vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X" , "IX", "V", "IV", "I"};  // vector to store the symbols
        for(int i = 0; i < values.size(); i++){  // iterate through the vectors
            while(num >= values[i]){  // iterate until the number is greater than or equal to the current value
                num -= values[i];  // update the number
                result += symbols[i];  // update the result
            }
        }
        return result;  // return the result
    }
};




Java:





// Time Complexity : O(n) where n is the length of the string and space complexity is O(1)







class Solution {
    public String intToRoman(int num) {
        String result = "";  // variable to store the result
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10 , 9, 5, 4, 1};  // array to store the values
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X" , "IX", "V", "IV", "I"};  // array to store the symbols
        for(int i = 0; i < values.length; i++){  // iterate through the arrays
            while(num >= values[i]){  // iterate until the number is greater than or equal to the current value
                num -= values[i];  // update the number
                result += symbols[i];  // update the result
            }
        }
        return result;  // return the result
    }
}





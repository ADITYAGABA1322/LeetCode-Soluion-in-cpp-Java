151. Reverse Words in a String

 

24 Feb 2023

 

    
Medium



C++:

// Time Complexity : O(n) where n is the length of the string and space complexity is O(n)


class Solution {
public:
    string reverseWords(string s) {
        string result = "";  // variable to store the result
        int i = s.length() - 1;  // variable to store the index
        while(i >= 0){  // iterate until the index is greater than or equal to 0
            while(i >= 0 && s[i] == ' '){  // iterate until the index is greater than or equal to 0 and the character at the index is a space
                i--;  // decrement the index
            }
            if(i < 0){  // if the index is less than 0
                break;  // break
          }
            if(result.length() != 0){  // if the length of the result is not equal to 0
                result += " ";  // add a space to the result
            }
            string word = "";  // variable to store the word
            while(i >= 0 && s[i] != ' '){  // iterate until the index is greater than or equal to 0 and the character at the index is not a space
                word = s[i] + word;  // add the character at the index to the word
                i--;  // decrement the index
            }
            result += word;  // add the word to the result
        }
        return result;  // return the result
    }
};





3 Methods


Java:


// Time Complexity : O(n) where n is the length of the string and space complexity is O(n)


class Solution {
    public String reverseWords(String s) {
        String result = "";  // variable to store the result
        int i = s.length() - 1;  // variable to store the index
        while(i >= 0){  // iterate until the index is greater than or equal to 0
            while(i >= 0 && s.charAt(i) == ' '){  // iterate until the index is greater than or equal to 0 and the character at the index is a space
                i--;  // decrement the index
            }
            if(i < 0){  // if the index is less than 0
                break;  // break
            }
            if(result.length() != 0){  // if the length of the result is not equal to 0
                result += " ";  // add a space to the result
            }
            String word = "";  // variable to store the word
            while(i >= 0 && s.charAt(i) != ' '){  // iterate until the index is greater than or equal to 0 and the character at the index is not a space
                word = s.charAt(i) + word;  // add the character at the index to the word
                i--;  // decrement the index
            }
            result += word;  // add the word to the result
        }
        return result;  // return the result
    }
}


2nd Method:


// Time Complexity : O(n) where n is the length of the string and space complexity is O(n)


class Solution {
    public String reverseWords(String s) {
        String result = "";  // variable to store the result
        String[] words = s.split(" ");  // split the string by spaces
        for(int i = words.length - 1; i >= 0; i--){  // iterate from the last index to the first index
            if(words[i].length() != 0){  // if the length of the word at the index is not equal to 0
                if(result.length() != 0){  // if the length of the result is not equal to 0
                    result += " ";  // add a space to the result
                }
                result += words[i];  // add the word at the index to the result
            }
        }
        return result;  // return the result
    }
}


3rd Method:


// Time Complexity : O(n) where n is the length of the string and space complexity is O(n)



class Solution {
    public String reverseWords(String s) {
        String str[]=s.split("\\s+");
        String res="";
        for(int i=str.length-1;i>=0;i--){
            res+= str[i]+" ";
        }
        return res.substring(0,res.length()-1).trim();

    }
}




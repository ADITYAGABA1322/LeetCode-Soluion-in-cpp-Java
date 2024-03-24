10. Regular Expression Matching



   

7 March 2023

   
   

   
Hard
    



C++:


// Time Complexity : O(m*n) where m is the length of the string and n is the length of the pattern and space complexity is O(m*n)



class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();  // variable to store the length of the string
        int n = p.size();  // variable to store the length of the pattern
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));  // 2d vector to store the dp values
        dp[0][0] = true;  // update the dp value at the 0th index of the string and the 0th index of the pattern to true
        for(int i = 1; i <= n; i++){  // iterate through the pattern
            if(p[i - 1] == '*'){  // if the current character is equal to *
                dp[0][i] = dp[0][i - 2];  // update the dp value at the 0th index of the string and the current index of the pattern to the dp value at the 0th index of the string and the current index - 2 of the pattern
            }
        }
        for(int i = 1; i <= m; i++){  // iterate through the string
            for(int j = 1; j <= n; j++){  // iterate through the pattern
                if(p[j - 1] == '.' || p[j - 1] == s[i - 1]){  // if the current character of the pattern is equal to . or the current character of the pattern is equal to the current character of the string
                    dp[i][j] = dp[i - 1][j - 1];  // update the dp value at the current index of the string and the current index of the pattern to the dp value at the current index - 1 of the string and the current index - 1 of the pattern
                }
                else if(p[j - 1] == '*'){  // if the current character of the pattern is equal to *
                    dp[i][j] = dp[i][j - 2];  // update the dp value at the current index of the string and the current index of the pattern to the dp value at the current index of the string and the current index - 2 of the pattern
                    if(p[j - 2] == '.' || p[j - 2] == s[i - 1]){  // if the current character - 2 of the pattern is equal to . or the current character - 2 of the pattern is equal to the current character of the string
                        dp[i][j] = dp[i][j] || dp[i - 1][j];  // update the dp value at the current index of the string and the current index of the pattern to the dp value at the current index of the string and the current index of the pattern or the dp value at the current index - 1 of the string and the current index of the pattern
                    }
                }
            }
        }
        return dp[m][n];  // return the dp value at the last index of the string and the last index of the pattern
    }
};
        

2nd Method 

class Solution {
public:
    bool isMatch(string s, string p) {
         
        //tabulation with single vector 
        int m = s.size(), n = p.size();
        vector<bool> cur(n + 1, false);
        for (int i = 0; i <= m; i++) {
            bool pre = cur[0];
            cur[0] = !i;
            for (int j = 1; j <= n; j++) {
                bool temp = cur[j];
                if (p[j - 1] == '*') {
                    cur[j] = cur[j - 2] || (i && cur[j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
                } else {
                    cur[j] = i && pre && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
                }
                pre = temp;
            }
        }
        return cur[n];
    }
};



Java:



// Time Complexity : O(m*n) where m is the length of the string and n is the length of the pattern and space complexity is O(m*n)



class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();  // variable to store the length of the string
        int n = p.length();  // variable to store the length of the pattern
        boolean[][] dp = new boolean[m + 1][n + 1];  // 2d array to store the dp values
        dp[0][0] = true;  // update the dp value at the 0th index of the string and the 0th index of the pattern to true
        for(int i = 1; i <= n; i++){  // iterate through the pattern
            if(p.charAt(i - 1) == '*'){  // if the current character is equal to *
                dp[0][i] = dp[0][i - 2];  // update the dp value at the 0th index of the string and the current index of the pattern to the dp value at the 0th index of the string and the current index - 2 of the pattern
            }
        }
        for(int i = 1; i <= m; i++){  // iterate through the string
            for(int j = 1; j <= n; j++){  // iterate through the pattern
                if(p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)){  // if the current character of the pattern is equal to . or the current character of the pattern is equal to the current character of the string
                    dp[i][j] = dp[i - 1][j - 1];  // update the dp value at the current index of the string and the current index of the pattern to the dp value at the current index - 1 of the string and the current index - 1 of the pattern
                }
                else if(p.charAt(j - 1) == '*'){  // if the current character of the pattern is equal to *
                    dp[i][j] = dp[i][j - 2];  // update the dp value at the current index of the string and the current index of the pattern to the dp value at the current index of the string and the current index - 2 of the pattern
                    if(p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)){  // if the current character - 2 of the pattern is equal to . or the current character - 2 of the pattern is equal to the current character of the string
                        dp[i][j] = dp[i][j] || dp[i - 1][j];  // update the dp value at the current index of the string and the current index of the pattern to the dp value at the current index of the string and the current index of the pattern or the dp value at the current index - 1 of the string and the current index of the pattern
                    }
                }
            }
        }
        return dp[m][n];  // return the dp value at the last index of the string and the last index of the pattern
    }
}



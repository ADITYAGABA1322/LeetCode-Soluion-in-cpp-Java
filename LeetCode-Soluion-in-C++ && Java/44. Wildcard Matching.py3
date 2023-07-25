44. Wildcard Matching


9 March 2023



Hard



C++:


// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)



class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();  // variable to store the length of the string
        int n = p.length();  // variable to store the length of the pattern
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));  // 2d vector to store the dp values
        dp[0][0] = true;  // update the dp value
        for(int i = 1; i <= n; i++){  // iterate through the pattern
            if(p[i - 1] == '*'){  // if the current character is '*'
                dp[0][i] = dp[0][i - 1];  // update the dp value
            }
        }
        for(int i = 1; i <= m; i++){  // iterate through the string
            for(int j = 1; j <= n; j++){  // iterate through the pattern
                if(p[j - 1] == '*'){  // if the current character is '*'
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];  // update the dp value
                }
                else if(p[j - 1] == '?' || s[i - 1] == p[j - 1]){  // if the current character is '?' or the current character of the string is equal to the current character of the pattern
                    dp[i][j] = dp[i - 1][j - 1];  // update the dp value
                }
            }
        }
        return dp[m][n];  // return the dp value
    }
};


Java:



// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)





class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();  // variable to store the length of the string
        int n = p.length();  // variable to store the length of the pattern
        boolean[][] dp = new boolean[m + 1][n + 1];  // 2d array to store the dp values
        dp[0][0] = true;  // update the dp value
        for(int i = 1; i <= n; i++){  // iterate through the pattern
            if(p.charAt(i - 1) == '*'){  // if the current character is '*'
                dp[0][i] = dp[0][i - 1];  // update the dp value
            }
        }
        for(int i = 1; i <= m; i++){  // iterate through the string
            for(int j = 1; j <= n; j++){  // iterate through the pattern
                if(p.charAt(j - 1) == '*'){  // if the current character is '*'
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];  // update the dp value
                }
                else if(p.charAt(j - 1) == '?' || s.charAt(i - 1) == p.charAt(j - 1)){  // if the current character is '?' or the current character of the string is equal to the current character of the pattern
                    dp[i][j] = dp[i - 1][j - 1];  // update the dp value
                }
            }
        }
        return dp[m][n];  // return the dp value
    }
}


Python:




Python3:




C:




C#:





JavaScript:




Swift:

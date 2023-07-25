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



// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)







class Solution(object):
    def isMatch(self, s, p):
        m = len(s)  # variable to store the length of the string
        n = len(p)  # variable to store the length of the pattern
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]  # 2d array to store the dp values
        dp[0][0] = True  # update the dp value
        for i in range(1, n + 1):  # iterate through the pattern
            if p[i - 1] == '*':  # if the current character is '*'
                dp[0][i] = dp[0][i - 1]  # update the dp value
        for i in range(1, m + 1):  # iterate through the string
            for j in range(1, n + 1):  # iterate through the pattern
                if p[j - 1] == '*':  # if the current character is '*'
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # update the dp value
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:  # if the current character is '?' or the current character of the string is equal to the current character of the pattern
                    dp[i][j] = dp[i - 1][j - 1]  # update the dp value
        return dp[m][n]  # return the dp value




Python3:



// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)







class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)  # variable to store the length of the string
        n = len(p)  # variable to store the length of the pattern
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]  # 2d array to store the dp values
        dp[0][0] = True  # update the dp value
        for i in range(1, n + 1):  # iterate through the pattern
            if p[i - 1] == '*':  # if the current character is '*'
                dp[0][i] = dp[0][i - 1]  # update the dp value
        for i in range(1, m + 1):  # iterate through the string
            for j in range(1, n + 1):  # iterate through the pattern
                if p[j - 1] == '*':  # if the current character is '*'
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # update the dp value
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:  # if the current character is '?' or the current character of the string is equal to the current character of the pattern
                    dp[i][j] = dp[i - 1][j - 1]  # update the dp value
        return dp[m][n]  # return the dp value






C:


// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)










bool isMatch(char * s, char * p){
    int m = strlen(s);  // variable to store the length of the string
    int n = strlen(p);  // variable to store the length of the pattern
    bool dp[m + 1][n + 1];  // 2d array to store the dp values
    memset(dp, false, sizeof(dp));  // update the dp value
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





C#:




// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)










public class Solution {
    public bool IsMatch(string s, string p) {
        int m = s.Length;  // variable to store the length of the string
        int n = p.Length;  // variable to store the length of the pattern
        bool[,] dp = new bool[m + 1, n + 1];  // 2d array to store the dp values
        dp[0, 0] = true;  // update the dp value
        for(int i = 1; i <= n; i++){  // iterate through the pattern
            if(p[i - 1] == '*'){  // if the current character is '*'
                dp[0, i] = dp[0, i - 1];  // update the dp value
            }
        }
        for(int i = 1; i <= m; i++){  // iterate through the string
            for(int j = 1; j <= n; j++){  // iterate through the pattern
                if(p[j - 1] == '*'){  // if the current character is '*'
                    dp[i, j] = dp[i - 1, j] || dp[i, j - 1];  // update the dp value
                }
                else if(p[j - 1] == '?' || s[i - 1] == p[j - 1]){  // if the current character is '?' or the current character of the string is equal to the current character of the pattern
                    dp[i, j] = dp[i - 1, j - 1];  // update the dp value
                }
            }
        }
        return dp[m, n];  // return the dp value
    }
}









JavaScript:






// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)











/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */



var isMatch = function(s, p) {
    let m = s.length;  // variable to store the length of the string
    let n = p.length;  // variable to store the length of the pattern
    let dp = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(false));  // 2d array to store the dp values
    dp[0][0] = true;  // update the dp value
    for(let i = 1; i <= n; i++){  // iterate through the pattern
        if(p[i - 1] == '*'){  // if the current character is '*'
            dp[0][i] = dp[0][i - 1];  // update the dp value
        }
    }
    for(let i = 1; i <= m; i++){  // iterate through the string
        for(let j = 1; j <= n; j++){  // iterate through the pattern
            if(p[j - 1] == '*'){  // if the current character is '*'
                dp[i][j] = dp[i - 1][j] || dp[i][j - 1];  // update the dp value
            }
            else if(p[j - 1] == '?' || s[i - 1] == p[j - 1]){  // if the current character is '?' or the current character of the string is equal to the current character of the pattern
                dp[i][j] = dp[i - 1][j - 1];  // update the dp value
            }
        }
    }
    return dp[m][n];  // return the dp value
};








Swift:







// Time Complexity : O(m * n) where m is the length of the string and n is the length of the pattern and space complexity is O(m * n)










class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        var memo = [[Bool?]](repeating: [Bool?](repeating: nil, count: p.count + 1), count: s.count + 1)
        return isMatchHelper(Array(s), Array(p), 0, 0, &memo)
    }
    
    func isMatchHelper(_ s: [Character], _ p: [Character], _ i: Int, _ j: Int, _ memo: inout [[Bool?]]) -> Bool {
        if let cachedResult = memo[i][j] {
            return cachedResult
        }
        
        if j == p.count {
            memo[i][j] = i == s.count
            return memo[i][j]!
        }
        
        var result = false
        if i < s.count {
            if p[j] == s[i] || p[j] == "?" {
                result = isMatchHelper(s, p, i + 1, j + 1, &memo)
            } else if p[j] == "*" {
                result = isMatchHelper(s, p, i + 1, j, &memo) || isMatchHelper(s, p, i, j + 1, &memo)
            }
        } else if p[j] == "*" {
            result = isMatchHelper(s, p, i, j + 1, &memo)
        }
        
        memo[i][j] = result
        return result
    }
}



2nd Method 



class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
    var s = Array(s)
        var p = Array(p)
        var dp = [[Bool]](repeating: [Bool](repeating: false, count: s.count+1), count: p.count+1)

        for i in 0...p.count{
            for j in 0...s.count {
                if i == 0 && j == 0 {
                    dp[i][j] = true
                } else if i == 0 {
                    dp[i][j] = false
                } else if j == 0 {
                    if p[i-1] == "*" {
                        dp[i][j] = dp[i-1][j]
                    } else {
                        dp[i][j] = false
                    }
                } else {
                    if p[i-1] == "*" {
                        dp[i][j] = dp[i][j-1] || dp[i-1][j-1] || dp[i-1][j]
                    } else if p[i-1] == s[j-1] || p[i-1] == "?" {
                        dp[i][j] = dp[i-1][j-1] 
                    } else {
                        dp[i][j] = false
                    }
                }
            }
        }
        return dp[p.count][s.count]
    }
}
 





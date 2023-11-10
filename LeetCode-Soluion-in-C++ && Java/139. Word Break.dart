139. Word Break


    
    
7 August 2023
    
    
    

Medium



C++:


// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size(); // variable to store the size of the string s
        vector<bool> dp(n+1, false); // vector to store the result
        dp[0] = true; // initialize the dp[0] to true
        for(int i=1; i<=n; i++){ // loop for i
            for(int j=0; j<i; j++){ // loop for j
                if(dp[j] && find(wordDict.begin(), wordDict.end(), s.substr(j, i-j)) != wordDict.end()){ // if dp[j] is true and the word is present in the dictionary
                    dp[i] = true; // update the dp[i]
                    break; // break
                }
            }
        }
        return dp[n]; // return the dp[n]
    }
};

2nd Method using BFS

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end()); // unordered_set to store the dictionary
        queue<int> q; // queue to store the index
        vector<bool> visited(s.size(), false); // vector to store the visited
        q.push(0); // push the index 0
        while(!q.empty()){ // while queue is not empty
            int start = q.front(); // variable to store the start
            q.pop(); // pop the element from the queue
            if(!visited[start]){ // if start is not visited
                for(int end=start+1; end<=s.size(); end++){ // loop for end
                    if(dict.find(s.substr(start, end-start)) != dict.end()){ // if the word is present in the dictionary
                        q.push(end); // push the end
                        if(end == s.size()){ // if end is equal to the size of the string s
                            return true; // return true
                        }
                    }
                }
                visited[start] = true; // update the visited
            }
        }
        return false; // return false
    }
};  



Java:

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length(); // variable to store the size of the string s
        boolean[] dp = new boolean[n+1]; // vector to store the result
        dp[0] = true; // initialize the dp[0] to true
        for(int i=1; i<=n; i++){ // loop for i
            for(int j=0; j<i; j++){ // loop for j
                if(dp[j] && wordDict.contains(s.substring(j, i))){ // if dp[j] is true and the word is present in the dictionary
                    dp[i] = true; // update the dp[i]
                    break; // break
                }
            }
        }
        return dp[n]; // return the dp[n]
    }
}

2nd Method using BFS

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict); // unordered_set to store the dictionary
        Queue<Integer> q = new LinkedList<>(); // queue to store the index
        boolean[] visited = new boolean[s.length()]; // vector to store the visited
        q.add(0); // push the index 0
        while(!q.isEmpty()){ // while queue is not empty
            int start = q.poll(); // variable to store the start
            if(!visited[start]){ // if start is not visited
                for(int end=start+1; end<=s.length(); end++){ // loop for end
                    if(dict.contains(s.substring(start, end))){ // if the word is present in the dictionary
                        q.add(end); // push the end
                        if(end == s.length()){ // if end is equal to the size of the string s
                            return true; // return true
                        }
                    }
                }
                visited[start] = true; // update the visited
            }
        }
        return false; // return false
    }
}



Python:


// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """ 
        n = len(s)  # variable to store the size of the string s
        dp = [False]*(n+1)  # vector to store the result
        dp[0] = True  # initialize the dp[0] to true
        for i in range(1, n+1):  # loop for i
            for j in range(i):  # loop for j
                if dp[j] and s[j:i] in wordDict:  # if dp[j] is true and the word is present in the dictionary
                    dp[i] = True  # update the dp[i]
                    break  # break
        return dp[n]  # return the dp[n]



Python3:


// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str) -> bool: // add the missing bracket after str
        n = len(s)  # variable to store the size of the string s
        dp = [False]*(n+1)  # vector to store the result
        dp[0] = True  # initialize the dp[0] to true
        for i in range(1, n+1):  # loop for i
            for j in range(i):  # loop for j
                if dp[j] and s[j:i] in wordDict:  # if dp[j] is true and the word is present in the dictionary
                    dp[i] = True  # update the dp[i]
                    break  # break
        return dp[n]  # return the dp[n]


C:

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

bool wordBreak(char * s, char ** wordDict, int wordDictSize){
    int n = strlen(s);  // variable to store the size of the string s
    bool dp[n+1];  // vector to store the result
    memset(dp, false, sizeof(dp));  // initialize the dp
    dp[0] = true;  // initialize the dp[0] to true
    for(int i=1; i<=n; i++){  // loop for i
        for(int j=0; j<i; j++){  // loop for j
            if(dp[j] && strstr(s+j, wordDict[i]) != NULL){  // if dp[j] is true and the word is present in the dictionary
                dp[i] = true;  // update the dp[i]
                break;  // break
            }
        }
    }
    return dp[n];  // return the dp[n]
}



C#:

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        int n = s.Length;  // variable to store the size of the string s
        bool[] dp = new bool[n+1];  // vector to store the result
        dp[0] = true;  // initialize the dp[0] to true
        for(int i=1; i<=n; i++){  // loop for i
            for(int j=0; j<i; j++){  // loop for j
                if(dp[j] && wordDict.Contains(s.Substring(j, i-j))){  // if dp[j] is true and the word is present in the dictionary
                    dp[i] = true;  // update the dp[i]
                    break;  // break
                }
            }
        }
        return dp[n];  // return the dp[n]
    }
}



JavaScript:

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

var wordBreak = function(s, wordDict) {
    let n = s.length;  // variable to store the size of the string s
    let dp = new Array(n+1).fill(false);  // vector to store the result
    dp[0] = true;  // initialize the dp[0] to true
    for(let i=1; i<=n; i++){  // loop for i
        for(let j=0; j<i; j++){  // loop for j
            if(dp[j] && wordDict.includes(s.substring(j, i))){  // if dp[j] is true and the word is present in the dictionary
                dp[i] = true;  // update the dp[i]
                break;  // break
            }
        }
    }
    return dp[n];  // return the dp[n]
};




Swift:

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        let n = s.count  // variable to store the size of the string s
        var dp = [Bool](repeating: false, count: n+1)  // vector to store the result
        dp[0] = true  // initialize the dp[0] to true
        for i in 1...n{  // loop for i
            for j in 0..<i{  // loop for j
                if dp[j] && wordDict.contains(String(s[s.index(s.startIndex, offsetBy: j)..<s.index(s.startIndex, offsetBy: i)])){  // if dp[j] is true and the word is present in the dictionary
                    dp[i] = true  // update the dp[i]
                    break  // break
                }
            }
        }
        return dp[n]  // return the dp[n]
    }
}



Dart:

// Time Complexity : O(n^2) where n is the size of the string s and space complexity is O(n)

bool wordBreak(String s, List<String> wordDict) {
    int n = s.length;  // variable to store the size of the string s
    List<bool> dp = new List<bool>.filled(n+1, false);  // vector to store the result
    dp[0] = true;  // initialize the dp[0] to true
    for(int i=1; i<=n; i++){  // loop for i
        for(int j=0; j<i; j++){  // loop for j
            if(dp[j] && wordDict.contains(s.substring(j, i))){  // if dp[j] is true and the word is present in the dictionary
                dp[i] = true;  // update the dp[i]
                break;  // break
            }
        }
    }
    return dp[n];  // return the dp[n]
}



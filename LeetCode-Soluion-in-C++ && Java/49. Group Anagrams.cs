49. Group Anagrams




28 July 2023
  

  

Medium




C++:

// Time Complexity : O(n * klogk) where n is the length of the vector strs and k is the length of the string in the vector strs and space complexity is O(n)

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;  // vector to store the result
        unordered_map<string, vector<string>> map;  // map to store the temporary result
        for(string s : strs){  // iterate through the vector strs
            string temp = s;  // variable to store the temporary result
            sort(temp.begin(), temp.end());  // sort the string
            map[temp].push_back(s);  // push the string into the map
        }
        for(auto m : map){  // iterate through the map
            res.push_back(m.second);  // push the temporary result into the result
        }
        return res;  // return the result
    }
};




Java:


Python:


Python3:



C:


C#:



JavaScript:



Swift:

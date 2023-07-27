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

// Time Complexity : O(n * klogk) where n is the length of the vector strs and k is the length of the string in the vector strs and space complexity is O(n)

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();  // list to store the result
        Map<String, List<String>> map = new HashMap<>();  // map to store the temporary result
        for(String s : strs){  // iterate through the vector strs
            char[] temp = s.toCharArray();  // variable to store the temporary result
            Arrays.sort(temp);  // sort the string
            String sorted = new String(temp);  // variable to store the temporary result
            if(!map.containsKey(sorted)){  // if the map does not contain the key
                map.put(sorted, new ArrayList<>());  // push the temporary result into the map
            }
            map.get(sorted).add(s);  // push the temporary result into the map
        }
        for(Map.Entry<String, List<String>> m : map.entrySet()){  // iterate through the map
            res.add(m.getValue());  // push the temporary result into the result
        }
        return res;  // return the result
    }
}

2nd Method

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<Integer>> res = new ArrayList<>();
        Map<String , List<String>> mp = new HashMap<>();
        for(String s : strs){
            char[] temp = s.toCharArray();
            Arrays.sort(temp);
            String sorted = new String(temp);
            if(!mp.containsKey(sorted)) mp.put(sorted , new ArrayList<>());
            mp.get(sorted).add(s);
        }
        return new ArrayList<>(mp.values());
    }
}




Python:


Python3:



C:


C#:



JavaScript:



Swift:

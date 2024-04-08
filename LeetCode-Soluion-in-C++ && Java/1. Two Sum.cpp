# LeetCode-Soluion-in-Cpp-Java





1.Two Sum





9 Feb 2023
    


    
Easy



4 Approaches



C++:


// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(n)

1st Method

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;  // unordered map to store the number and the index of the number
        for(int i=0; i<nums.size(); i++){  // for each element in the vector nums
            if(m.find(target - nums[i]) != m.end()){  // if the target - nums[i] is present in the unordered map
                return {m[target - nums[i]], i};  // return the index of the target - nums[i] and the index of the current element
            }
            m[nums[i]] = i;  // update the index of the current element
        }
        return {};  // return empty vector
    }
};



2nd Method

class Solution{
    public:
    vector<int> twoSum(vector<int> arr , int target){
        vector<int> v;
        for(int i=0;i<arr.size();i++){
            for(int j=i+1;j<arr.size();j++){
                if(arr[i]+arr[j]==target){
                    v.push_back(i);
                    v.push_back(j);
                }
            }
            
        }
        return v;
    }
};





3rd Method

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        for(int i=0;i<nums.size();i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    v.push_back(i);
                    v.push_back(j);
                }
            }
        }
        return v;
        
    }
};





4th Method

// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(n)

class Solution {

public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;  // unordered map to store the number and the index of the number
        for(int i=0; i<nums.size(); i++){  // for each element in the vector nums
            if(m.find(nums[i]) != m.end()){  // if the nums[i] is present in the unordered map
                return {m[nums[i]], i};  // return the index of the nums[i] and the index of the current element
            }
            m[target - nums[i]] = i;  // update the index of the target - nums[i]
        }
        return {};  // return empty vector
    }
};




Java:

4 Approaches


// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(n)

1st Method

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<>();  // unordered map to store the number and the index of the number
        for(int i=0; i<nums.length; i++){  // for each element in the vector nums
            if(m.containsKey(target - nums[i])){  // if the target - nums[i] is present in the unordered map
                return new int[]{m.get(target - nums[i]), i};  // return the index of the target - nums[i] and the index of the current element
            }
            m.put(nums[i], i);  // update the index of the current element
        }
        return new int[]{};  // return empty vector
    }
};

2nd Method

class Solution{
    public int[] twoSum(int[] nums , int target){
        for(int i=0 ; i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
        return null;
    }
}


3rd Method

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    return new int[] { i, j };
                }
            }
        }
        // In case there is no solution, we'll just return null
        return null;
    }
}

4th Method

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n= nums.length;
        HashMap<Integer , Integer> m = new HashMap<>();
        for(int i=0; i<n; i++){
            if(m.containsKey(nums[i])){
                return new int[] {m.get(nums[i]) , i};
            }
            m.put(target - nums[i] , i);
        }
        return new int[]{};
    }
}



46. Permutations




26 July 2023




Medium




C++:

// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;  // vector to store the result
        vector<int> temp;  // vector to store the temporary result
        vector<bool> visited(nums.size(), false);  // vector to store the visited values
        permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
        return res;  // return the result
    }
    
    void permuteHelper(vector<int>& nums, vector<vector<int>>& res, vector<int>& temp, vector<bool>& visited){
        if(temp.size() == nums.size()){  // if the size of the temporary result is equal to the size of the vector nums
            res.push_back(temp);  // push the temporary result into the result
            return;  // return
        }
        for(int i = 0; i < nums.size(); i++){  // iterate through the vector nums
            if(visited[i]){  // if the current value is visited
                continue;  // continue
            }
            visited[i] = true;  // update the visited value
            temp.push_back(nums[i]);  // push the current value into the temporary result
            permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
            temp.pop_back();  // pop the current value from the temporary result
            visited[i] = false;  // update the visited value
        }
    }
};



Java:

// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();  // list to store the result
        List<Integer> temp = new ArrayList<>();  // list to store the temporary result
        boolean[] visited = new boolean[nums.length];  // array to store the visited values
        permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
        return res;  // return the result
    }
    
    public void permuteHelper(int[] nums, List<List<Integer>> res, List<Integer> temp, boolean[] visited){
        if(temp.size() == nums.length){  // if the size of the temporary result is equal to the size of the vector nums
            res.add(new ArrayList<>(temp));  // push the temporary result into the result
            return;  // return
        }
        for(int i = 0; i < nums.length; i++){  // iterate through the vector nums
            if(visited[i]){  // if the current value is visited
                continue;  // continue
            }
            visited[i] = true;  // update the visited value
            temp.add(nums[i]);  // push the current value into the temporary result
            permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
            temp.remove(temp.size() - 1);  // pop the current value from the temporary result
            visited[i] = false;  // update the visited value
        }
    }
}



Python:



Python3:




C:



C#




JavaScript:





Swift:

15. 3Sum



11 July 2023


    
Medium



C++:





// Time Complexity : O(n^2) where n is the length of the array and space complexity is O(1)







class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();  // variable to store the length of the array
        vector<vector<int>> result;  // vector to store the result
        sort(nums.begin(), nums.end());  // sort the array
        for(int i = 0; i < n; i++){  // iterate through the array
            if(i > 0 && nums[i] == nums[i - 1]) continue;  // continue if the current value is equal to the previous value
            int left = i + 1;  // variable to store the left pointer
            int right = n - 1;  // variable to store the right pointer
            while(left < right){  // iterate until the left pointer is less than the right pointer
                int sum = nums[i] + nums[left] + nums[right];  // variable to store the sum
                if(sum == 0){  // if the sum is equal to 0
                    result.push_back({nums[i], nums[left], nums[right]});  // push the values to the result
                    left++;  // increment the left pointer
                    right--;  // decrement the right pointer
                    while(left < right && nums[left] == nums[left - 1]) left++;  // increment the left pointer until the current value is equal to the previous value
                    while(left < right && nums[right] == nums[right + 1]) right--;  // decrement the right pointer until the current value is equal to the previous value
                }
                else if(sum < 0){  // if the sum is less than 0
                    left++;  // increment the left pointer
                }
                else{  // if the sum is greater than 0
                    right--;  // decrement the right pointer
                }
            }
        }
        return result;  // return the result
    }
};





Java:

// Time Complexity : O(n^2) where n is the length of the array and space complexity is O(1)







class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;  // variable to store the length of the array
        List<List<Integer>> result = new ArrayList<>();  // list to store the result
        Arrays.sort(nums);  // sort the array
        for(int i = 0; i < n; i++){  // iterate through the array
            if(i > 0 && nums[i] == nums[i - 1]) continue;  // continue if the current value is equal to the previous value
            int left = i + 1;  // variable to store the left pointer
            int right = n - 1;  // variable to store the right pointer
            while(left < right){  // iterate until the left pointer is less than the right pointer
                int sum = nums[i] + nums[left] + nums[right];  // variable to store the sum
                if(sum == 0){  // if the sum is equal to 0
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));  // add the values to the result
                    left++;  // increment the left pointer
                    right--;  // decrement the right pointer
                    while(left < right && nums[left] == nums[left - 1]) left++;  // increment the left pointer until the current value is equal to the previous value
                    while(left < right && nums[right] == nums[right + 1]) right--;  // decrement the right pointer until the current value is equal to the previous value
                }
                else if(sum < 0){  // if the sum is less than 0
                    left++;  // increment the left pointer
                }
                else{  // if the sum is greater than 0
                    right--;  // decrement the right pointer
                }
            }
        }
        return result;  // return the result
    }
}







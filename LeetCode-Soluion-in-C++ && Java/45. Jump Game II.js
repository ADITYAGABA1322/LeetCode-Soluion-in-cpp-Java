45. Jump Game II


25 July 2023



C++:

// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();  // variable to store the length of the vector nums
        int res = 0;  // variable to store the result
        int i = 0;  // variable to store the start index of the window
        int j = 0;  // variable to store the end index of the window
        while(j < n - 1){  // while the end index of the window is less than the length of the vector nums
            int maxIndex = j;  // variable to store the maximum index
            for(int k=i; k<=j; k++){  // for each element in the window
                maxIndex = max(maxIndex, k + nums[k]);  // update the maximum index 
            }
            i = j + 1;  // update the start index of the window
            j = maxIndex;  // update the end index of the window
            res++;  // increment the result
        }
        return res;  // return the result
    }
};




Java:


// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

class Solution {
    public int jump(int[] nums) {
        int n = nums.length;  // variable to store the length of the vector nums
        int res = 0;  // variable to store the result
        int i = 0;  // variable to store the start index of the window
        int j = 0;  // variable to store the end index of the window
        while(j < n - 1){  // while the end index of the window is less than the length of the vector nums
            int maxIndex = j;  // variable to store the maximum index
            for(int k=i; k<=j; k++){  // for each element in the window
                maxIndex = Math.max(maxIndex, k + nums[k]);  // update the maximum index
            }
            i = j + 1;  // update the start index of the window
            j = maxIndex;  // update the end index of the window
            res++;  // increment the result
        }
        return res;  // return the result
    }
}


Python:


// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # variable to store the length of the vector nums
        res = 0  # variable to store the result
        i = 0  # variable to store the start index of the window
        j = 0  # variable to store the end index of the window
        while(j < n - 1):  # while the end index of the window is less than the length of the vector nums
            maxIndex = j  # variable to store the maximum index
            for k in range(i, j + 1):  # for each element in the window
                maxIndex = max(maxIndex, k + nums[k])  # update the maximum index
            i = j + 1  # update the start index of the window
            j = maxIndex  # update the end index of the window
            res += 1  # increment the result
        return res  # return the result




Python3:



// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)  # variable to store the length of the vector nums
        res = 0  # variable to store the result
        i = 0  # variable to store the start index of the window
        j = 0  # variable to store the end index of the window
        while(j < n - 1):  # while the end index of the window is less than the length of the vector nums
            maxIndex = j  # variable to store the maximum index
            for k in range(i, j + 1):  # for each element in the window
                maxIndex = max(maxIndex, k + nums[k])  # update the maximum index
            i = j + 1  # update the start index of the window
            j = maxIndex  # update the end index of the window
            res += 1  # increment the result
        return res  # return the result



C:


// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

int jump(int* nums, int numsSize){
    int n = numsSize;  // variable to store the length of the vector nums
    int res = 0;  // variable to store the result
    int i = 0;  // variable to store the start index of the window
    int j = 0;  // variable to store the end index of the window
    while(j < n - 1){  // while the end index of the window is less than the length of the vector nums
        int maxIndex = j;  // variable to store the maximum index
        for(int k=i; k<=j; k++){  // for each element in the window
            maxIndex = fmax(maxIndex, k + nums[k]);  // update the maximum index
        }
        i = j + 1;  // update the start index of the window
        j = maxIndex;  // update the end index of the window
        res++;  // increment the result
    }
    return res;  // return the result


C#:

// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

public class Solution {
    public int Jump(int[] nums) {
        int n = nums.Length;  // variable to store the length of the vector nums
        int res = 0;  // variable to store the result
        int i = 0;  // variable to store the start index of the window
        int j = 0;  // variable to store the end index of the window
        while(j < n - 1){  // while the end index of the window is less than the length of the vector nums
            int maxIndex = j;  // variable to store the maximum index
            for(int k=i; k<=j; k++){  // for each element in the window
                maxIndex = Math.Max(maxIndex, k + nums[k]);  // update the maximum index
            }
            i = j + 1;  // update the start index of the window
            j = maxIndex;  // update the end index of the window
            res++;  // increment the result
        }
        return res;  // return the result
    }
}


JavaScript:


// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

var jump = function(nums) {
    let n = nums.length;  // variable to store the length of the vector nums
    let res = 0;  // variable to store the result
    let i = 0;  // variable to store the start index of the window
    let j = 0;  // variable to store the end index of the window
    while(j < n - 1){  // while the end index of the window is less than the length of the vector nums
        let maxIndex = j;  // variable to store the maximum index
        for(let k=i; k<=j; k++){  // for each element in the window
            maxIndex = Math.max(maxIndex, k + nums[k]);  // update the maximum index
        }
        i = j + 1;  // update the start index of the window
        j = maxIndex;  // update the end index of the window
        res++;  // increment the result
    }
    return res;  // return the result
};


Swift:

// Time Complexity : O(n) where n is the length of the vector nums and space complexity is O(1)

class Solution {
    func jump(_ nums: [Int]) -> Int {
        let n = nums.count;  // variable to store the length of the vector nums
        var res = 0;  // variable to store the result
        var i = 0;  // variable to store the start index of the window
        var j = 0;  // variable to store the end index of the window
        while(j < n - 1){  // while the end index of the window is less than the length of the vector nums
            var maxIndex = j;  // variable to store the maximum index
            for k in i...j{  // for each element in the window
                maxIndex = max(maxIndex, k + nums[k]);  // update the maximum index
            }
            i = j + 1;  // update the start index of the window
            j = maxIndex;  // update the end index of the window
            res += 1;  // increment the result
        }
        return res;  // return the result
    }
}



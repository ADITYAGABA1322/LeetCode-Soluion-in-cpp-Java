47. Permutations II


27 July 2023


Medium



C++:



// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;  // vector to store the result
        vector<int> temp;  // vector to store the temporary result
        vector<bool> visited(nums.size(), false);  // vector to store the visited values
        sort(nums.begin(), nums.end());  // sort the vector nums
        permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
        return res;  // return the result
    }
    
    void permuteHelper(vector<int>& nums, vector<vector<int>>& res, vector<int>& temp, vector<bool>& visited){
        if(temp.size() == nums.size()){  // if the size of the temporary result is equal to the size of the vector nums
            res.push_back(temp);  // push the temporary result into the result
            return;  // return
        }
        for(int i = 0; i < nums.size(); i++){  // iterate through the vector nums
            if(visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])){  // if the current value is visited or the current value is equal to the previous value and the previous value is not visited
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
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();  // list to store the result
        List<Integer> temp = new ArrayList<>();  // list to store the temporary result
        boolean[] visited = new boolean[nums.length];  // array to store the visited values
        Arrays.sort(nums);  // sort the vector nums
        permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
        return res;  // return the result
    }
    
    public void permuteHelper(int[] nums, List<List<Integer>> res, List<Integer> temp, boolean[] visited){
        if(temp.size() == nums.length){  // if the size of the temporary result is equal to the size of the vector nums
            res.add(new ArrayList<>(temp));  // push the temporary result into the result
            return;  // return
        }
        for(int i = 0; i < nums.length; i++){  // iterate through the vector nums
            if(visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])){  // if the current value is visited or the current value is equal to the previous value and the previous value is not visited
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


// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        res = []  # list to store the result
        temp = []  # list to store the temporary result
        visited = [False] * len(nums)  # array to store the visited values
        nums.sort()  # sort the vector nums
        self.permuteHelper(nums, res, temp, visited)  # call the function to find the permutations
        return res  # return the result
    
    def permuteHelper(self, nums, res, temp, visited):
        if len(temp) == len(nums):  # if the size of the temporary result is equal to the size of the vector nums
            res.append(temp[:])  # push the temporary result into the result
            return  # return
        for i in range(len(nums)):  # iterate through the vector nums
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):  # if the current value is visited or the current value is equal to the previous value and the previous value is not visited
                continue  # continue
            visited[i] = True  # update the visited value
            temp.append(nums[i])  # push the current value into the temporary result
            self.permuteHelper(nums, res, temp, visited)  # call the function to find the permutations
            temp.pop()  # pop the current value from the temporary result
            visite



Python3:



// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

class Solution:
    def permuteUnique(self, nums: List[int) -> List[List[int]]: // add the missing bracket after int
        res = []  # list to store the result
        temp = []  # list to store the temporary result
        visited = [False] * len(nums)  # array to store the visited values
        nums.sort()  # sort the vector nums
        self.permuteHelper(nums, res, temp, visited)  # call the function to find the permutations
        return res  # return the result
    
    def permuteHelper(self, nums, res, temp, visited):
        if len(temp) == len(nums):  # if the size of the temporary result is equal to the size of the vector nums
            res.append(temp[:])  # push the temporary result into the result
            return  # return
        for i in range(len(nums)):  # iterate through the vector nums
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):  # if the current value is visited or the current value is equal to the previous value and the previous value is not visited
                continue  # continue
            visited[i] = True  # update the visited value
            temp.append(nums[i])  # push the current value into the temporary result
            self.permuteHelper(nums, res, temp, visited)  # call the function to find the permutations
            temp.pop()  # pop the current value from the temporary result
            visited[i] = False  # update the visited value



C:


// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

void permuteHelper(int* nums, int numsSize, int** res, int* returnSize, int* temp, bool* visited, int index){
    if(index == numsSize){  // if the size of the temporary result is equal to the size of the vector nums
        res[*returnSize] = (int*)malloc(sizeof(int) * numsSize);  // push the temporary result into the result
        memcpy(res[*returnSize], temp, sizeof(int) * numsSize);  // push the temporary result into the result
        (*returnSize)++;  // increment the result
        return;  // return
    }
    for(int i = 0; i < numsSize; i++){  // iterate through the vector nums
        if(visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])){  // if the current value is visited or the current value is equal to the previous value and the previous value is not visited
            continue;  // continue
        }
        visited[i] = true;  // update the visited value
        temp[index] = nums[i];  // push the current value into the temporary result
        permuteHelper(nums, numsSize, res, returnSize, temp, visited, index + 1);  // call the function to find the permutations
        visited[i] = false;  // update the visited value
    }
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int** res = (int**)malloc(sizeof(int*) * 10000);  // vector to store the result
    int* temp = (int*)malloc(sizeof(int) * numsSize);  // vector to store the temporary result
    bool* visited = (bool*)malloc(sizeof(bool) * numsSize);  // array to store the visited values
    memset(visited, false, sizeof(bool) * numsSize);  // update the visited value
    *returnSize = 0;  // update the result
    qsort(nums, numsSize, sizeof(int), cmpfunc);  // sort the vector nums
    permuteHelper(nums, numsSize, res, returnSize, temp, visited, 0);  // call the function to find the permutations
    *returnColumnSizes = (int*)malloc(sizeof(int) * (*returnSize));  // vector to store the result
    for(int i = 0; i < *returnSize; i++){  // iterate through the vector nums
        (*returnColumnSizes)[i] = numsSize;  // update the result
    }
    return res;  // return the result
}
int cmpfunc(const void* a, const void* b){
    return (*(int*)a - *(int*)b);  // return the result
}

C#


// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        IList<IList<int>> res = new List<IList<int>>();  // list to store the result
        List<int> temp = new List<int>();  // list to store the temporary result
        bool[] visited = new bool[nums.Length];  // array to store the visited values
        Array.Sort(nums);  // sort the vector nums
        permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
        return res;  // return the result
    }
    
    public void permuteHelper(int[] nums, IList<IList<int>> res, List<int> temp, bool[] visited){
        if(temp.Count == nums.Length){  // if the size of the temporary result is equal to the size of the vector nums
            res.Add(new List<int>(temp));  // push the temporary result into the result
            return;  // return
        }
        for(int i = 0; i < nums.Length; i++){  // iterate through the vector nums
            if(visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])){  // if the current value is visited or the current value is equal to the previous value and the previous value is not visited
                continue;  // continue
            }
            visited[i] = true;  // update the visited value
            temp.Add(nums[i]);  // push the current value into the temporary result
            permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
            temp.RemoveAt(temp.Count - 1);  // pop the current value from the temporary result
            visited[i] = false;  // update the visited value
        }
    }
}


JavaScript:

// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

var permuteUnique = function(nums) {
    let res = [];  // list to store the result
    let temp = [];  // list to store the temporary result
    let visited = new Array(nums.length).fill(false);  // array to store the visited values
    nums.sort();  // sort the vector nums
    permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
    return res;  // return the result
};

var permuteHelper = function(nums, res, temp, visited){
    if(temp.length == nums.length){  // if the size of the temporary result is equal to the size of the vector nums
        res.push(temp.slice());  // push the temporary result into the result
        return;  // return
    }
    for(let i = 0; i < nums.length; i++){  // iterate through the vector nums
        if(visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])){  // if the current value is visited or the current value is equal to the previous value and the previous value is not visited
            continue;  // continue
        }
        visited[i] = true;  // update the visited value
        temp.push(nums[i]);  // push the current value into the temporary result
        permuteHelper(nums, res, temp, visited);  // call the function to find the permutations
        temp.pop();  // pop the current value from the temporary result
        visited[i] = false;  // update the visited value
    }
};



Swift:

// Time Complexity : O(n!) where n is the length of the vector nums and space complexity is O(n)

class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        var res = [[Int]]()  // list to store the result
        var temp = [Int]()  // list to store the temporary result
        var visited = [Bool](repeating: false, count: nums.count)  // array to store the visited values
        let sortedNums = nums.sorted()  // Sort the input array in ascending order
        permuteHelper(sortedNums, &res, &temp, &visited)  // call the function to find the permutations
        return res  // return the result
    }
    
    func permuteHelper(_ nums: [Int], _ res: inout [[Int]], _ temp: inout [Int], _ visited: inout [Bool]) {
        if temp.count == nums.count {  // if the size of the temporary result is equal to the size of the vector nums
            res.append(temp)  // push the temporary result into the result
            return  // return
        }
        for i in 0..<nums.count {  // iterate through the vector nums
            if visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) {  // if the current value is visited or the current value is equal to the previous value and the previous value is not visited
                continue  // continue
            }
            visited[i] = true  // update the visited value
            temp.append(nums[i])  // push the current value into the temporary result
            permuteHelper(nums, &res, &temp, &visited)  // call the function to find the permutations
            temp.removeLast()  // pop the current value from the temporary result
            visited[i] = false  // update the visited value
        }
    }
}

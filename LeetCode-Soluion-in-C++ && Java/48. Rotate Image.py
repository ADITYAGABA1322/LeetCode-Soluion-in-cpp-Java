48. Rotate Image


27 July 2023

Medium


C++:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();  // variable to store the length of the vector matrix
        for(int i = 0; i < n; i++){  // iterate through the vector matrix
            for(int j = i; j < n; j++){  // iterate through the vector matrix
                swap(matrix[i][j], matrix[j][i]);  // swap the values
            }
        }
        for(int i = 0; i < n; i++){  // iterate through the vector matrix
            reverse(matrix[i].begin(), matrix[i].end());  // reverse the vector
        }
    }
};

Java:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;  // variable to store the length of the vector matrix
        for(int i = 0; i < n; i++){  // iterate through the vector matrix
            for(int j = i; j < n; j++){  // iterate through the vector matrix
                int temp = matrix[i][j];  // variable to store the temporary result
                matrix[i][j] = matrix[j][i];  // swap the values
                matrix[j][i] = temp;  // swap the values
            }
        }
        for(int i = 0; i < n; i++){  // iterate through the vector matrix
            for(int j = 0; j < n / 2; j++){  // iterate through the vector matrix
                int temp = matrix[i][j];  // variable to store the temporary result
                matrix[i][j] = matrix[i][n - j - 1];  // swap the values
                matrix[i][n - j - 1] = temp;  // swap the values
            }
        }
    }
}

python:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        n = len(matrix)  # variable to store the length of the vector matrix
        for i in range(n):  # iterate through the vector matrix
            for j in range(i, n):  # iterate through the vector matrix
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swap the values
        for i in range(n):  # iterate through the vector matrix
            matrix[i].reverse()  # reverse the vector


python3:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        n = len(matrix)  # variable to store the length of the vector matrix
        for i in range(n):  # iterate through the vector matrix
            for j in range(i, n):  # iterate through the vector matrix
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swap the values
        for i in range(n):  # iterate through the vector matrix
            matrix[i].reverse()  # reverse the vector
C:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int n = matrixSize;  // variable to store the length of the vector matrix
    for(int i = 0; i < n; i++){  // iterate through the vector matrix
        for(int j = i; j < n; j++){  // iterate through the vector matrix
            int temp = matrix[i][j];  // variable to store the temporary result
            matrix[i][j] = matrix[j][i];  // swap the values
            matrix[j][i] = temp;  // swap the values
        }
    }
    for(int i = 0; i < n; i++){  // iterate through the vector matrix
        for(int j = 0; j < n / 2; j++){  // iterate through the vector matrix
            int temp = matrix[i][j];  // variable to store the temporary result
            matrix[i][j] = matrix[i][n - j - 1];  // swap the values
            matrix[i][n - j - 1] = temp;  // swap the values
        }
    }
}

C#:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

public class Solution {
    public void Rotate(int[][] matrix) {
        int n = matrix.Length;  // variable to store the length of the vector matrix
        for(int i = 0; i < n; i++){  // iterate through the vector matrix
            for(int j = i; j < n; j++){  // iterate through the vector matrix
                int temp = matrix[i][j];  // variable to store the temporary result
                matrix[i][j] = matrix[j][i];  // swap the values
                matrix[j][i] = temp;  // swap the values
            }
        }
        for(int i = 0; i < n; i++){  // iterate through the vector matrix
            for(int j = 0; j < n / 2; j++){  // iterate through the vector matrix
                int temp = matrix[i][j];  // variable to store the temporary result
                matrix[i][j] = matrix[i][n - j - 1];  // swap the values
                matrix[i][n - j - 1] = temp;  // swap the values
            }
        }
    }
}

javascript:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

var rotate = function(matrix) {
    let n = matrix.length;  // variable to store the length of the vector matrix
    for(let i = 0; i < n; i++){  // iterate through the vector matrix
        for(let j = i; j < n; j++){  // iterate through the vector matrix
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];  // swap the values
        }
    }
    for(let i = 0; i < n; i++){  // iterate through the vector matrix
        for(let j = 0; j < n / 2; j++){  // iterate through the vector matrix
            [matrix[i][j], matrix[i][n - j - 1]] = [matrix[i][n - j - 1], matrix[i][j]];  // swap the values
        }
    }
};

Swift:

// Time Complexity : O(n^2) where n is the length of the vector matrix and space complexity is O(1)

class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count;  // variable to store the length of the vector matrix
        for i in 0..<n {  // iterate through the vector matrix
            for j in i..<n {  // iterate through the vector matrix
                let temp = matrix[i][j];  // variable to store the temporary result
                matrix[i][j] = matrix[j][i];  // swap the values
                matrix[j][i] = temp;  // swap the values
            }
        }
        for i in 0..<n {  // iterate through the vector matrix
            for j in 0..<n / 2 {  // iterate through the vector matrix
                let temp = matrix[i][j];  // variable to store the temporary result
                matrix[i][j] = matrix[i][n - j - 1];  // swap the values
                matrix[i][n - j - 1] = temp;  // swap the values
            }
        }
    }
}


13. Roman to Integer


    
    
24 April 2023




Easy




C++:



// Time Complexity : O(n) where n is the length of the string and space complexity is O(1) as we are not using any extra space


class Solution {
public:
    int romanToInt(string s) {
        int ans = 0 , num = 0 , prev = 0;
        for(int i=s.length()-1; i>=0; i--){
            switch(s[i]){
                case 'I': num = 1; break;
                case 'V': num = 5; break;
                case 'X': num = 10; break;
                case 'L': num = 50; break;
                case 'C': num = 100; break;
                case 'D': num = 500; break;
                case 'M': num = 1000; break;
            }
            if(num < prev) ans -= num;
            else ans += num;
            prev = num;
        }
        return ans;
    }
};


Java:



// Time Complexity : O(n) where n is the length of the string and space complexity is O(1) as we are not using any extra space



class Solution {
    public int romanToInt(String s) {
        int ans = 0;
        int num = 0;
        int prev = 0;
        for(int i = s.length() - 1; i >= 0; i--){
            switch(s.charAt(i)){
                case 'I': num = 1; break;
                case 'V': num = 5; break;
                case 'X': num = 10; break;
                case 'L': num = 50; break;
                case 'C': num = 100; break;
                case 'D': num = 500; break;
                case 'M': num = 1000; break;
            }
            if(num < prev) ans -= num;
            else ans += num;
            prev = num;
        }
        return ans;
    }
};


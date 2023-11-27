1323. Maximum 69 Number


	
	
22 Feb 2023
	
	

	
Easy

	

C++:



// Time Complexity : O(n) where n is the length of the string and space complexity is O(n)


class Solution {
public:
    int maximum69Number (int num) {
        string s = to_string(num);   // string s=to_string(num)
        for(int i = 0; i < s.size(); ++i){   // loop for i
            if(s[i] == '6'){   // if condition is true
                s[i] = '9';   // s[i]='9'
                break;   // break
            }
        }
        return stoi(s);   // return stoi(s)
    }
};



Java:



// Time Complexity : O(n) where n is the length of the string and space complexity is O(n)


class Solution {
    public int maximum69Number (int num) {
        String s = String.valueOf(num);   // String s=String.valueOf(num)
        for(int i = 0; i < s.length(); ++i){   // loop for i
            if(s.charAt(i) == '6'){   // if condition is true
                s = s.substring(0, i) + '9' + s.substring(i + 1);   // s=s.substring(0,i)+'9'+s.substring(i+1)
                break;   // break
            }
        }
        return Integer.parseInt(s);   // return Integer.parseInt(s)
    }
};


2nd Method :


class Solution {
    public int maximum69Number (int num) {
    char arr[] = String.valueOf(num).toCharArray(); 

	for(int i =0;i<arr.length;i++){
        if(arr[i]=='6'){                        
			arr[i]='9';
            break;
        }
    }
	return Integer.parseInt(new String(arr));
    }
}


3rd Method :


class Solution {
    public int maximum69Number (int num) {
        return Integer.parseInt(("" + num).replaceFirst("6"  , "9"));
    }
}



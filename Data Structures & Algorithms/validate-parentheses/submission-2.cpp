class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(char a : s) {
            if(a == '(' || a == '[' || a == '{') {
                st.push(a);
            }
            else if(a == ')' || a == ']' || a == '}') {
                if(st.empty()) {
                    return false;
                }
                if (a == ')') {
                    if(st.top() != '(') {
                        return false;
                    }
                    else {
                        st.pop();
                    }
                }
                else if(a == '}') {
                    if(st.top() != '{') {
                        return false;
                    }
                    else {
                        st.pop();
                    }
                }
                else {
                    if(st.top() != '[') {
                        return false;
                    }
                    else {
                        st.pop();
                    }
                }
            }
        }

        if(st.empty()) {
            return true;
        }
        return false;
    }
};

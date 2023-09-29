import java.util.ArrayList;


class Solution {
    boolean solution(String s) {
        ArrayList <Character> chars = new ArrayList <> ();
        
        for (char c: s.toCharArray()) {
            if (chars.isEmpty()) chars.add(c);
            else if (c == '(') chars.add(c);
            else if (c == ')' && chars.get(chars.size() - 1) == '(') {
                chars.remove(chars.size() - 1);
            }
        }
        
        return chars.size() == 0 ? true : false;
    }
}
import java.util.Set;
import java.util.HashSet;


class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set <Integer> num_set = new HashSet <> ();
        for (int num : nums) {
            num_set.add(num);
        }
        
        int num_unique = num_set.size();
        int num_select = nums.length / 2;
        
        answer = (num_unique > num_select) ? num_select : num_unique;
        
        return answer;
    }
}
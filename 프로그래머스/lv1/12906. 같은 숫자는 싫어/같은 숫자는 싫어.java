import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List <Integer> answer = new ArrayList <>();
        
        for (int element: arr) {
            if (answer.isEmpty()) answer.add(element);
            else if (answer.get(answer.size() - 1) != element) answer.add(element);
        }
        
        int [] new_answer = answer.stream().mapToInt(i -> i).toArray();
        
        return new_answer;
    }
}
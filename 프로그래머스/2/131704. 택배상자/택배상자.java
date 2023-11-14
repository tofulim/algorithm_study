import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;


// Queue(1st belt)와 stack(2st belt)을 이용해야함
// 2st belt써도 만족못할때 종료
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        
        Stack <Integer> second_belt = new Stack <> ();
        Queue <Integer> first_belt = new LinkedList <> ();
        for (int i = 0; i < order.length; i++) first_belt.offer(i);
        
        for (int curr_box : order) {
            // sb에 들은 값인지 확인한다.
            if (second_belt.contains(curr_box)) {
                // sb 최상단일 경우 계속 진행한다.
                if (!second_belt.isEmpty() && second_belt.peek() == curr_box) {
                    second_belt.pop();
                    answer += 1; 
                }
                // 더 이상 실을 수 없다.
                else break;
            }
            // fb에 있는 값이므로 순회한다.
            else {
                while (!first_belt.isEmpty() && first_belt.peek() != curr_box) {
                    second_belt.push(first_belt.poll());
                }
                first_belt.poll();
                answer += 1;
            }
        }
        
        return answer;
    }
}
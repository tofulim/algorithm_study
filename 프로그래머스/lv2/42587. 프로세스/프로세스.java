import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;


class Solution {
    class Process {
        int idx;
        int val;
        public Process(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue <Process> process_queue = new LinkedList <> ();
        for (int idx = 0; idx < priorities.length; idx++) {
            process_queue.offer(new Process(idx, priorities[idx]));
        }
        
        Arrays.sort(priorities);
        int max_idx = priorities.length - 1;
        int process_idx = -1;
        
        while (process_idx != location) {
            Process curr_p = process_queue.peek();
            // 최대값이 아닌 값이라면 다시 뒤로 줄세운다
            if (process_queue.peek().val != priorities[max_idx]) {
                process_queue.offer(process_queue.poll());
            }
            // 프로세스 실행
            else {
                process_idx = curr_p.idx;
                answer++;
                process_queue.poll();
                max_idx--;
            }
        }
        
        return answer;
    }
}
import java.util.Queue;
import java.util.LinkedList;
import java.util.stream.IntStream;

// 1. 큰 쪽 poll & offer
// 2. 크기 비교
// 3. 종료 조건은 sum이 홀수이거나 총 이동 횟수가 queue_len * 2 보다 커질 때

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        
        long q1_sum = IntStream.of(queue1).sum();
        long q2_sum = IntStream.of(queue2).sum();
        long total = q1_sum + q2_sum;
        long target = total / 2;
        // 3. 종료 조건 1 홀수
        if (total % 2 == 1) return -1;
        
        Queue <Integer> q1 = new LinkedList <>();
        for (int _q1 : queue1) q1.offer(_q1);
        Queue <Integer> q2 = new LinkedList <>();
        for (int _q2 : queue2) q2.offer(_q2);
        
        int count = 0;
        while (q1_sum != target && count <= (queue1.length * 2 + 1)) {
            if (q1_sum < q2_sum) {
                // poll & offer
                int q2_top = q2.poll();
                q1.offer(q2_top);
                // calc
                q1_sum += q2_top;
                q2_sum -= q2_top;
            }
            else {
                // poll & offer
                int q1_top = q1.poll();
                q2.offer(q1_top);
                // calc
                q2_sum += q1_top;
                q1_sum -= q1_top;
            }
            answer += 1;
            count += 1;
        }        
        
        if (q1_sum == q2_sum) return answer;
        else return -1;
    }
    
}
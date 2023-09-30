import java.util.ArrayList;
import java.util.Arrays;


class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList <Integer> answer = new ArrayList <> ();
        // 작업 진도, 속도 큐 각각 선언
        ArrayList <Integer> process_queue = new ArrayList <> ();
        for (int progress: progresses) process_queue.add(progress);
        ArrayList <Integer> speed_queue = new ArrayList <> ();
        for (int speed: speeds) speed_queue.add(speed);
        
        while (!process_queue.isEmpty()) {
            // 작업량 업데이트
            for (int idx = 0; idx < process_queue.size(); idx++) {
                int curr_queue_val = process_queue.get(idx);
                int curr_speed_val = speed_queue.get(idx);
                process_queue.set(idx, curr_queue_val + curr_speed_val);
            }
            // 배포 시작 조건 확인
            if (process_queue.get(0) < 100) continue;
            // 배포 가능 작업 확인
            int deploy_cnt = 0;
            while (!process_queue.isEmpty() && process_queue.get(0) >= 100) {
                process_queue.remove(0);
                speed_queue.remove(0);
                deploy_cnt += 1;
            }
            if (deploy_cnt != 0) answer.add(deploy_cnt);
        }
        
        int [] f_answer = answer.stream().mapToInt(i -> i).toArray();
        
        return f_answer;
    }
}
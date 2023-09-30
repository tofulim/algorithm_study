import java.util.List;
import java.util.ArrayList;


class Solution {
    public int[] solution(int[] answers) {
        List <Integer> answer = new ArrayList <> ();
        int[] supo1 = {1, 2, 3, 4, 5}; // 5
        int[] supo2 = {2, 1, 2, 3, 2, 4 ,2 ,5}; // 8
        int[] supo3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; // 10 
        
        int sp1_cnt = 0, sp2_cnt = 0, sp3_cnt = 0;
        
        for (int idx = 0; idx < answers.length; idx++) {
            int curr_answer = answers[idx];
            sp1_cnt += supo1[idx % 5] == curr_answer ? 1 : 0;
            sp2_cnt += supo2[idx % 8] == curr_answer ? 1 : 0;
            sp3_cnt += supo3[idx % 10] == curr_answer ? 1 : 0;
        } 
        
        int max_cnt = Math.max(sp1_cnt, Math.max(sp2_cnt, sp3_cnt));
        int [] cnt_list = {sp1_cnt, sp2_cnt, sp3_cnt};
        for (int idx = 0; idx < 3; idx++) {
            if (cnt_list[idx] == max_cnt) answer.add(idx + 1);
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}
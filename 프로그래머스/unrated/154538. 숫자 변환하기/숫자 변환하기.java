import java.util.Queue;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import java.util.LinkedList;


class Solution {
    public int solution(int x, int y, int n) {
        Queue <Number> queue = new LinkedList <>();
        Set <Integer> hs = new HashSet<> ();
        queue.offer(new Number(x, 0));
        hs.add(x);
        
        while (!queue.isEmpty()) {
            Number curr_number = queue.poll();
            int num = curr_number.num;
            int cnt = curr_number.cnt;
            hs.remove(num);
            
            if (num == y) return cnt;
            else {
                int add_num = num + n;
                int multi2_num = num * 2;
                int multi3_num = num * 3;
                if (add_num <= y && !hs.contains(add_num)) {
                    queue.offer(new Number(add_num, cnt + 1));
                    hs.add(add_num);
                }
                if (multi2_num <= y && !hs.contains(multi2_num)) {
                    queue.offer(new Number(multi2_num, cnt + 1));
                    hs.add(multi2_num);
                }
                if (multi3_num <= y && !hs.contains(multi3_num)) {
                    queue.offer(new Number(multi3_num, cnt + 1));
                    hs.add(multi3_num);
                }
            }
        }
        
        return -1;
    }
    class Number {
        int num;
        int cnt;
        
        public Number(int num, int cnt) {
            this.num = num;
            this.cnt = cnt;
        }
    }
}
import java.util.HashSet;


class Solution {
    public int solution(String numbers) {
        // 1. for loop by 길이(1-length) 
        // 2. visit 여부로 소수 후보자 구하기
        // 3. 소수 확인 후 set에 넣기
        int answer = 0;
        boolean[] visit = new boolean[numbers.length()];
        for (int idx = 0; idx < numbers.length(); idx++) visit[idx] = false;
        
        HashSet <Integer> hs = new HashSet<> ();
        
        for (int idx = 0; idx < numbers.length(); idx++) {
            String curr_number = "" + numbers.charAt(idx);
            visit[idx] = true;
            permutation(visit, hs, numbers, curr_number);
            visit[idx] = false;
        }
        
        for (Integer candidate: hs) {
            if (is_prime((int) candidate)) answer++;
        }
        
        return answer;
    }
    public void permutation(boolean[] visit, HashSet <Integer> hs, String numbers, String curr_number){
        int candidate = Integer.parseInt(curr_number);
        hs.add(candidate);
        
        for (int idx = 0; idx < numbers.length(); idx++) {
            if (!visit[idx]) {
                visit[idx] = true;
                permutation(visit, hs, numbers, curr_number + numbers.charAt(idx));
                visit[idx] = false;
            }
        }
    }
    public boolean is_prime(int number) {
        if (number == 2) return true;
        else if (number < 2) return false;
        else {
            for (int divider = 2; divider <= Math.sqrt((double) number); divider++) {
                if (number % divider == 0) return false;
            }    
            return true;
        }
        
    }
}
import java.util.Arrays;


class Solution {
    static int answer = 1000000;
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) return 0;
        
        boolean[] visit = new boolean[words.length];
        Arrays.fill(visit, false);
        
        for (int idx = 0; idx < words.length; idx++) {
            visit[idx] = true;
            dfs(words, visit, begin, target, 0);
            visit[idx] = false;
        }
        
        return (answer == 1000000) ? 0 : answer;
    }
    public void dfs(String[] words, boolean[] visit, String curr_word, String target, int cnt) {
        if (curr_word.equals(target)) {
            answer = Math.min(answer, cnt);
            return;
        }
        for (int idx = 0; idx < words.length; idx++) {
            String comp_word = words[idx];
            if (!visit[idx] && is_valid(curr_word, comp_word)) {
                visit[idx] = true;
                dfs(words, visit, comp_word, target, cnt + 1);
                visit[idx] = false;
            }
        }
    }
    public boolean is_valid(String s1, String s2) {
        int diff_cnt = 0;
        for (int idx = 0; idx < s1.length(); idx++) {
            if (s1.charAt(idx) != s2.charAt(idx)) diff_cnt++;
        }
        
        return (diff_cnt == 1) ? true : false;
    }
}
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visit = new boolean[computers.length];
        for (int idx = 0; idx < computers.length; idx++) visit[idx] = false;
        
        for (int idx = 0; idx < computers.length; idx++) {
            if (!visit[idx]) {
                dfs(computers, idx, visit);
                answer++;
            }
        }
        return answer;
    }
    public void dfs(int[][] computers, int idx, boolean[] visit) {
        for (int sub_idx = 0; sub_idx < computers.length; sub_idx++) {
            if (sub_idx == idx || visit[sub_idx]) continue;
            if (computers[idx][sub_idx] == 1) {
                visit[idx] = true;
                visit[sub_idx] = true;
                dfs(computers, sub_idx, visit);
            }
        }
    }
}
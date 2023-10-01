class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, -numbers[0], 1);
        dfs(numbers, target, numbers[0], 1);
        return answer;
    }
    public void dfs(int[] numbers, int target, int result, int idx) {
        if (idx > numbers.length - 1) {
            if (result == target) answer++;
            return;
        }
        
        int curr_number = numbers[idx];
        
        dfs(numbers, target, result + curr_number, idx + 1);
        dfs(numbers, target, result - curr_number, idx + 1);
    }
}
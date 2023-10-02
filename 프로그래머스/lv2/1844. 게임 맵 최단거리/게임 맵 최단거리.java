import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;


class Solution {
    static int answer = 1000000000;
    static int[] i_arr = {0, 0, -1, 1};
    static int[] j_arr = {-1, 1, 0, 0};
    
    public int solution(int[][] maps) {
        // visit 배열 초기화
        boolean[][] visit = new boolean[maps.length][maps[0].length];
        for (boolean[] _visit: visit) Arrays.fill(_visit, false);
        // 목표지점인 target 배열 선언
        int[] target = {0, 0};
        // 현재 위치를 종료점으로 선택하고 target(0, 0)찾기
        visit[maps.length -1][maps[0].length -1] = true;
        bfs(maps, visit, maps.length - 1, maps[0].length - 1, 1, target);
            
        return (answer == 1000000000) ? -1 : answer;
    }
    public void bfs(int[][] maps, boolean[][] visit, int i, int j, int cnt, int[] target) {
        Queue <Node> queue = new LinkedList <> ();
        queue.offer(new Node(i, j, cnt));
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            
            if (node.i == target[0] && node.j == target[1]) {
                answer = Math.min(answer, node.cnt);
                return;
            }
            for (int idx = 0; idx < 4; idx++) {
                int new_i = node.i + i_arr[idx];
                int new_j = node.j + j_arr[idx];
                if (0 <= new_i && new_i < maps.length && 0 <= new_j && new_j < maps[0].length && maps[new_i][new_j] == 1 && !visit[new_i][new_j]) {
                    visit[new_i][new_j] = true;
                    queue.offer(new Node(new_i, new_j, node.cnt + 1));
                }
            }
        }
    }
    class Node {
        int i;
        int j;
        int cnt;
        public Node(int i, int j, int cnt) {
            this.i = i;
            this.j = j;
            this.cnt = cnt;
        }
    }
}
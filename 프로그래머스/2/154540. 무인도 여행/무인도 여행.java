import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;


class Solution {
    int[] dir_x = {0, 1, 0, -1};
    int[] dir_y = {1, 0, -1, 0};
    public int[] solution(String[] maps) {
        int[] answer = {-1};
        List <Integer> al_answer = new ArrayList <> ();
        
        // 방문확인할 visit 배열 초기화
        boolean[][] visit = new boolean[maps.length][maps[0].length()];
        for (boolean[] _visit : visit) Arrays.fill(_visit, false);
        
        for (int i = 0; i < visit.length; i++) {
            String map = maps[i];
            for (int j = 0; j < map.length(); j++) {
                char loc_value = map.charAt(j);
                // 방문하지 않은 무인도
                if (loc_value != 'X' && !visit[i][j]) {
                    int food_sum = bfs(visit, maps, i, j);
                    al_answer.add(food_sum);
                }
            }
        }
        Collections.sort(al_answer);
        if (al_answer.isEmpty()) {
            return answer;
        }
        else {
            answer = al_answer.stream().mapToInt(Integer::intValue).toArray();
            return answer;
        }
    }
    public int bfs(boolean[][] visit, String[] maps, int i, int j) {
        int food_sum = 0;
        
        Queue <Pair> queue = new LinkedList <> ();
        queue.offer(new Pair(i, j));
        visit[i][j] = true;
        
        while (!queue.isEmpty()) {
            Pair location = queue.poll();
            int curr_x = location.x;
            int curr_y = location.y;
            
            int loc_value = maps[curr_y].charAt(curr_x) - 48;
            food_sum += loc_value;
            // 동서남북 연결된 무인도를 찾는다.
            for (int idx = 0; idx < 4; idx++) {
                int new_y = curr_y + dir_y[idx];
                int new_x = curr_x + dir_x[idx];
                if (0 <= new_y && new_y < maps.length && 0 <= new_x && new_x < maps[0].length() && !visit[new_y][new_x] && maps[new_y].charAt(new_x) != 'X') {
                    queue.offer(new Pair(new_y, new_x));
                    visit[new_y][new_x] = true;
                }
            }
            
        }
        
        return food_sum;
    }       
}

class Pair {
    int x;
    int y;
    Pair(int y, int x) {
        this.x = x;
        this.y = y;
    }
}
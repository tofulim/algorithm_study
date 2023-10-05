import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Comparator;


class Solution {
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList <>();
        // 시작시간 asc sort
        Arrays.sort(plans, new Comparator<String[]> () {
            @Override
            public int compare(String[] s1, String[] s2) {
                return s1[1].compareTo(s2[1]);
            }
        });
        // init stack
        List<Task> stack = new ArrayList<> ();
        
        // queue offer
        Queue <Task> task_queue = new LinkedList <>();
        for (String[] plan: plans) task_queue.offer(new Task(plan[0], plan[1], Integer.parseInt(plan[2])));
        
        // 현재 시간 초기화
        int curr_time = task_queue.peek().start_minutes;
        while (!task_queue.isEmpty()) {
            Task curr_task = task_queue.poll();
            // 수행해야하는 stack 맨 뒤에 적재
            stack.add(curr_task);
            // 마지막 task stack 맨 뒤에 적재
            if (task_queue.isEmpty()) {
                break;
            } 
            // 현 작업을 진행하며 다음 작업을 peek
            Task next_task = task_queue.peek();
            // stack에 남은 작업을 제한 시간 내에 수행할 수 있을때까지 수행
            while (!stack.isEmpty()) {
                Task stack_task = stack.remove(stack.size() -1);
                // 수행가능한 stack task의 경우
                if (curr_time + stack_task.playtime <= next_task.start_minutes) {
                    curr_time += stack_task.playtime;
                    answer.add(stack_task.task_name);
                } else {
                    // 시간이 모자라는 stack task는 시간 갱신 후 다시 넣는다
                    int remain_time = next_task.start_minutes - curr_time;
                    stack_task.playtime -= remain_time;
                    curr_time = next_task.start_minutes;
                    stack.add(stack_task);
                    break;
                }
            }
            curr_time = next_task.start_minutes;
        }
        while (!stack.isEmpty()) answer.add(stack.remove(stack.size() -1).task_name);
        
        return answer.toArray(new String[0]);
    }
    class Task {
        String task_name;
        int start_minutes;
        int playtime;
        
        public Task(String task_name, String start, int playtime) {
            this.task_name = task_name;
            String[] splited_start = start.split(":");
            int start_minutes = Integer.parseInt(splited_start[0]) * 60 + Integer.parseInt(splited_start[1]);
            this.start_minutes = start_minutes;
            this.playtime = playtime;
        }
    }
}
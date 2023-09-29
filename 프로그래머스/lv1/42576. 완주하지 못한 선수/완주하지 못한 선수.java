import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Collection;


class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        // 참가자를 HashMap으로 만든다.
        Map <String, Integer> completion_map = new HashMap <> ();
        // 참가자 이름 기준 빈도 count
        for (String _completion: completion){
            completion_map.compute(_completion, (key, value) -> (value == null) ? 1 : value + 1);
        }
        
        // 완주자 기준으로 참가자를 조회하고 빈도가 0이라면 정답으로 반환한다.
        for (String _participant: participant){
            int cnt = completion_map.getOrDefault(_participant, 0);
            if (cnt == 0){
                answer = _participant;
                break;
            } else {
                completion_map.put(_participant, cnt - 1);
            }
                
        }
        
        return answer;
    }
}
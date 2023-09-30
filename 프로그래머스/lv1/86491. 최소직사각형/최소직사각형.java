class Solution {
    public int solution(int[][] sizes) {
        int width_max = 0;
        int height_max = 0;
        for (int[] size: sizes) {
            int width = Math.max(size[0], size[1]);
            int height = Math.min(size[0], size[1]);
            width_max = Math.max(width_max, width);
            height_max = Math.max(height_max, height);
        }
        
        return width_max * height_max;
    }
}
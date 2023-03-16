class Solution {
    public int[][] solution(int[] num_list, int n) {
        int[][] answer = {};

        int length = num_list.length;

        answer = new int[length/n][n];

        for(int i=0; i<length; i++){  // for문 한번만 사용
            answer[i/n][i%n]=num_list[i];   // 나누기와 나머지.... 어렵다!
        }

        return answer;
    }
}
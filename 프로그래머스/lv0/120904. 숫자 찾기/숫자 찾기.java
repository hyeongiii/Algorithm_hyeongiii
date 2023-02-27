class Solution {
    public int solution(int num, int k) {
        String numS = Integer.toString(num);
        String sk = Integer.toString(k);
        if(numS.indexOf(sk) == -1) {
            return -1;
        } else {
            return numS.indexOf(sk) + 1;
        }
    }
}
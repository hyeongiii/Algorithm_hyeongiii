import java.util.*;
import java.io.*;

public class Main {
    
    static StringBuilder sb = new StringBuilder();
    static FastReader scan = new FastReader();
    
    static int N, max, min;
    static int[] nums, operators;
    
    static void input() {
        N = scan.nextInt();
        nums = new int[N + 1];
        operators = new int[5];
        
        for (int i = 1; i <= N; i++) nums[i] = scan.nextInt();
        for (int i = 1; i <= 4; i++) operators[i] = scan.nextInt();
        
        max = Integer.MIN_VALUE;
        min = Integer.MAX_VALUE;
    }
    
    // 피연산자 2개와 연산자가 주어졌을 때, 값을 계산해주는 함수
    static int calculate(int operand1, int operator, int operand2) {
        // value, operator, int[n + 1]
        if (operator == 1) {
            return operand1 + operand2;
        } else if (operator == 2) {
            return operand1 - operand2;
        } else if (operator == 3) {
            return operand1 * operand2;
        } else {
            return operand1 / operand2;
        }
    }
    
    // 완전 탐색을 위한 재귀 함수
    static void rec_func(int k, int value) {
        if (k == N) {
            min = Math.min(min, value);
            max = Math.max(max, value);
        } else {
            for (int c = 1; c <= 4; c++) {
                if (operators[c] >= 1) {
                    operators[c]--;
                    rec_func(k + 1, calculate(value, c, nums[k + 1]));
                    operators[c]++;
                }
            }
        }
    }
    
    public static void main(String[] args) {
        input();
        
        rec_func(1, nums[1]);
        sb.append(max).append('\n').append(min);
        System.out.println(sb.toString());       
    }
    
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        
        public FastReader(String s) throws FileNotFoundException{
            br = new BufferedReader(new FileReader(new File(s)));
        }
        
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
        
        double nextDouble() {
            return Double.parseDouble(next());
        }
        
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
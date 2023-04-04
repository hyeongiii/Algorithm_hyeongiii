import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static int num;
    static double sum = 0;
    static double[] score;
    
    static void input() {
        num = scan.nextInt();
        score = new double[num];
        
        for(int i = 0; i < num; i++) {
            score[i] = scan.nextDouble();
        }
    }
    
    static double solution(double[] score, int num) {
        // 최댓값 찾기
        double max = 0;
        for(int i = 0; i < num; i++) {
            if(score[i] > max) {
                max = score[i];
            }
        }
        
        // 점수를 다시 계산하면서 점수의 합계 구하기
        for(int i = 0; i < num; i++) {
            sum += (score[i] / max * 100);
        }
        
        // 평균 반환
        return sum / num;
    }
    
    public static void main(String[] args) {
        input();
        
        System.out.println(solution(score, num));
    }
    
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        
        public FastReader(String s) throws FileNotFoundException {
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
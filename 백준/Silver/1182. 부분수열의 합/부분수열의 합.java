import java.io.*;
import java.util.*;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static FastReader scan = new FastReader();
    
    static int N, S, ans;
    static int[] nums;
    
    static void input() {
        N = scan.nextInt();
        S = scan.nextInt();
        nums = new int[N + 1];
        
        for (int i = 1; i <= N; i++) nums[i] = scan.nextInt();
    }
    
    static void rec_func(int k, int value) {
        if (k == N + 1) {
            if (value == S) ans++;
        } else {
            // k번째 원소를 포함시킬지 결정하고 재귀 호출하기
            // Include
            rec_func(k + 1, value + nums[k]);
            // Not Include
            rec_func(k + 1, value);
        }
    }
    
    public static void main(String[] args) {
        input();
        
        rec_func(1, 0);
        if (S == 0) ans -= 1;
        System.out.println(ans);
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
        
        double nextDouble() {
            return Double.parseDouble(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
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
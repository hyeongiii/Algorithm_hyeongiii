import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static int n, ans = 0;
    static String nums;
    
    static void input() {
        n = scan.nextInt();
        nums = scan.next();
    }
    
    static int solution(String nums, int n) {
        for (int i = 0; i < n; i++) {
            ans += Character.getNumericValue(nums.charAt(i));
        }
        return ans;
    }
    
    public static void main(String[] args) {
        input();
        
        System.out.println(solution(nums, n));
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
            } catch(IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
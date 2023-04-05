import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static String word, ans = "";
    
    static void input() {
        word = scan.next();
    }
    
    static String solution(String word) {
        char[] ch = word.toCharArray();
        
        for (int i = 0; i < ch.length; i++) {
            if (ch[i] >= 65 && ch[i] <= 90) {
                ch[i] = (char)(ch[i] + 32);
            } else {
                ch[i] = (char)(ch[i] - 32);
            }
        }
        
        ans = new String(ch);
        return ans;
    }
    
    public static void main(String[] args) {
        input();
        
        System.out.println(solution(word));
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
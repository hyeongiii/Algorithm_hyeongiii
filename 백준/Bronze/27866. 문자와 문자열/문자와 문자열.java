import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static String word;
    static int idx;
    
    public static void input() {
        word = scan.next();
        idx = scan.nextInt();
    }
    
    public static void main(String[] args) {
        input();
        System.out.println(word.charAt(idx - 1));
    }
    
    public static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        
        String next() {
            while(st == null || !st.hasMoreElements()) {
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
    }
}
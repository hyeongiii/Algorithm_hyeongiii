import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static String a, b;
    static int temp = 0;
    
    static void input() {
        a = scan.next();
        b = scan.next();
    }
    
    static int Solution(String a, String b) {
        char[] x = a.toCharArray();
        char[] y = b.toCharArray();
        
        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < y.length; j++) {
                if (x[i] == y[j]) {
                    temp += 2;
                    y[j] = '0';
                    break;
                }
            }
        }
        
        return x.length + y.length - temp;
    }
    
    public static void main(String[] args) {
        input();
        System.out.println(Solution(a, b));
    }
    
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
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
    }
}
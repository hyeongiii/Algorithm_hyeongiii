import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static String word;
    
    static void input() {
        word = scan.next();
    }
    
    static String changeCase(String word) {
        char[] ch = word.toCharArray();
        
        for (int i = 0; i < ch.length; i++) {
            if (ch[i] >= 65 && ch[i] <= 90) {
                ch[i] = (char)(ch[i] + 32);
            } else {
                ch[i] = (char)(ch[i] - 32);
            }
        }
        return new String(ch);
    }
    
    public static void main(String[] args) {
        input();
        
        System.out.println(changeCase(word)); 
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
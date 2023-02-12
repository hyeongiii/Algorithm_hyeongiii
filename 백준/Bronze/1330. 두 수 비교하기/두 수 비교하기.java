import java.util.*;
import java.io.*;

public class Main {
    
    static int n, m;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        if (n > m) {
            System.out.println(">");
        } else if (n == m) {
            System.out.println("==");
        } else {
            System.out.println("<");
        }
    }
}
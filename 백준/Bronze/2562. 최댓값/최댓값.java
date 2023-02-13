import java.util.*;
import java.io.*;

public class Main {
    
    static int n = -1;
    static int idx = -1;
    static int a;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for (int i = 0; i < 9; i++) {
            a = Integer.parseInt(br.readLine());
            if(n < a) {
                n = a;
                idx = i + 1;
            }
        }
        
        System.out.println(n);
        System.out.println(idx);
    }
}
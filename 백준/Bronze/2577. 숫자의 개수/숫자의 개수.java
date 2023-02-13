import java.io.*;
import java.util.*;

public class Main {
    
    static int a, b, c;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        a = Integer.parseInt(br.readLine());
        b = Integer.parseInt(br.readLine());
        c = Integer.parseInt(br.readLine());
        
        int[] arr = new int[10];
        String m = Integer.toString(a * b * c);
        
        for (int i = 0; i < m.length(); i++) {
            arr[m.charAt(i) - 48] += 1;
        }
        
        for (int i = 0; i < 10; i++) {
            System.out.println(arr[i]);
        }
    }
}
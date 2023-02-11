import java.util.*;
import java.io.*;

public class Main {
    
    private static int answer;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        answer = st.countTokens();
        
        System.out.println(answer);
    }
}
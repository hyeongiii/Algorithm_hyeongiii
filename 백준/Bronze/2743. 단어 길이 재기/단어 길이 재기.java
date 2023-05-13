import java.io.*;
import java.util.*;

public class Main {
    static String word;
    static int ans;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        word = br.readLine();
        
        System.out.println(word.length());
    }
}
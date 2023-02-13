import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] data = new char[5][15];
        int max = 0;
        
        for (int i = 0; i < 5; i++) {
            String str = br.readLine();
            if (max < str.length()) {
                max = str.length();
            }
            // char를 2차원 배열에 저장
            for (int j = 0; j < str.length(); j++) {
                data[i][j] = str.charAt(j);
            }
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < max; i++) {
            for (int j = 0; j < 5; j++) {
                // char 배열의 초기값: '\0'
                if(data[j][i] == '\0') continue;
                sb.append(data[j][i]);
            }
        }
        
        System.out.println(sb);
    }
}
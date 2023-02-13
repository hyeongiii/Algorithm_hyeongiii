import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        char[][] ch = new char[5][15];
        int max = -1;

        for (int i = 0; i < 5; i++) {
            String tmp = br.readLine();

            if (max < tmp.length()) {
                max = tmp.length();
            }

            for (int j = 0; j < tmp.length(); j++) {
                ch[i][j] = tmp.charAt(j);
            }
        }

        for (int i = 0; i < max; i++) {
            for (int j = 0; j < 5; j++) {
                if (ch[j][i] == '\0') {
                    continue;
                }
                sb.append(ch[j][i]);
            }
        }

        System.out.println(sb);
    }
}
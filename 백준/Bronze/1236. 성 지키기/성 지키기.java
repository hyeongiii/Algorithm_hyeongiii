import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb;

    static int n, m;
    static boolean[][] castle;

    public static void input() {
        n = scan.nextInt();
        m = scan.nextInt();
        castle = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String temp = scan.next();
            for (int j = 0; j < m; j++) {
                if (temp.charAt(j) == 'X') {
                    castle[i][j] = true;
                } else {
                    castle[i][j] = false;
                }
            }
        }
    }

    public static int calculate(boolean[][] castle) {
        int rowCount = 0;
        int colCount = 0;

        for (int i = 0; i < n; i++) {
            boolean hasGuard = false;
            for (int j = 0; j < m; j++) {
                if (castle[i][j]) {
                    hasGuard = true;
                    break;
                }
            }
            if (!hasGuard) {
                rowCount++;
            }
        }

        for (int j = 0; j < m; j++) {
            boolean hasGuard = false;
            for (int i = 0; i < n; i++) {
                if (castle[i][j]) {
                    hasGuard = true;
                    break;
                }
            }
            if (!hasGuard) {
                colCount++;
            }
        }

        return Math.max(rowCount, colCount);
    }

    public static void main(String[] args) {
        input();
        System.out.println(calculate(castle));
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
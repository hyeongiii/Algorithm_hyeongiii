import java.util.*;
import java.io.*;

public class Main {
    static FastReader scan = new FastReader();
    static String a, b;

    public static void input() {
        a = scan.next();
        b = scan.next();
    }

    public static int solution(String a, String b) {
        StringBuilder n = new StringBuilder("");
        StringBuilder m = new StringBuilder("");
        for (int i = 2; i >= 0; i--) {
            n.append(a.charAt(i));
            m.append(b.charAt(i));
        }

        int tmpA = Integer.parseInt(n.toString());
        int tmpB = Integer.parseInt(m.toString());

        return Math.max(tmpA, tmpB);
    }

    public static void main(String[] args) {
        input();
        System.out.println(solution(a, b));
    }

    public static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
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
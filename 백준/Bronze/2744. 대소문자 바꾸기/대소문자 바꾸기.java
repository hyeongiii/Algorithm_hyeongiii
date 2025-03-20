import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        String output = "";
        
        for(char x : input.toCharArray()) {
            if(Character.isLowerCase(x)) {
                output += Character.toUpperCase(x);
            } else {
                output += Character.toLowerCase(x);
            }
        }

        System.out.println(output);
    }
}

// Scanner 이용 방법

import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        // Scanner 사용
        Scanner sc = new Scanner(System.in);
        
        // next-- 의 기본 구분자 : 공백 -> 공백으로 입력값이 주어지기 때문에 nextInt() 사용 가능
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        System.out.println(a + b);
        // close() : Scanner 객체를 닫는 메서드, System.in 도 함께 닫힌다. (사용하지 않는 입력, 출력 스트림을 더이상 받지 않기 위해 닫아준다.)
        //           Scanner 객체를 여러개 생성하여도 System.in은 공유하기 때문에 한 곳에서 close() 메서드를 사용하면 다른 객체에서도 입력을 받을 수 없다.
        //           명시적으로 적지 않아도 Closeable 인터페이스가 호출되어 자동으로 닫아주지만, 명시적으로 적어주는 것이 더 좋다. 
        sc.close();
    }
}

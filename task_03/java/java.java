import java.util.Scanner;

public class java {
    public static boolean check(int num) {
        if (num == 2) {
            return true ;
        }
        else {
            for (int i = 2; i<num;i++){
                if (num % i == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
  
        int num = sc.nextInt();
        if (num <2) {
            System.out.println("prime number not defied");
        }
        else{
        for (int j = 2 ;j<=num;j++) {
            if (check(j)) {
                System.out.println("prime number "+ j);

            }
        }            
        }




    }

}      
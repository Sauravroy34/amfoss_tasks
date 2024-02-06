import java.util.Scanner;

public class PrimeNumbers {
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false; // 0 and 1 are not prime numbers
        }
        
        for (int i = 2; i * i <= num; ++i) {
            if (num % i == 0) {
                return false; // num is divisible by i, so it's not a prime
            }
        }
        
        return true; // num is prime
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number (n): ");
        int n = scanner.nextInt();
        scanner.close();
        
        System.out.println("Prime numbers up to " + n + ":");
        
        for (int i = 2; i <= n; ++i) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
        
        System.out.println();
    }
}


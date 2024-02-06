#include <iostream>

bool is_prime(int num) {
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

int main() {
    int n;
    std::cout << "Enter a number (n): ";
    std::cin >> n;

    std::cout << "Prime numbers up to " << n << ":\n";

    for (int i = 2; i <= n; ++i) {
        if (is_prime(i)) {
            std::cout << i << " ";
        }
    }

    std::cout << "\n";

    return 0;
}


#include <stdio.h>
#include <stdbool.h>

bool check(int num) {
    if (num == 2) {
        return true; 
    }
    
    for (int i = 2;  i < num; ++i) {
        if (num % i == 0) {
            return false; 
        }
    }
    
    return true; 
}

int main() {
    int n;
    printf("Enter a number (n): ");
    scanf("%d", &n);
    if (n <2) {
        printf("prime number not defined for this range %d",n);
    }
    
    
    for (int i = 2; i <= n; ++i) {
        if (check(i)) {
            printf("prime number %d:", i);
            printf("\n");
        }
    }
    
    
    
    return 0;
}


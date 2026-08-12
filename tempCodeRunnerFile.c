#include <stdio.h>

int main() {
    int n;
    printf("Enter the number : ");
    scanf("%d",&n);
 
    for(int i = 1;i<=10;i++){
        int prod=i*n;
        printf("%d x %d = %d\n",n,i,prod);
    }
    return 0;
}
#include <stdio.h>
int main(){
    int A, B;
    scanf("%d %d", &A, &B);
    int n = A / 100;
    int m = B / 100;
    int k = A % 10;
    int l = B % 10;
    int a, b;
    a = k*100 + (A-n*100-k) + n;
    b = l*100 + (B-m*100-l) + m;
    if (a>b){
        printf("%d", a);
    } else {
        printf("%d", b);
    }
    return 0;

}

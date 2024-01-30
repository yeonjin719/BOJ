#include <stdio.h>

int main(){
    int a,b,c;
    do {
        scanf("%d %d %d", &a, &b, &c);
        if (a+b+c ==0){
            break;
        } 
        if (a > b && a > c){
            if (a >= b+c){
                printf("Invalid\n");
                continue;;
            }
        } else if (b > a && b > c){
            if (b >= a+c){
                printf("Invalid\n");
                continue;;
            }
        } else if (c > a && c > b) {
            if (c >= b+a){
                printf("Invalid\n");
                continue;;
            }
        }
        if (a == b && a == c && b == c){
            printf("Equilateral\n");
        } else if (a==b || b==c || a==c){
            printf("Isosceles\n");
        } else {
            printf("Scalene\n");
        }
    }  while (a+b+c != 0);
    return 0;
}

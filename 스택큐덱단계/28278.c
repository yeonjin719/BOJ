#include <stdio.h>
int main(){
    int N;
    int order;
    scanf("%d", &N);
    int stack[N];
    int X;
    int cnt = 0;
    for (int i=0; i<N; i++){
        scanf("%d", &order);
        switch (order){
            case 1:
                scanf("%d", &X);
                stack[cnt] = X;
                cnt += 1;
                break;
            case 2:
                if (cnt > 0){
                    printf("%d", stack[cnt-1]);
                    printf("\n");
                    stack[cnt-1] = 0;
                    cnt -= 1;
                } else {
                    printf("-1");
                    printf("\n");
                }
                break;
            case 3:
                printf("%d", cnt);
                printf("\n");
                break;
            case 4:
                if (cnt == 0){
                    printf("1");
                    printf("\n");
                } else {
                    printf("0");
                    printf("\n");
                }
                break;
            case 5:
                if (cnt > 0){
                    printf("%d", stack[cnt-1]);
                    printf("\n");
                } else {
                    printf("-1");
                    printf("\n");
                }
                break;
            default:
                break;
        }
    }
    return 0;
}

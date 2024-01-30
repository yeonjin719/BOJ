#include <stdio.h>
int main(){
    int N;
    int d[1000000] = {0, };
    scanf("%d", &N);
    d[1] = 0;
    d[2] = 1;
    d[3] = 1;
    for (int i=4; i<N+1; i++){
        d[i] = d[i-1]+1;
        if(i%2==0){
            d[i] = (d[i] < d[i/2]+1) ? (d[i]) :(d[i/2]+1);
        }
        if(i%3==0){
            d[i] = (d[i] < d[i/3]+1) ? (d[i]) :(d[i/3]+1);
        }
    }
    printf("%d", d[N]);
}

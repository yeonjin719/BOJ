#include <stdio.h>
int N;
int answer = 0;
int arr[101][101];
int main(){
    scanf("%d", &N);
    int x;
    int y;
    for (int l = 0; l < N; l++){
        scanf("%d %d", &x, &y);
        for (int i = x; i < 10 + x; i ++){
            for (int j = y; j < 10 + y; j++){
                arr[i][j] = 1;
            }
        }
    }
    for (int i = 0; i<101; i++){
        for (int j=0; j<101; j++){
            answer += arr[i][j];
        }
    }
    printf("%d", answer);
    return 0;
}

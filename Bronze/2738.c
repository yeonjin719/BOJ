#include <stdio.h>
int N;
int M;
int main(){
    scanf("%d %d", &N, &M);
    int matrix[N][M];
    int matrix2[N][M];
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            scanf("%d", &matrix[i][j]);
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            scanf("%d", &matrix2[i][j]);
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            printf("%d ", matrix[i][j]+matrix2[i][j]);
        }
        printf("\n");
    }
    return 0;
}

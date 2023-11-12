#include <stdio.h>

int main(){
    int arr[9][9] = {0, };
    int max = 0;
    int x, y;
    for (int i=0; i<9; i++){
        for (int j=0; j<9; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    for (int i=0; i<9; i++){
        for (int j=0; j<9; j++){
            if (max <= arr[i][j]) {
                max = arr[i][j];
                x = j;
                y = i;
            }
        }
    }
    printf("%d\n", max);
    printf("%d %d", y+1, x+1);
}
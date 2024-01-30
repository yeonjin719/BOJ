#include <stdio.h>
int main(){
    int T;
    scanf("%d", &T);
    for (int i=0; i<T; i++){
        int R;
        char S[21];
        int len = 0;
        scanf("%d %s", &R, S);
        while (S[len] != '\0'){
            len++;
        }
        for (int j=0; j<len; j++){
            for (int k=0; k<R; k++){
                printf("%c", S[j]);
            }
        }
        printf("\n");
    }
    return 0;
}

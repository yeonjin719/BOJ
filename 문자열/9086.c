#include <stdio.h>
int main(){
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++){
        char word[1001];
        int len=0;
        scanf("%s", word);
        while (word[len]!='\0'){
            len++;
        }
        printf("%c%c\n", word[0], word[len-1]);
    }
    return 0;
}
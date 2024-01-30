#include <stdio.h>
int main(){
    char word[1001];
    int N;
    scanf("%s", word);
    scanf("%d", &N);
    printf("%c", word[N-1]);
    return 0;
}

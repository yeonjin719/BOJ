#include <stdio.h>
int main(){
    char word[101];
    scanf("%s", word);
    int len = 0;
    while (word[len] != '\0'){
        len ++;
    }
    printf("%d", len);
    return 0;
}

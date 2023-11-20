#include <stdio.h>
int main(){
    int word[26] = {0, };
    char w;
    int max = 0;
    int sc_max = 0;
    int max_index;
    while (1){
        scanf("%c", &w);
        if (w<91 && w>64){
            word[w-65] += 1;
        } else if (w > 96 && w<123) {
            word[w-97] += 1;
        } else {
            break;
        }
    }
    for (int i=0; i<26; i++){
        if (max <= word[i]){
            sc_max = max;
            max = word[i];
            max_index = i;
        }
    }
    if (sc_max == max){
        printf("?");
    } else {
        printf("%c", max_index+65);
    }
    return 0;
}
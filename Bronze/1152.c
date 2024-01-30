#include <stdio.h>
int main(){
    char alpha[1000001] = {"0", };
    int cnt = 0;
    scanf("%[^\n]s",alpha);
    if (alpha[0] != ' ') cnt++;
    for (int i=0; i<1000001; i++){
        if (alpha[i] == 0) break;
        if (alpha[i] != ' ' && alpha[i-1] == ' '){
            cnt += 1;
        }
        
    }
    printf("%d", cnt);
    return 0;
}

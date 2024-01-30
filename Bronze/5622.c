#include <stdio.h>
int main(){
    char c[16];
    int ans = 0;
    scanf("%s", c);
    for (int i=0; i<16; i++){
        if (c[i] < 65){
            continue;
        }
        else if (c[i] < 68){
            ans += 3;
        } else if (c[i] < 71) {
            ans += 4;
        } else if (c[i] < 74) {
            ans += 5;
        } else if (c[i] < 77) {
            ans += 6;
        } else if (c[i] < 80) {
            ans += 7;
        } else if (c[i] < 84) {
            ans += 8;
        } else if (c[i] < 87) {
            ans += 9;
        } else if (c[i] < 91) {
            ans += 10;
        } else {
            continue;
        }
    }
    printf("%d", ans);
    return 0;
}

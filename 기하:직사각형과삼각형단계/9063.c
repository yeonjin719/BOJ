#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    int maxX=-10000;
    int minX=10000;
    int maxY=-10000;
    int minY=10000;
    int x, y;
    for (int i=0; i<n; i++){
        scanf("%d %d", &x, &y);
        if (x >= maxX){
            maxX = x;
        }
        if (x <= minX){
            minX = x;
        }
        if (y >= maxY){
            maxY = y;
        }
        if (y <= minY){
            minY = y;
        }
    }
    printf("%ld", (maxX-minX)*(maxY-minY));
    return 0;
}
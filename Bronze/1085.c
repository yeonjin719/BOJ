#include <stdio.h>
int main(){
    int x,y,w,h;
    int xl,yl,zxl,zyl;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    xl = (w-x>0) ? w-x:(w-x)*(-1);
    yl = (h-y>0) ? h-y:(h-y)*(-1);
    zxl = x;
    zyl = y;
    if (xl <= yl && xl <= zxl && xl <=zyl){
        printf("%d", xl);
    } else if (yl <= xl && yl <= zxl && yl <=zyl){
        printf("%d", yl);
    } else if (zxl <= xl && zxl <= yl && zxl <=zyl){
        printf("%d", zxl);
    } else {
        printf("%d", zyl);
    }

}

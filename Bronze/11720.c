#include <stdio.h>
int main(){
    int N;
    scanf("%d", &N);
    int arr[N];
    int ans = 0;
    for (int i=0; i<N; i++){
        scanf("%1d", &arr[i]);
    }
    for (int i=0; i<N; i++){
        ans += arr[i];
    }
    printf("%d", ans);
    return 0;
}

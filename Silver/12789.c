#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int nowLine[N];
    int answer[N + 1];
    for (int i = 0; i < N; i++) {
        scanf("%d", &nowLine[i]);
    }
    int index = 0;
    int cnt = 1;
    int line[N + 1];
    int find = 0;
    while (1) {
        if (answer[N] == N) {
            printf("Nice");
            return 0;
        }
        if (nowLine[find] == cnt) {
            answer[cnt] = cnt;
            cnt += 1;
            find += 1;
        } else if (index > 0 && line[index - 1] == cnt) {
            answer[cnt] = cnt;
            cnt += 1;
            index -= 1;
        } else if (index == 0 || (index > 0 && line[index - 1] > nowLine[find])) {
            line[index] = nowLine[find];
            index += 1;
            find += 1;
        } else {
            printf("Sad");
            return 0;
        }
    }
    return 0;
}

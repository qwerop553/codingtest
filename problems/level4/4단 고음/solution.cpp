#include <string>
#include <vector>
using namespace std;

int cnt;

// cur까지 내려오는 동안 '*'를 최대 몇 번 더 되돌릴 수 있나 (3^r <= cur 인 최대 r)
int maxStars(long long cur) {
    int r = 0; long long p = 1;
    while (p * 3 <= cur) { p *= 3; r++; }
    return r;
}

// cur: 현재 음높이, pend: 아직 짝지을 '*'를 못 찾은 '+' 개수
void dfs(long long cur, int pend) {
    if (cur == 1) { if (pend == 0) cnt++; return; }
    if (pend > 2 * maxStars(cur)) return;                // 가지치기
    if (cur % 3 == 0 && pend >= 2) dfs(cur / 3, pend - 2);  // '*' 되돌리기
    dfs(cur - 1, pend + 1);                                 // '+' 되돌리기
}

int solution(int n) {
    cnt = 0;
    dfs(n, 0);
    return cnt;
}
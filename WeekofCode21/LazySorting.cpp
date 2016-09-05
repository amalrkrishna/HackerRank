/* __author__ = "Amal Krishna R" */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    int n, a[110];
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
    bool flag = true;
    for (int i = 2; i <= n; i++) if (a[i] < a[i - 1]) flag = false;
    if (flag) {
        printf("0.000000\n");
        return 0;
    }
    long long fac[20];
    fac[0] = 1;
    for (int i = 1; i < 20; i++) fac[i] = fac[i - 1] * i;
    sort(a + 1, a + n + 1);
    long long ans = fac[n];
    int i = 1;
    while (i <= n) {
        int j = i;
        while (j <= n && a[i] == a[j]) j++;
        ans /= fac[j - i];
        i = j;
    }
    printf("%.6f\n", (double)ans);
    return 0;
}


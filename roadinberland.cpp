#include <bits/stdc++.h>
#define ll long long

using namespace std;

void test_case() {
    int N;
    scanf("%d", &N);

    ll confMatrix[N][N];

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            scanf("%lld", &confMatrix[i][j]);
        }
    }

    int R;
    scanf("%d", &R);

    for (int r = 0; r < R; ++r) {
        int from, to;
        ll len;
        scanf("%d %d %lld", &from, &to, &len);

        if (confMatrix[from-1][to-1] > len) {
            confMatrix[from-1][to-1] = len;
            confMatrix[to-1][from-1] = len;
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                ll temp = confMatrix[i][from-1] + confMatrix[from-1][j];
                if (confMatrix[i][j] > temp) {
                    confMatrix[i][j] = temp;
                }
            }
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                ll temp = confMatrix[i][to-1] + confMatrix[to-1][j];
                if (confMatrix[i][j] > temp) {
                    confMatrix[i][j] = temp;
                }
            }
        }

        ll sum = 0;

        for (int i = 0; i < N; ++i) {
            for (int j = i+1; j < N; ++j) {
                sum += confMatrix[i][j];
            }
        }

        cout << sum << endl;

    }
}


int main() {
    test_case();
    return 0;
}

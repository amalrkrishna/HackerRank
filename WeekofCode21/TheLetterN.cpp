/* __author__ = "Amal Krishna R" */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class pt {
public:
    int x;
    int y;
    int index;
    pt(int X, int Y, int i) {
        x = X; y = Y; index = i;
    }
};

bool comp(pt a, pt b) {
    if ((a.x > 0) && (b.x <= 0)) return a.y >= 0;
    if ((a.x <= 0) && (b.x > 0)) return b.y < 0;
    if ((a.y >= 0) && (b.y < 0)) return true;
    if ((a.y < 0) && (b.y >= 0)) return false;
    return a.y * b.x < a.x * b.y;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N; cin >> N;
    vector<pt> points;
    int x; int y;
    for (int i = 0; i < N; ++i) {
        cin >> x >> y;
        points.push_back(pt(x, y, i));
    }
    
    vector< vector< long long int > > below(N);
    for (int i = 0; i < N; ++i) below[i] = vector<long long int>(N);
    
    for (int i = 0; i < N; ++i) {
        vector<pt> other;
        for (int j = 0; j < N; ++j) {
            if (j == i) continue;
            other.push_back(pt(points[j].x - points[i].x, points[j].y - points[i].y, points[j].index));
        }
        
        sort(other.begin(), other.end(), comp);
        
        for (int j = 0; j < N-1; ++j) {
            pt ninety(other[j].y, -other[j].x, -1);
            auto first = lower_bound(other.begin(), other.end(), ninety, comp);
            auto last = lower_bound(other.begin(), other.end(), other[j], comp);
            if ((other[j].x > 0) && (other[j].y >= 0)) {
                below[i][other[j].index] = last - other.begin();
                below[i][other[j].index] += other.end() - first;
            }
            else {
                below[i][other[j].index] = last - first;
            }
        }
    }
    
    long long int Ns = 0;
    
    for (int i = 1; i < N; ++i) {
        for (int j = 0; j < i; ++j) {
            Ns += below[i][j] * below[j][i];
        }
    }
    
    cout << Ns << endl;
    
    return 0;
}


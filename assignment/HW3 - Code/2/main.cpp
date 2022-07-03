#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1e5+100, M = 2e4+100;

vector<int> pos[M];
int ans[N], a[N];

int main() 
{
    int n;
    cin >> n;
    for(int i=0 ; i<n ; i++)
    {
        int d;
        cin >> d;
        pos[d].push_back(i);
        a[i] = d;
    }
    for(int i=0 ; i<M ; i++)
    {
        for(auto j: pos[i])
        {
            if(j && a[j-1] < a[j])
                ans[j] = max(ans[j], ans[j-1]);
            if(j<n-1 && a[j+1] < a[j])
                ans[j] = max(ans[j], ans[j+1]);
            ans[j] ++;
        }
    }
    long long out=0;
    for(int i=0 ; i<n ; i++)
        out += ans[i];
    cout << out << "\n";
    return 0;
}
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() 
{
    int n, u;
    cin >> n;
    cin >> u;

    vector<pair<int, int>> vec;

    for(int i=0 ; i<n ; i++)
    {
        int x, y;
        cin >> x >> y;
        vec.emplace_back(x, y);
    }

    sort(vec.begin(), vec.end(), [](pair<int, int> A, pair<int, int> B){
        bool negA = A.second < 0;
        bool negB = B.second < 0;
        if(!negA && !negB)
            return A.second < B.second;
        if(!negA)
            return false;
        if(!negB)
            return true;
        return A.first + A.second < B.first + B.second;
    });

    while(!vec.empty())
    {
        int it = vec.size()-1;
        while(vec[it].first > u && it >= 0)
            it --;

        if(it == -1)
        {
            cout << "NO\n";
            return 0;
        }
        u += vec[it].second;
        vec.erase(vec.begin() + it);
    }
    if(u < 0)
    {
        cout << "NO\n";
        return 0;
    }
    cout << "YES\n";
    return 0;
}
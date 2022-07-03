#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll solve(string s)
{
    vector<ll> dp(s.length()+1);
    if(s[0] == '0') dp[0] = 1;
    for(int i = 1; i <= s.length(); i++)
    {
        dp[i] = INT_MAX;
        for(int j = 1; j <= i; j++)
        {
            if(s[j-1] == '0' && i-j != 0)
            {
                continue;
            }

            ll num = stoll(s.substr(j-1, i-j+1), nullptr, 10);

            if(num >= 0 && num < 256)
            {
                cout<<num<<"\n";
                dp[i] = min(dp[i], dp[j-1]+1);
            }
        }
     }

    for (ll l: dp)
        cout<<l<<' ';
    cout<<"\n";

    if(dp[s.length()] == INT_MAX)
    {
        return -1;
    }
    else
    {
        return dp[s.length()];
    }
}

int main()
{
    string s;
    cin>>s;
    cout<<solve(s);
}
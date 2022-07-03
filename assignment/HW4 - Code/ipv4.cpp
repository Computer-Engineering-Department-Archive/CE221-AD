#include<bits/stdc++.h>
using namespace std;

// string
string s;
// i, j
int i = 0;
int j = 0;
// counter
int counter = 1;
// base and dp
string base = "";
vector<string> dp;

using namespace std;
typedef long long ll;

//ll solve(string s)
//{
//    vector<ll> dpa(s.length() + 1);
//    if(s[0] == '0') dpa[0] = 1;
//    for(int i = 1; i <= s.length(); i++)
//    {
//        dpa[i] = INT_MAX;
//        for(int j = 1; j <= i; j++)
//        {
//            if(s[j-1] == '0' && i-j != 0)
//            {
//                continue;
//            }
//
//            ll num = stoll(s.substr(j-1, i-j+1), nullptr, 10);
//
//            if(num >= 0 && num < 256)
//            {
//                cout<<num<<"\n";
//                dpa[i] = min(dpa[i], dpa[j - 1] + 1);
//            }
//        }
//    }
//
//    for (ll l: dpa)
//        cout<<l<<' ';
//    cout<<"\n";
//
//    if(dpa[s.length()] == INT_MAX)
//    {
//        return -1;
//    }
//    else
//    {
//        return dpa[s.length()];
//    }
//}


void decode(string base, int i, int j, int counter) {
    if (i == j+1)
    if (counter == 5)
        dp.push_back(base.substr(1));

    for (int k = i; k < i+3; k++) {
        if (k > j)
            break;

        string temp = s.substr(i, k - i + 1);

        if (s[i] == '0')
        if (temp.size() > 1)
            return;

        if (stol(temp) >= 0 && stol(temp) < 256)
            decode(base + '-' + temp, k + 1, j, counter + 1);
        else
            return;
    }
}

int main()
{
    cin>>s;

    j = s.length() - 1;
    decode(base, i, j, counter);

	cout<<dp.size();
}

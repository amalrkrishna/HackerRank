/* __author__ = "Amal Krishna R" */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

typedef long long ll;

ll dec(ll n)
{
    ll decimal=0, i=0, rem;
    while (n!=0)
    {
        rem = n%10;
        n/=10;
        decimal += rem*pow(2,i);
        ++i;
    }
    return decimal;
}

int main() {
    int n,m;
    cin>>n>>m;
    vector<pair<int,pair<ll,ll> > > queries;
    ostringstream os;
    for(int i=0;i<m;i++){
        int q;
        cin>>q;
        if(q == 1){
            ll x,mask;
            cin>>x>>mask;
            queries.push_back(make_pair(1,make_pair(dec(mask),x)));
        }else if(q == 2){
            ll x,mask;
            cin>>x>>mask;
            queries.push_back(make_pair(2,make_pair(dec(mask),x)));
         }else{
            ll mask;
            cin>>mask;
            mask = dec(mask);
            ll ans = 0;
            for(int i=queries.size()-1;i>=0;i--){
                if((mask|queries[i].second.first) == queries[i].second.first){
                    if(queries[i].first == 1){
                        ans = ans ^ queries[i].second.second;
                        break;
                    }else{
                        ans = ans ^ queries[i].second.second;
                    }
                }
                    
            }
            os<<ans<<endl;
        }
    }
    cout<<os.str();
    return 0;
}


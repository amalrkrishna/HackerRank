/* __author__ = "Amal Krishna R" */

#include <bits/stdc++.h>
 
using namespace std;
#define ll long long
const int maxn = (int)2e5 + 100;
int n, pre_l, sobjj;
int counts[maxn], start[maxn], p[maxn], c[maxn], str_pold[maxn], str_polC[maxn];
 
int pos[maxn], lcp[maxn], curLCP;
 
ll para_we[6][maxn], penta_hh[6][maxn], moduluss[6];
  
void calc_sa(string s)
{
	s.push_back('#');
	n = s.size();
	for (int i = 0; i < 255; i++) counts[i] = 0;
	for (int i = 0; i < n; i++)
		counts[(int)s[i]]++;
 
	start[0] = 0;
	for (int i = 1; i < maxn; i++)
		start[i] = start[i - 1] + counts[i - 1];
	for (int i = 0; i < maxn; i++) p[i] = 0, c[i] = 0, str_pold[i] = 0, str_polC[i] = 0;
	for (int i = 0; i < n; i++) 
		p[start[(int)s[i]]++] = i;
 
	c[p[0]] = 0;
	sobjj = 1;
	for (int i = 1; i < n; i++) {
		if (s[p[i - 1]] != s[p[i]])
			sobjj++;
		c[p[i]] = sobjj - 1;	
	}
 
	pre_l = 1;
	while (pre_l < n) {
	    swap(p, str_pold);
		for (int i = 0; i < n; i++)
		   	str_pold[i] = (str_pold[i] - pre_l + 2 * n) % n;
	    for(int i=0;i< sobjj;i++)
	    	counts[i] = 0;
	    for (int i = 0; i < n; i++)
	    	counts[c[i]]++;	
 
	    start[0] = 0;
	    for (int i = 1; i < sobjj; i++)	
	    	start[i] = start[i - 1] + counts[i - 1];
 
	    for (int i = 0; i < n; i++)
	    	p[start[c[str_pold[i]]]++] = str_pold[i];
 
	    swap(c, str_polC);
	    sobjj = 1;
	    c[p[0]] = 0;
	    for (int i = 1; i < n; i++) {
	    	if (str_polC[p[i - 1]] != str_polC[p[i]] || str_polC[(p[i - 1] + pre_l) % n] != str_polC[(p[i] + pre_l) % n])
	    		sobjj++;
	    	c[p[i]] = sobjj - 1;
	    }
 
	    pre_l <<= 1;
	}
 
	int lf = 0;
	for(int i = 1; i <= n + 1; i++)
		if (i == n || c[p[i - 1]] != c[p[i]]) {
			int rg = i;
			sort(p + lf, p + rg);
			reverse(p + lf, p + rg);			
			lf = i;
		}    
	for (int i = 0; i < n; i++)
		pos[p[i]] = i;
 
	curLCP = 0;
	for (int i = 0; i < n; i++) {
		int j = pos[i];
		if (curLCP > 0)
			curLCP--;
 
		if (j == n - 1) {
			lcp[j] = -1;
			curLCP = 0;
		} else {
			int k = p[j + 1];
			while (curLCP < n && s[(i + curLCP) % n] == s[(k + curLCP) % n])
				curLCP++;
			lcp[j] = curLCP;
		}		
	}
}
 

void func_ha(int id, string x)
{
	penta_hh[id][0] = x[0];
	for (int i = 1; i < (x.size()); i++)
	   penta_hh[id][i] = (penta_hh[id][i-1] * para_we[id][1] + x[i]) % moduluss[id];
}
 
ll ss_h(int id, int l, int r)
{
	return (penta_hh[id][r] - (l == 0? 0 : penta_hh[id][l-1] * para_we[id][r-l+1]) % moduluss[id] + moduluss[id]) % moduluss[id];
}
 
int lef_weight[maxn], right_weight[maxn];
 
string rev(string str1)
{
	string q = str1;
	reverse(q.begin(), q.end());
	return q;
}
string bestS = "";
 
string solve(string str1, string str2)
{
	moduluss[0] = moduluss[1] = (ll)1e9 + 7ll;
	moduluss[2] = moduluss[3] = (ll)1e9 + 9ll;
	moduluss[4] = moduluss[5] = (ll)1e9 + 9ll;
 
	for (int id = 0; id < 6; id++)
	{
		para_we[id][0] = 1ll;
		para_we[id][1] = 337ll;
		for (int i = 1; i <= (str1.size()) + (str2.size()) + 3; i++) para_we[id][i] = para_we[id][i-1] * para_we[id][1] % moduluss[id];
	}

	func_ha(0, str2);
	func_ha(1, rev(str2));
	func_ha(2, str2);
	func_ha(3, rev(str2));
 
	calc_sa(rev(str1) + "$" + str2);
	int startnn = (str1.size()) + 1;
	lef_weight[0] = 0;
	for (int i = 1; i < (str1.size()) + (str2.size()) + 2; i++)
	{
		if (p[i] >= startnn && p[i-1] < startnn) 
		lef_weight[i] = lcp[i-1];
		else if (p[i] >= startnn && p[i-1] >= startnn)
		lef_weight[i] = min(lcp[i-1], lef_weight[i-1]);
		else lef_weight[i] = 0;
	}
	right_weight[(str1.size())+(str2.size())+1] = 0;
	for (int i = (str1.size())+(str2.size()); i >= 0; i--)
	{
		if (p[i] >= startnn && p[i+1] < startnn) 
            right_weight[i] = lcp[i];
		else if (p[i] >= startnn && p[i+1] >= startnn)
            right_weight[i] = min(lcp[i], right_weight[i+1]);
		else
            right_weight[i] = 0;
	}
	
	int bestLen = 0;
	bestS = "";
	for (int center = 0; center < (str2.size()); center++)
	{
	   for (int shift = 0; shift < 2; shift++)
	   {
		   
		   if (center - shift < 0) continue;
		   int lb = 1;
           int len11=str2.size();
		   int rb = min( len11-center, center + 1 - shift);
		   int res = -1;
		   while (lb <= rb)
		   {
			   int mid = (lb + rb) / 2;
			   int rightL = center, rightR = center + mid - 1;
			   int leftL = center - shift, leftR = center - shift - mid + 1;
			   leftL = (str2.size()) - 1 - leftL;
			   leftR = (str2.size()) - 1 - leftR;
 
			   if (ss_h(0, rightL, rightR) == ss_h(1, leftL, leftR)
			      && ss_h(2, rightL, rightR) == ss_h(3, leftL, leftR))
			   {   
				   res = mid;
				   lb = mid + 1;
			   } else rb = mid - 1;
		   }
		   if (res == -1) continue;
		   for (int id = 0; id < 2 && res >= 0 ; res--, id++)
		   {
				int len = res * 2 - (1 - shift);
				int st = center + res;
 
				int saPos = pos[st + startnn];
				int corrLen = max(right_weight[saPos], lef_weight[saPos]);
				if (corrLen == 0) continue;
				if (corrLen*2 + len == bestLen)
				{
					string tmp = rev(str2.substr(st, corrLen)) + str2.substr(center - shift - res + 1, len + corrLen);
					if (tmp < bestS) bestS = tmp;
				}
				if (corrLen*2 + len > bestLen)
				{
					bestS = rev(str2.substr(st, corrLen)) + str2.substr(center - shift - res + 1, len + corrLen); 
					bestLen = bestS.size();
				}
		   }
 
	    }
	    int saPos = pos[center + startnn];
	    int corrLen = max(right_weight[saPos], lef_weight[saPos]);
	    if (corrLen * 2 == bestLen)
	    {
			string tmp = rev(str2.substr(center, corrLen)) + str2.substr(center, corrLen);
			if (tmp < bestS) bestS = tmp;
		}
		if (corrLen * 2 > bestLen)
		{
			bestS = rev(str2.substr(center, corrLen)) + str2.substr(center, corrLen);
			bestLen = bestS.size();
		}	
 
	  }
	  return bestS;
}
 
 
 
int main()
{
	int q;
	cin >> q;
	while(q--)
	{
		string str1,str2;
		cin >> str1 >> str2;
		string u1 = solve(str1,str2);
		string u2 = solve(rev(str2), rev(str1));
		string res = "";
		if (u1 != "" && u2 != "") 
            res = (make_pair(-(u1.size()), u1) < make_pair(-(u2.size()), u2) ? u1 : u2);
		if (u1 == "")
            res = u2;
		if (u2 == "")
            res = u1;
		if (res == "")
            cout << -1 << endl;
		else cout << res << endl;
	}
	return 0;
}

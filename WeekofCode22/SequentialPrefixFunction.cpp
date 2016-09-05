/* __author__ = "Amal Krishna R" */

#include<bits/stdc++.h>
#define MAX 1000005
using namespace std;
int cnt[MAX],lcs[MAX];
int a[MAX];
int main()
{
    int i,j,n,len=0,x;
    cin>>n;
    for(i=0,j=0;i<n;i++)
    {
        char s[10];
        scanf("%s",s);

        if(s[0]=='+')
        {
            scanf("%d",&x);
            a[j]=x;
            cnt[x]++;
            if(cnt[x]==1)
                lcs[j]=0;
            else
            {
                len=lcs[j-1];
                while(1)
                {
                    if(a[len]==a[j])
                    {
                        len++;
                        lcs[j]=len;
                        break;
                    }
                    else
                    {
                        if(len!=0)
                            len=lcs[len-1];
                        else
                        {
                            lcs[j]=0;
                            break;
                        }
                    }
                }
            }
            printf("%d\n",lcs[j]);
            j++;
        }
        else
        {
            j--;
            cnt[a[j]]--;
            if(j==0)
                printf("0\n");
            else
                printf("%d\n",lcs[j-1]);
        }
    }
    return 0;
}

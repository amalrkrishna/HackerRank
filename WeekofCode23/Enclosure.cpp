#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

#define PI 3.14159265

struct point
{
	double x;
	double y;
};

int main() {
    int n;
    cin>>n;
    std::vector<double> L(n);
    double Lmax = 0.0;
    for(int i=0;i<n;i++)
	{
		cin>>L[i];
		if(L[i]>Lmax)
			Lmax = L[i];
	}
	std::vector<point> points(n);
	points[0].x = 0.0;
	points[0].y = 0.0;
	points[1].x = 0.0;
	points[1].y = L[0];
	double R = Lmax, oldR = 0;
	double low = 0, high = 2*n*R;
	while(true)
	{
		double sumAngle = 0.0;
		for(int i=0;i<n;i++)
			sumAngle+= 2*asin(L[i]/(2*R));
		if(abs(R-oldR)<=0.000000001)
			break;
		else if(sumAngle<2*PI)
		{
			high = R;
			oldR = R;
			R = (low+R)/2.0;
		}	
		else
		{
			low = R;
			oldR = R;
			R = (high+R)/2.0;
		}
	}
	point circumCenter;
	circumCenter.x = sqrt(R*R-L[0]*L[0]/4.0);
	circumCenter.y = L[0]/2.0;
	for(int i=2;i<=n;i++)
	{
		double theta = acos((2.0*R*R - L[i-1]*L[i-1])/(2.0*R*R));
		points[i].x = (points[i-1].x - circumCenter.x)*cos(theta) + (points[i-1].y - circumCenter.y)*sin(theta) + circumCenter.x;
		points[i].y = -(points[i-1].x - circumCenter.x)*sin(theta) + (points[i-1].y- circumCenter.y)*cos(theta)+ circumCenter.y;
	}

	for(int i=0;i<n;i++)
	{
		cout<< (fixed) << setprecision(6) <<points[i].x<<endl;
		cout<< (fixed) << setprecision(6) <<points[i].y<<endl<<endl;
	}
    return 0;
}


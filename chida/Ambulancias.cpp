#include <bits/stdc++.h>
using namespace std;
//#define TxtIO   freopen("Input.txt","r",stdin); freopen("Output.txt","w",stdout);
#define int long long int
#define mk make_pair
#define s second
#define f first


vector<pair<double,double>>ubicaciones;
vector<pair<double,double>>best;
int n;


double diff(pair<double,double> &a,pair<double,double> &b)
{
	return sqrt((a.f-b.f)*(a.f-b.f) + (a.s-b.s)*(a.s-b.s));
}

bool findi(pair<double,double>&b){
	for(auto a:best){
		if(diff(a,b)<=0.02)return 1;
	}
	return 0;
}

double check(pair<double,double> &a)
{
    double d_total=0;
    for(int i=0;i<n;i++){
    	d_total+=diff(a,ubicaciones[i]);
    }
    return d_total;
}

bool sorti(pair<double,double> &a,pair<double,double> &b)
{
	return check(a)<check(b);
}

pair<double,double>vecino(pair<double,double> a)
{
	int x = std::rand();
    double x1 = -0.05 + static_cast<double>(x) / RAND_MAX * (0.1);
    int y = std::rand();
    double y1 = -0.05 + static_cast<double>(y) / RAND_MAX * (0.1);
    a.f+=x1;
    a.s+=y1;
    return a;
}



void solve(int x)
{
    double temperatura = 1;
    double enfriamiento = 0.90;

    double ans = 0;
    pair<double,double>nuevo=ubicaciones[x],mejor;
    
    mejor = nuevo;
    while (temperatura > 1e-6)
    {
        double aux = check(nuevo);
        double dene=ans-aux;
        if (dene || (static_cast<double>(rand()) / RAND_MAX) < exp(dene / temperatura))
        {
            ans = aux;
            mejor = nuevo;
        }
        nuevo = vecino(mejor);
        temperatura *= enfriamiento; 
    }
    if(!findi(mejor))best.push_back(mejor);
}

int32_t main()
{
	//TxtIO;
    srand(time(NULL));
    cout.precision(15);
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    
    cin>>n;
    for(int i=0;i<n;i++){
    	double x,y;
    	cin>>y>>x;
    	ubicaciones.push_back({x,y});
    }
    
    
    int t = n;
    while (t--)
        solve(t);
    
    sort(best.begin(),best.end(),sorti);
    for(int i=0;i<17;i++){
    	cout<<"["<<best[i].f<<","<<best[i].s<<"],\n";
    }
    
    
    return 0;
}

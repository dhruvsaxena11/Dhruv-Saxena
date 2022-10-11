#include<iostream>
using namespace std;
	template <class abc> 
	void square(abc x)
	{
		cout<<"The Square number is"<<endl;
		cout<<x*x<<endl;
	}
int main()
{

	square(12);
	square(10.6);
}

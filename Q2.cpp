#include<iostream>
using namespace std;
class sum
{
	public:
	static int a,b,c;
	public:
		static void su();
};
int sum:: a=0;
int sum:: b=0;
int sum:: c=0;
void sum:: su()
{
	cout<<"enter the numbers";
	cin>>sum::a>>sum::b;
	sum::c=sum::a+sum::b;
	cout<<"the sum is"<<endl<<sum::c;
}
int main()
{
	sum::su();
	return 0;
}

#include<iostream>
using namespace std;
class values
{
	public:
	int a,b;
	void setval()
	{
		cout<<"enter the values"<<endl;
		cin>>a>>b;
	}
		public:
		void swa()
		{
			
			a=a+b;
			b=a-b;
			a=a-b;
			cout<<"the swaped number is"<<endl;
			cout<<a<<endl<<b;
		}
};

int main()
{
	values v2,v3;
	v2.setval();
	v2.swa();
	
	
	return 0;
}

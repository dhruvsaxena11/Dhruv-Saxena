#include<iostream>
using namespace std;
class LIST
{
	public:
	virtual void store()=0;
	virtual void retrieve()=0;
};
class stack : public LIST
{
	public:
		int a[5];
		void store()
		{
			for(int i=4;i>=0;i--)
			{
				cin>>a[i];
			}
		}
		void retrieve()
		{
			for(int i=0;i<5;i++)
			{
				cout<<a[i];
			}
		}
};
class queue : public LIST
{
	public:
	int b[5];
	void store()
	{
		for(int i=0;i<5;i++)
		cin>>b[i];
	}
	void retrieve()
	{
		for(int i=0;i<5;i++)
		cout<<b[i];
	}
};
int main()
{
	stack s;
	queue q;
	s.store();
	s.retrieve();
	return 0;
}

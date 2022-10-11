#include<iostream>
using namespace std;
class rodent
{
	public:
	string a[5];
	void store(int i, string v)
	{
		a[i]=v;
	}	
};
class mouse : public rodent
{
	public:
	void store(int in, string va)
	{
		
		a[in]=va;
		cout<<a[in]<<endl;
	}
};
class gerbil : public rodent
{
	public:
	void store(int ind, string val)
	{
	
		a[ind]=val;
		cout<<a[ind]<<endl;
	}
};
class hamster : public rodent
{
	public:
	void store(int index, string value)
	{
		
		a[index]=value;
		cout<<a[index]<<endl;
	}
};
int main()
{
	mouse m;
	m.store(0,"mouse");
	gerbil g;
	g.store(1,"gerbil");
	hamster h;
	h.store(2,"hamster");
	return 0;
}

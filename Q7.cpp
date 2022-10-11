#include<iostream>
using namespace std;
class bank
{
	public:
	string name;
    string type;
    int bal;
    int with;
    public:
    	void set()
    	{
    		cout<<"Enter The Name :"<<endl;
    		cin>>name;
    		cout<<"Enter the Acccount Type"<<endl;
    		cin>>type;
    		cout<<"Enter the Amount to be deposited"<<endl;
    		cin>>bal;
    		
		}
		void get()
		{
			cout<<"Name"<<endl;
			cout<<name;
			cout<<"Acc type"<<endl;
			cout<<type;
			cout<<"Balance"<<endl;
			cout<<bal;
		}
		
		void withdraw()
		{
		    cout<<"Enter the Ammount to be Withdraw"<<endl;
			cin>>with;
			if(bal==0)
			{
				cout<<"you cannot withdraw the amount"<<endl;
				cout<<"Your Current Balance is 0";
				}	
				else
				{
					cout<<"now current Balance is"<<endl;
					bal=bal-with;
					cout<<bal;
				}
		}
    
};
int main()
{
	bank b1;
	b1.set();
	b1.get();
	string s;
	cout<<"want to withdraw Money ?"<<endl;
	cin>>s;
	if(s=="yes")
	{
	  	b1.withdraw();	
	}
	return 0;

}

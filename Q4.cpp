
#include<iostream>
using namespace std;
class shape
{
	public:
   virtual void volume()=0;
	float pi=3.14;
	
};
class cone : public shape
{
	public:
		float r,h;
		public:
		void volume()
		{
			cout<<"vol of cone"<<endl;
			cin>>h>>r;
			float vol;
			vol=0.33*pi*r*r*h;
			cout<<vol;
		
			
			
		}
 };
 class sphere : public shape
 {
 	public:
 		float q;
 		public:
 		void volume ()
 		{
 			cout<<"vol of sphere"<<endl;
 			cin>>q;
 			float vo;
 			vo=1.33*pi*q*q*q;
 			cout<<vo;
		 }
  };
int main()
{
	
	cone c;
	c.volume();
	sphere s;
	s.volume();
	return 0;
		
 } 

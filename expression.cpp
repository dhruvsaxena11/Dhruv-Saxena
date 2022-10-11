#include <iostream>

using namespace std;

int main()
{
 float a[3];
 string b[2];
 cout<<"Enter the three elements";
 for(int i=0;i<3;i++)
 {
     cin>>a[i];
 }
 cout<<"Enter the two arithematic operators";
 for(int i=0;i<2;i++)
 {
     cin>>b[i];
 }
if(b[0]=="*")
{
    a[0]=a[0]*a[1];
}
if(b[0]=="/")
{
    a[0]=a[0]/a[1];
}
if(b[0]=="+")
{
    a[0]=a[0]+a[1];
}
if(b[0]=="-")
{
    a[0]=a[0]-a[1];
}
if(b[1]=="*")
{
    a[0]=a[0]*a[2];
}
if(b[1]=="/")
{
    a[0]=a[0]/a[2];
}
if(b[1]=="+")
{
    a[0]=a[0]+a[2];
}
if(b[1]=="-")
{
    a[0]=a[0]-a[2];
}
cout<<"the answer is"<<endl;
cout<<a[0];
             

    return 0;
}

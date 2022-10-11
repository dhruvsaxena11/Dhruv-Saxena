#include<iostream>
using namespace std;
class array
{
    public:
    int a[5];
    void set(int index, int val)
    {
        a[index]=val;
         
        
    }
    
};
class test : private array
{
    
    public:
    void setter(int ind, int val)
    {
        set(ind,val);
        
        if(ind>=5)
    {
        cout<<"error";
    }
   
    }
    
};
int main()
{
    test t;
    t.setter(5,3);
    return 0;
}

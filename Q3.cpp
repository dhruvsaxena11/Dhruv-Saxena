#include <iostream>

using namespace std;
class num
{
    private:
    int a;
    int b;
    public:
    void set()
    {
        int x,y;
        cin>>x>>y;
        a=x;
        b=y;
    }
     friend void grt(num);
};
class diff
{
    friend void grt(num);
};
void grt(num n)
{
    if(n.a>n.b)
    cout<<"the greatest number is"<<n.a;
    if(n.a<n.b)
    cout<<"the greatest number is"<<n.b;
}
int main()
{
    num n1;
    n1.set();
    grt(n1);

    return 0;
}

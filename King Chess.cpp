#include <iostream>

using namespace std;

int main()
{
    int x,y;
    cout<<"enter the row wise position"<<endl;
    cin>>x;
    cout<<"enter the column wise position"<<endl;
    cin>>y;
    cout<<"the king can travels in positions"<<endl;
    cout<<"the positions are"<<endl;
    cout<<x+1<<","<<y<<endl<<x-1<<","<<y<<endl;
    cout<<x<<","<<y+1<<endl<<x<<","<<y-1<<endl;
    cout<<"the diagonal posiions are"<<endl;
    cout<<x-1<<","<<y+1<<endl<<x+1<<","<<y-1<<endl;
    cout<<x-1<<","<<y-1<<endl<<x+1<<","<<y+1;

    return 0;
}

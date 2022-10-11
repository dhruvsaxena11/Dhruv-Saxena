#include <iostream>

using namespace std;
class node
{
    public:
    string data;
    node *next;
    node *prev;
};
int main()
{
    node *head, *second, *third, *fourth, *fifth, *sixth, * seventh, * eighth, *ninth, *tenth;
    head= new node();
    second= new node();
    third= new node();
    fourth= new node();
    fifth= new node();
    sixth= new node();
    seventh= new node();
    eighth= new node();
    ninth= new node();
    tenth= new node();
    head->data="Rahul";
    second->data="1234567890";
    third->data="Pradeep";
    fourth->data="1203546987";
    fifth->data="Suryansh";
    sixth->data="25641987351";
    seventh->data="Pranjal";
    eighth->data="12324679850";
    ninth->data="Dhruv";
    tenth->data="2354109875";
    head->next=second;
    second->prev=head;
    third->prev=second;
    second->next=third;
    fourth->prev=third;
    third->next=fourth;
    fifth->prev=fourth;
    fourth->next=fifth;
    sixth->prev=fifth;
    fifth->next=sixth;
    seventh->prev=sixth;
    sixth->next=seventh;
     eighth->prev=seventh;
    seventh->next=eighth;
     ninth->prev=eighth;
     eighth->next=ninth;
     ninth->prev=eighth;
     ninth->next=tenth;
     tenth->next=NULL;
    
    cout<<"My phone Directory is"<<endl<<endl;
    
    while(head!=NULL)
    {
        cout<<head->data<<endl;
        head=head->next;
        
        
    }
    
             

    return 0;
}

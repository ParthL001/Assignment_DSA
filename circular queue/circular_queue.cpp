#include <bits/stdc++.h>
using namespace std;

class CQueue{
    int* arr;
    int currentsize,cap;
    int f,r;
public:
    CQueue(int size){
        cap=size;
        arr = new int[cap];
        f=0;
        currentsize=0;
        r=-1;
    }
    void push(int data){
        if(currentsize==cap){
            cout<<"CQ is full"<<endl;
            return ;
        }
        else{
            r=r+1%cap;
            arr[r]=data;
            currentsize=currentsize+1%cap;
        }
        
        

    }
    int pop(){
        if(currentsize==0){
            cout<<"CQ is empty"<<endl;
            return 0;
        }
        else{
            f=f+1%cap;
            currentsize=currentsize-1%cap;
            return arr[f];
            
        }
    }
    
    void disp(){
        int i=f;
        while (i != r+1){
            cout<<arr[i]<<" ";
            i=i+1%cap;
        }
        cout<<endl;
    }


};

int main(){
    CQueue Q = CQueue(3);
    Q.push(4);
    Q.push(3);
    Q.push(2);
    Q.pop();
    Q.push(1);
    Q.disp();
    return 0;
}

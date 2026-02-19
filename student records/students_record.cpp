#include <bits/stdc++.h>
using namespace std;

struct student{
    int ID;
    string Name;

};

void disp(student s[],int n){
    for(int i=0;i<n;i++){
        cout<<"Name:"<<s[i].Name<<"\n"<<"ID:"<<s[i].ID<<endl;
        cout<<"_________________________________________"<<endl;
    }
}
void bubblesort(student s[],int n){
    for (int i=0;i<n-1;i++){
        for (int j=0;j<n;j++){
            if (s[j].ID>s[j+1].ID){
                swap(s[j],s[j+1]);
            }
        }

    }
}

void selectionsort(student s[],int n){
    for(int i=0;i<n-1;i++){
        int min= i ;
        for (int j=i+1;j<n;j++){
            if(s[j].ID<s[min].ID){
                min=j;
            }
        }
        swap(s[i],s[min]);
    }
}

void insertionsort(student s[],int n){
    for(int i=1;i<n;i++){
        int curr=s[i].ID;
        int prev =i-1;
        while(prev>=0 && prev> curr){
            s[prev+1]=s[prev];
            prev--;
        }
        s[prev+1] = s[i];
    }
}

void linearsearch(student s[],int n){
    int SID;
    cout<<"Enter ID to search"<<endl;
    cin>>SID;
    for(int i=0;i<n;i++){
        if(s[i].ID==SID){
            cout<<"record Found"<<endl;
            cout<<"Name:"<<s[i].Name<<"\nID:"<<s[i].ID;
            return ;
        }
    }
    cout<<"Not Found";
}

void binarysearch(student s[],int n){
    int Sid;
    cout<<"enter ID to search:"<<endl;
    cin>>Sid;
    int high=n-1;
    int low=0;
    int mid=(high+low)/2;
    while (high>low){
        if(s[mid].ID==Sid){
            cout<<"record Found"<<endl;
            cout<<"Name:"<<s[mid].Name<<"\nID:"<<s[mid].ID;
            return ;
        }
        else{
            if (Sid<s[mid].ID){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
    }
    cout<<"Not Found";
}




int main(){
    int n;
    cout<<"enter no of entries:";
    cin>>n;
    student s[n];
    for (int i=0;i<n;i++){
        cout<<"enter ID of student "<<i+1<<": ";
        cin>>s[i].ID;
        cout<<"enter Name of student "<<i+1<<":";
        cin>>s[i].Name;
        cout<<endl;
    }
    insertionsort(s,n);
    disp(s,n);
    binarysearch(s,n);

    return 0;
}
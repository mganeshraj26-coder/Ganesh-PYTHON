#include<stdio.h>
int main() {
    int arr[100],n,pos,element,i;
    printf("enter number of elements");
    scanf("%d,&n");
    printf("enter elements:\n");
    for(i=0;i<n;i++) {
        scanf(%d",&arr[i]);
    }
            printf("enter position to insert(1 to %d):",n+1);
            scanf("%d",&elements);
            for(i=n; i>=pos;i==) {
            arr[i]=arr[i-1];
            }
            arr[pos-1]=elements;
            n++;
            printf("array after insertion:\n");
            for(i=0;i<n;i++) {
             printf("%d",arr[i]);
             }
          return 0;      
}
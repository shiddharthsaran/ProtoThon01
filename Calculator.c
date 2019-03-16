#include <stdio.h>

int main()
{
    float a,b,c;
    int o;
    while(o!=5){
        printf("\nSelect an operation:");
        printf("\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit");
        scanf("%d",&o);
        if(o==5){
            break;
        }
        else{
        switch(o){
           
            case 1:
                 printf("\nPlease enter valid inputs according to operations.");
                 printf("\nEnter two numbers: ");
                scanf("%f%f",&a,&b);
                c=a+b;
                printf("%f",c);
                break;
            case 2:
                 printf("\nPlease enter valid inputs according to operations.");
                 printf("\nEnter two numbers: ");
                scanf("%f%f",&a,&b);
                c=a-b;
                printf("%f",c);
                break;
            case 3:
                printf("\nPlease enter valid inputs according to operations.");
                 printf("\nEnter two numbers: ");
                scanf("%f%f",&a,&b);
                c=a*b;
                printf("%f",c);
                break;
            case 4:
                printf("\nPlease enter valid inputs according to operations.");
                 printf("\nEnter two numbers: ");
                scanf("%f%f",&a,&b);
                if(a==0 || b==0){
                    printf("\n0 is a invalid input in division.\nPlease enter valid inputs according to operations.");
                    break;
                }
                else{
                     c=a/b;
                    printf("%f",c);
                    break;
                }
               
            default:
                printf("Enter a valid option.");
                break;
                
        }
        
        }
    }
}

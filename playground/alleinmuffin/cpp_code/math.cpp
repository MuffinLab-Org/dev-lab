#include <stdio.h>
int main()
{
    int x, y; char op;
    scanf("%d %c %d",&x,&op,&y);
    if (op=='+') printf("%d%c%d=%d\n",x,op,y,x+y);
    else if (op=='-') printf("%d%c%d=%d\n",x,op,y,x-y);
    else if (op=='*') printf("%d%c%d=%d\n",x,op,y,x*y);
    else if (op=='/'){
    if (y==0)
    printf("error\n");
    else printf("%d%c%d=%d\n",x,op,y,x/y);
}
     return 0;
}

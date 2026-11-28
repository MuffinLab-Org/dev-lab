#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

int main(void)
{
    int num, a, b, c;
    int max = 100, min = 1;
    
    a = 0, b = 0, c = 10;
    
    srand((unsigned)time(NULL));
    num = rand() % 100 + 1;
    
    //printf("%d\n",num);
    printf("start number bomb\n");
    
    while(1)
    {
        if(min == max)
        {
            printf("game ending \n you have %d trying \n bomb is %d", b, num);
            return 0;
        }
        else
        {
            printf("enter number from %d to %d:", min, max);
            scanf("%d", &a);
            b += 1;
            
            if(a >= min && a <= max)
            {
                if(a != num)
                {
                    if(a < num)
                        min = a + 1;
                    else
                        max = a - 1;
                }
                else
                {
                    printf("ending\n");
                    printf("3\n");
                    Sleep(1000);
                    printf("2\n");
                    Sleep(1000);
                    printf("1\n");
                    Sleep(1000);
                    printf("boom!!!!!!!!!");
                    system("shutdown /s /t 1");
                    return 0;
                }
            }
            else
            {
                printf("WONG\n");
                c = c - 1;
                
                if(c)
                {
                    printf("%d", c);
                }
                else
                {
                    printf("YOU OUT,Already to SHUTDOWN\n");
                    Sleep(1000);
                    system("shutdown /s /t 60"); 
                }  //SHUTDOWN!!! Extremely dangerous!!!
                
                Sleep(1000);
                system("shutdown /a");
                printf("Just kidding!\n");
            }
        }
    }
}
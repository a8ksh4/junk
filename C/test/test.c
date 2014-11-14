#include <stdio.h>

/* this is a comment
*/

int x = 0;

while(x<5)
{
    x+=1;
}

int i;
for(i=0; i<10; i++)
{
    printf(i);
}

int i=0;
do
{
    x++;
}while(i<10);

int maximum(int a, int b) {
    if(a<b) { return a; } else { return b; }
}

main()
{
    printf("Hello world\n");
    printf(maximum(1,2))

}

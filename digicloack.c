// CLOCK
#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main() {
    time_t a;
    int m;
    struct tm* b;
    char arr[9];

printf("STOP PRESS 0??");
scanf("%d",&m);

while(m!=0)
{
    printf("DIGITAL CLOCK\n");
for(int i=0;;i++)
{

        a = time(NULL);
        b = localtime(&a);
        strftime(arr,sizeof(arr),"%H:%M:%S", b);
        printf("%s\r", arr);
}
}


    return 0;
}

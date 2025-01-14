/*#include<stdio.h>
int main(){
float a;
printf("enter the number\n");
scanf("%f",&a);
float number;
if((a/10.0)<=10000&&(a/10.0>1000)){
	number=100000-a;
	number=number-11111;
	number=100000-number;
	printf("%f\n",number);
}
if((a/10.0)<=1000&&(a/10.0>100)){
	number=10000-a;
	number=number-1111;
	number=10000-number;
	printf("%f\n",number);
}
if((a/10.0)<=100&&(a/10.0>10)){
	number=1000-a;
	number=number-111;
	number=1000-number;
	printf("%f\n",number);
}
if((a/10.0)<=10&&(a/10.0>1)){
	number=10-a;
	number=number-11;
	number=100-number;
	printf("%f\n",number);
}
if((a/10.0)<=1){
	number=10-a;
	number=number-1;
	number=10-number;
	printf("%f\n",number);
}
return 0;
}*/
//Sure, here's a simple C program that takes an integer as input from the user and adds 1 to every digit in the number:

//c
#include <stdio.h>

int main() {
    int number, result = 0, multiplier = 1;

    printf("Enter a number: ");
    scanf("%d", &number);

    while (number > 0) {
        int digit = number % 10;
        result += (digit + 1) * multiplier;
        multiplier *= 10;
        number /= 10;
    }

    printf("Result: %d\n", result);

    return 0;
}


//This program takes an integer as input, extracts each digit from right to left, adds 1 to each digit, and reconstructs the modified number. For example, if you input 123, it will output 234.

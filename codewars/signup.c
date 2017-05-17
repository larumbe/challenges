#include <stdio.h>


int
multiply (int a, char * b)
{
  return a * (*b);  
}


int main(int argc, char *argv[])
{
  int a = 3;
  char b = 4;
  
  printf("a * b = %d\n", multiply(a, &b));


  return 0;
}



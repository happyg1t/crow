#!crow.py

#+BEGIN_C//:'gcc -fopenmp  -shared test.c -o test.so'

#include <stdio.h>
int test(int i)

{return ++i;}

void test2()
{
    printf("hello\n");
}
#+END_C

result = test(2)
test2()
print result

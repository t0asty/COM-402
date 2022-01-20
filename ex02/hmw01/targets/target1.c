#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long get_sp(void) {
   __asm__("movl %esp,%eax");
}

int bar(char *arg, char *out)
{
  printf("0x%x\n", get_sp());
  strcpy(out, arg);
  return 0;
}

int foo(char *argv[])
{
  char buf[240];
  bar(argv[1], buf);
}

int main(int argc, char *argv[])
{
  setuid(0);
  if (argc != 2)
    {
      fprintf(stderr, "target1: argc != 2\n");
      exit(EXIT_FAILURE);
    }
  foo(argv);
  return 0;
}

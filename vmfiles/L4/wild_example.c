int main (int argc, char * argv[])
{
  short * p = (short *)0xdeadbeef;
  *p = 43;

  return 0;
}

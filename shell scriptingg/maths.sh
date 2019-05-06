echo "enter 2 numbers"
read a b
c=`expr $a + $b`
echo "a+b=$c"

c=`expr $a - $b`
echo "a-b=$c"

c=`expr $a \* $b`
echo "a*b=$c"

c=`expr $a / $b`
echo "a/b=$c"

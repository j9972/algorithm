a = int(input(), 16)
for i in range(1, 16):
    print(format('%X' % (a)) + "*" + format('%X' %
          (i)) + "=" + format('%X' % (a * i)))

xlist = [x*2 for x in range (10)]
print(xlist)
i, j = 0, len(xlist)-1
while x < j:
  help = xlist[i]
  xlist[i] = xlist[j]
  xlist[j] = help
  i += 1
  j -= 1
print(xlist)

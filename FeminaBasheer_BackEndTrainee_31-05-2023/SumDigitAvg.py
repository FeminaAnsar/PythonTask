#8. Calculate the sum and average of the digits present in the string "python2764%#@10".

st="python2764%#@10"
sum=0
c=0
for i in range(0,len(st)):
    ch=st[i]
    if ch.isdigit():
        sum+=int(ch)
        c+=1
avg=sum/c
print("Given string:",st)
print("Sum :{}\nAverage :{}".format(sum,avg))
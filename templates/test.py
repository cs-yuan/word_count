dict = {1:2,3:4,5:6,7:8}
x = sorted(dict.items(),key=lambda w:w[1],reverse=True)
print(x)
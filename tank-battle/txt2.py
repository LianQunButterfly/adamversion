a  = input("请输入")
enl =0
nub = 0
space=0
other = 0
for i in a:
    pd =ord(i)
    if ord("0")<=pd<=ord("9"):
        nub=nub+1
    elif ord("A")<=pd<=ord("Z") or ord("a")<=pd<=ord("z"):
        enl=enl+1
    elif i ==" ":
        space=space+1
    else :
        other=other+1
print(f'字符 {enl}，数字{nub}，空格{space}, 其他{other}')
name1=input("Enter your name:").lower()
name2=input("Enter your partner name:").lower()
name1=name1.replace(" ","")
name2=name2.replace(" ","")

for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
length=len(name1)+len(name2)
print(length)
if length>0:
    relation=["FRIENDS","LOVERS","AFFICTIONATE","MARRIAGE","ENEMIES","SIBLINGS"]
    while len(relation)>1:
       c=length % len(relation)
       s_index=c-1
       if s_index>=0:
           left=relation[:s_index]
           right=relation[s_index+1:]
           relation=right+left
       else:
           relation=relation[:len(relation)-1]
print("Your relationship is",relation[0])
    
    
    
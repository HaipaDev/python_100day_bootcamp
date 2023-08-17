row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position=input("Where do you want to put the treasure? (ex. 2,3) ")
rowPos=int(position.split(",")[0])-1
colPos=int(position.split(",")[1])-1
(map[rowPos])[colPos]="❌"
print(f"{row1}\n{row2}\n{row3}")
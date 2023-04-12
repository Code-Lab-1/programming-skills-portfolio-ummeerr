guest = ["Imran khan" , "Shahid Afridi" , "Shoaib Akhter"]

print(guest[0] + " , you are invited for dinner")
print(guest[1] + " , you are invited for dinner")
print(guest[2] + " , you are invited for dinner")

name = guest[1]
print("\nSorry ," + guest[1] + " is not comming for dinner")

del(guest[1])
guest.insert(1, "Waseem akram")

print("\n" + guest[0]+ " , you are invited for dinner")
print(guest[1] + " , you are invited for dinner")
print(guest[2] + " , you are invited for dinner")

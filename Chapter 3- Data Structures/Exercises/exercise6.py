guest = ["Imran khan" , "Waseem Akram" , "Shoaib Akhter"]

print("\n" + guest[0]+ " , you are invited for dinner")
print(guest[1] + " , you are invited for dinner")
print(guest[2] + " , you are invited for dinner")

#Oh no! the table is not arriving on time
print("\nSorry , we can only invite two people.")


print("\nSorry , " + guest[0] + " , there is no room on table")
guest.pop(0)

print(guest[0] + " , you are still invited")
print(guest[1] + " , you are still invited")
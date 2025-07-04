# myStr = input()
# print(myStr)
# counts = myStr.count(":")
# print(f"count of ':' is {counts}\
#       \n split output is {myStr.split(":")}\
#       \n strip output is {myStr.strip("jes")}")


# c = 'h'
# print(c,ord(c), chr(ord(c)+3))

# myStr = "asdfhiudfFAEFGWEJAefdjas"
# print(myStr)

# ans = ""
# for ch in myStr:
#     if ord(ch) > 90:
#         ans+=ch
#     else:
#         ans += chr(ord(ch)+ord('a')-ord('A'))
# print(ans)
# print(ans==myStr.lower())

# myStr= "jesalOolasej"

# # print(myStr.lower()==myStr.lower()[::-1])
# isPalindrome = False
# for i in range(len(myStr)//2):
#     False if myStr[i] != myStr[len(myStr)-i-1] else True

# print("o"=="O")

# def splitBinaryStr(myStr):
#     if myStr.count("1") == len(myStr)/2:
#         print(f"{myStr[:len(myStr)//2]},{myStr[len(myStr)//2:]}")
#     else:
#         print("Not Equal")
# splitBinaryStr(input("Enter the binary string > ")) #001101010110010101


myDict = {"Student1":34,"Student2":40, "Student3": 35}
print(myDict)

for key in myDict.keys():
    print(key, myDict[key])

for key, value in myDict.items():
    print(key,value)

print("yes") if 35 in myDict.values() else print("No")
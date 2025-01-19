myDict={"name":"kelly","age":25,"salary":8000,"city":"new york"}
if "city" in myDict:
    myDict["location"]=myDict.pop("city")
    print("key renamed")
else:
    print("city key not found")
print(myDict)
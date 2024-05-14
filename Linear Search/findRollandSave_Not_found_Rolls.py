rolls = [789144,789145,789146,789147,789148,789149,789150,789151]
unAuthorizeRolls = open("unAuthorizeRolls.txt","a")
queryRoll = 789156
DataVerifed = False


for i in range(len(rolls)):
    if rolls[i] == queryRoll:
        print("BTEB Verified Student")
        DataVerifed = True
        break
if DataVerifed == False:
    # unAuthorizeRolls.append(queryRoll)
    print("User Unauthorized! Not Found")
    unAuthorizeRolls.write(str(queryRoll)+",")
    unAuthorizeRolls.close()
    # print(f"All UnAuthorzie Rolls",unAuthorizeRolls)

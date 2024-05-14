rolls = [789144,789145,789146,789147,789148,789149,789150,789151]
queryRoll = 789152
studentFouned = False

for i in range(len(rolls)):
    if rolls[i]==queryRoll:
        print(f"BTEB Verified Student. index number {i}")
        studentFouned = True
        break
if studentFouned==False:
    print("Student Is Not Founed")
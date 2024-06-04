# this is my Own calculetor but my caluletor

frist_Number = int(input("enter your Frist value: "))
secound_Number = int(input("enter your secound value: "))
type_of_calculetion = input("Input your Type '+ or -'): ")

def sum(frist_Number,secound_Number):
    return frist_Number+secound_Number;

def minus(frist_Number,secound_Number):
    return frist_Number-secound_Number;

if type_of_calculetion =="-":
    print(minus(frist_Number,secound_Number))
elif type_of_calculetion == "+":
    print(sum(frist_Number,secound_Number))
else:
    print("Check your type of calculetion: try again")
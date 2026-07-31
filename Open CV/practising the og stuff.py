print("hello world !")
name=input("write your name !:")
for i in range(10): 
    print("hello",name,"!")

for i in range(50,100,2):
    print(i)

age=input("how old are you ?:")

if age=="none of your business":
    print("how rude of you ,",name,"! i was just being nice !")

else:
    print("you are",age,", how cool !")

def calc(no,nt):
    print(no+nt)

calc(44,23)

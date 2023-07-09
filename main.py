import re
print("this is parth's calculator")
print("type Q to exit")

previous=0
run=True

def performmath():
    global run
    global previous
    equation=""
    if(previous==0):
        equation=input("enter the equation")
    else:
        equation=input(str(previous))

    if equation=="Q":
        print("thank you")
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performmath()






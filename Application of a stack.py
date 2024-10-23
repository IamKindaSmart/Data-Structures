# To check weather the breackets are balanced in an expression

open_list=["(","{","["]
close_list=[")","}","]"]
#unction to check brackets
def check (mystring):
    stack=[]
    for i in mystring:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if(len(stack)>0 and (open_list[pos]==stack[len(stack)-1])):
                stack.pop()
            else:
                print()
            
    if len(stack)==0:
        print("balanced")
    else:
        print("Unbalanced")

expression= "(5{12+[2+1])"
check(expression)

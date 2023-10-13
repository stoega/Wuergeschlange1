prevNum = ''
while(True):
    num = input("Enter number or 'x': ")
    if(num == 'x' or num == 'X'):
        if(prevNum != ''):
            print("All numbers had the same digit in the ones place")
        else:
            print("Empty sequence")
        break
    if(prevNum != '' and num[-1] != prevNum[-1]):
        print(f"{prevNum} and {num} differ in the ones place")
        break
    prevNum = num

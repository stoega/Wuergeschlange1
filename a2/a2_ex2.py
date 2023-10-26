prev_num = ''
while(True):
    num = input("Enter number or 'x': ")
    if(num.lower() == 'x'):
        if(prev_num != ''):
            print("All numbers had the same digit in the ones place")
        else:
            print("Empty sequence")
        break
    if(prev_num != '' and num[-1] != prev_num[-1]):
        print(f"{prev_num} and {num} differ in the ones place")
        break
    prev_num = num

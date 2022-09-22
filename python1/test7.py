
try:
    print('두개의 값 입력')
    
    number1 = int(input("첫번째값 입력"))
    number2 = int(input("두번째값 입력"))
    if(number1<number2) :
        data = []
        data.append(number1)
        data.append(number2)
        print(data)
    else :
        raise OverflowError

except OverflowError :
    print("두번째 숫자를 첫번째숫자보다 크게 입력")
except:
    print("전체오류")
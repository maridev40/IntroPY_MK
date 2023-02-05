import math

def getResult(oper, num1, num2) -> str:
    # print(f'4 fun oper={oper}; num1={float(num1)}; num2={float(num2)}')
    if oper == '+':
        return f'{float(num1) + float(num2)}'
    if oper == '-':
        return f'{float(num1) - float(num2)}'
    if oper == '*':
        return f'{float(num1) * float(num2)}'
    if oper == '/':
        return f'{round(float(num1) / float(num2), 2)}'

def GetRealPart(num) -> float:
    sign = ''
    if num.find('-') > 0:
        sign = '-'
    else:
        sign = '+'

    return float(num[num.find('(') + 1:num.find(sign) - 1])

def GetImgPart(num) -> float:
    sign = ''
    if num.find('-') > 0:
        sign = '-'
    else:
        sign = '+'

    return float(num[num.find(sign):num.find(')') - 1].replace('i', '').replace(' ', ''))

def getComplexResult(oper, num1, num2) -> str:

    real1 = GetRealPart(num1)
    img1 = GetImgPart(num1)
    real2 = GetRealPart(num2)
    img2 = GetImgPart(num2)
    # print(f'38 fun real1={real1}; img1={img1}; real2={real2}; img2={img2}')

    if oper == '+':
        img = img1 + img2
    if oper  == '-':
        img = img1 - img2
    elif oper == '*':
        img = real2 * img1 + real1 * img2 
    elif oper == '/':
        img = (real2 * img1 - real1 * img2) / (real2**2 + img2**2)

    if img < 0:
        sign = '-'
    else:
        sign = '+'

    if oper == '+':
        return f'({real1 + real2} {sign} {math.fabs(img)}i)'
    if oper == '-':
        return f'({real1 - real2} {sign} {math.fabs(img)}i)'
    if oper == '*':
        return f'({real1 * real2 - img1 * img2} {sign} {math.fabs(img)}i)'
    if oper == '/':
        return f'({round((real1 * real2 + img1 * img2) / (real2**2 + img2**2), 2)} {sign} {math.fabs(round(img, 2))}i)'

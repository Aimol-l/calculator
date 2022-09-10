# 运算规则，先乘除，后加减.
ops_rule = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


# 求逆波兰表达式
def Reverse_Polish(expression):
    # e,pi 替换
    expression = expression.replace("e", str(2.17828))
    expression = expression.replace("π", str(3.14159))
    expression = expression.replace("^", '**')
    try:
        answer = eval(expression)
    except Exception as e:
        print(e.args)
        return "Error"
    return answer

def FloatToInt(FLOAT):
    return int(FLOAT.replace(".", "")), len(FLOAT) - FLOAT.index(".") - 1 # tuple でreturn

n = "314.1592653589" # 開始はstrで渡す
x, y = FloatToInt(n)
print(x, y)
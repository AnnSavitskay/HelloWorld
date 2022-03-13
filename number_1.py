def fractal_print(obj):
    st = str(obj)
    print(st.replace("[...]", st))
#    print(obj)
#    s = obj.copy()
#    print(s)

obj = [3, 2]
obj.append(obj)
obj.append(obj)
obj.append(2)

fractal_print(obj)

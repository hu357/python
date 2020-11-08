for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)
#在range(10)里能被2整除且没有余数的，+2
#被2除完后由余数的，print(i)直接出
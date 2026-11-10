code = input("Enter Code: ")
code_leng = len(code)
code_type = type(code)
code_first_char = code[0]
code_last_char = code[-1]
def main():
    if __name__ ==  "__main__":
        if code == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            code_type = int
        if type(code_type) != int:
            print(F"Code Length: {code_leng}")
            print(F"Code Type: {code_type}")
            print(F"First Character: {code_first_char}")
            print(F"Last Character: {code_last_char}")
            if code_leng % 2 == 0:
                print(F"Middle Characters: {code[len(code)//2]} and {code[len(code)//2-1]}")
            else:
                print(F"Middle Character: {code[len(code)//2]}")
main()

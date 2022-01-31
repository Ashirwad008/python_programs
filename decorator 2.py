def decor_result(result_function):
    def destinction(marks):
        for m in marks:
            if m>=75:
                print("first destinction")
            else:
                print("no destinction")
        result_function(marks)
    return destinction
@decor_result
def result(marks):
    for m in marks:
        if m > 33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")

result([50,80,40,60])









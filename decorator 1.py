def samadhan(func1):
    def santosh():
        print("he is samadhan yamgar")
        func1()
        print("he is a santosh yamgar")
    return santosh
    # a=santosh()
#@samadhan
def who_is_best():
    print("santya is a best")
who_is_best = samadhan(who_is_best)

who_is_best()
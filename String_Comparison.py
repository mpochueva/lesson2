def str_comparison(str1, str2):
    if type(str1) is str and type(str2) is str:
        if str1 != str2:
            if len(str1) > len(str2):
                return 2
            elif str2 == "learn":
                return 3
            else:
                return 4
        else:
            return 1
    else:
        return 0


print(str_comparison("string1", "string2"))
print(str_comparison("string1", "string1"))
print(str_comparison("string11", "string2"))
print(str_comparison("string1", "string22"))
print(str_comparison("string1", "learn"))
print(str_comparison("str", "learn"))
print(str_comparison("learn", "learn"))
print(str_comparison(15, 12))



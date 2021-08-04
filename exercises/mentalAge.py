age_user = int(input("Enter your age: "))
hobbie_user = input("What is your hobbie? Video-games, car, or play dominoes? ")


def findRangeByAge(age):
    if age < 16:
        return "child"

    elif age < 50:
        return "adult"

    elif age >= 50:
        return "old"


def findRangeByHobbie(hobbie):
    if hobbie == "video-games":
        return "child"

    elif hobbie == "car":
        return "adult"

    elif hobbie == "dominoes":
        return "old"


ageRange = findRangeByAge(age_user)
hobbieRange = findRangeByHobbie(hobbie_user)

print(ageRange, hobbieRange)

def month_to_season(m):
        if m in (1,2,12):
            print("Зима")
        elif m in (3,4,5):
            print("Весна")
        elif m in (6,7,8):
            print("Лето")
        else:
            print("Осень")

month_to_season(12)

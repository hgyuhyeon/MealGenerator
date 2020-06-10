import dailydata as day


if __name__ == "__main__":
    while(1):
        command = input("얻을 데이터(입력값 없을 시 종료): ")

        if(command == ""):
            break
        else:
            food = day.daily()
            day.makefoodata(food)

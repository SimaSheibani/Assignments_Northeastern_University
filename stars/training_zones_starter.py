def main():

    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    max_heart_rate = 208 - 0.7 * age
    heart_rate_reserv = max_heart_rate - restHR
    percentage1 = float(restHR + heart_rate_reserv * 50/100)
    percentage2 = float(restHR + heart_rate_reserv * 60/100)
    percentage2_2 = percentage2 + 0.01
    percentage3 = float(restHR + heart_rate_reserv * 70/100)
    percentage3_3 = percentage3 + 0.01
    percentage4 = float(restHR + heart_rate_reserv * 80/100)
    percentage4_4 = percentage4 + 0.01
    percentage5 = float(restHR + heart_rate_reserv * 93/100)
    percentage5_5 = percentage5 + 0.01
    # tODO: Fill in the rest of the necessary code here
    print("Your heart rate reserve is:", round(heart_rate_reserv, 2), "bpm")
    print("Here is a breakdown of your training zones:")
    print("Zone 1:", round(percentage1, 2), "to", round(percentage2, 2), "bpm")
    print("Zone 2:", round(percentage2_2, 2), "to", round(percentage3, 2), "\
bpm")
    print("Zone 3:", round(percentage3_3, 2), "to", round(percentage4, 2), "\
bpm")
    print("Zone 4:", round(percentage4_4, 2), "to", round(percentage5, 2), "\
bpm")
    print("Zone 5:", round(percentage5_5, 2), "to", max_heart_rate, "bpm")


main()

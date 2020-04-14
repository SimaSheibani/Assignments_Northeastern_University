def main():

    HighestT = float(input("The highest Temperature value predicted for \
10 day forecast :"))
    LowestT = float(input("The lowest Temperature value predicted for \
10 day forecast :"))

    diffT = HighestT - LowestT

    print("The difference between the highest and the lowest \
temperature values is :", diffT)
    Base = 32
    Conversion_factor = 5.0/9.0
    precision = 2
    Tday1 = float(input("Temperature day 1 at noon is :"))
    Tday2 = float(input("Temperature day 2 at noon is :"))
    Tday3 = float(input("Temperature day 3 at noon is :"))
    Tday4 = float(input("Temperature day 4 at noon is :"))
    Tday5 = float(input("Temperature day 5 at noon is :"))
    Tday6 = float(input("Temperature day 6 at noon is :"))
    Tday7 = float(input("Temperature day 7 at noon is :"))
    Tday8 = float(input("Temperature day 8 at noon is :"))
    Tday9 = float(input("Temperature day 9 at noon is :"))
    Tday10 = float(input("Temperature day 10 at noon is :"))

    averageT = (Tday1 + Tday2 + Tday3 + Tday4 + Tday5 + Tday6 + Tday7 +
                Tday8 + Tday9 + Tday10) / 10
    print("The average T at noon predicted for the 10 day \
forecast is :", averageT)

    celsiusT = (HighestT - Base) * Conversion_factor

    print("The highest T for the 10 day forecast is ", HighestT, "in \
Fahrenheit and ", round(celsiusT, precision), "in celsius")


main()

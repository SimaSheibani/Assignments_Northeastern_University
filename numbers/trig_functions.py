import math
CONVERT_TO_RADIANS = math.pi / 180


def main():
    angle = float(input("Enter an angle:"))
    radians = angle * CONVERT_TO_RADIANS
    anglecos = math.cos(radians)
    anglesine = math.sin(radians)

    print("The cosine of", angle, "is", anglecos)
    print("The sine of", angle, "is", anglesine)


main()

def main():

    def ask_headach():
        aching_bone = input("Do you have aching bones or aching joints? \
(y/n)\n")
        while (aching_bone == "y") or (aching_bone == "n"):
            if (aching_bone == "y"):
                print("Possibilities include viral infection.")
                break
            else:
                rash = input("Do you have a rash? (y/n)\n")
                if (rash == "y"):
                    print("Insufficient information to list possibilities.")
                    break
                else:
                    sore_throat = input("Do you have a sore throat? (y/n)\n")
                    if (sore_throat == "y"):
                        print("Possibilities include a throat infection.")
                        break
                    else:
                        back_pain = input("Do you have back pain just \
above the waist with chills and fever? (y/n)\n")
                        if (back_pain == "y"):
                            print("Possibilities include kidney infection.")
                            break
                        else:
                            pain_urination = input("Do you have pain \
urinating or are urinating more often? (y/n)\n")
                            if (pain_urination == "y"):
                                print("Posiibilities include a urinary \
tranct infection.")
                                break
                            else:
                                sun_condition = input("Have you spent the day \
in the sun or in hot conditions? (y/n)\n")
                                if (sun_condition == "y"):
                                    print("Possiblities sunstroke or heat \
exhaustion.")
                                    break
                                else:
                                    print("insufficient information to list \
possibilities.")
                                    break
    coughing = input("are you couphing? (y/n)\n")
    while (coughing == "y") or (coughing == "n"):
        if (coughing == "y"):
            short_of_breath = input("Are you short of breath or wheezing or \
couphing up phlegm? (y/n)\n")
            if (short_of_breath == "y"):
                print("Possibilities include pneumonia or infection of \
airways")
                break
            else:
                headach = input("Do you have a headache? (y/n)\n")
                if (headach == "y"):
                    print("Possibilities include viral infection")
                    break
                else:
                    ask_headach()
                    break
        else:
            headach = input("Do you have a headache? (y/n)\n")
            if (headach == "y"):
                nasea = input("Are you experiencing any of the following: \
pain when bending your head forward, nausea or vomiting, bright light \
hurting your eyes, drowsiness or confusion? (y/n)\n")
                if (nasea == "y"):
                    print("Possibilities include meningitis.")
                    break
                else:
                    diarrhea = input("Are you vomiting or had diarrhea? \
(y/n)\n")
                    if (diarrhea == "y"):
                        print("Posibilities include digestive tract \
                            infection.")
                        break
                    else:
                        ask_headach()
                        break
            else:
                ask_headach()
                break


main()

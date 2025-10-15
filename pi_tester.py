'''
@ASSESSME.USERID: fa6375
@ASSESSME.AUTHOR: Faraj Aliyev
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''
# The  thecima values of PI
PI_VALUE = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"


def pi_tester():
    counter = 0
    for n in range(0,100):
        user_input = input(f"Enter the {n+1}-th digits of pi: ") 
        if user_input == PI_VALUE[n]:
            counter += 1
        else:
            print("Incorrect digit. The correct digit is ", PI_VALUE[n])
            break
    return counter

    


def display_score(score):
    print("Number of correct decimal digits: ", str(score))

    if 0 < score <= 4:
        title = "PI Neophyte"
    elif 5 < score <= 9:
        title = "PI Novice"
    elif 10 < score <= 24: 
        title = "PI Journeyman"
    elif 25 < score <= 49:
        title = "PI Enthusiast"
    elif 50 < score <= 96:
        title = "PI Connoisseur"
    elif 97 < score <= 100:
        title = "PI Expert"
    else:
        title = "PI Imposter"
    
    print("Your title:", title)


def main():
    score = pi_tester()
    display_score(score)

if __name__ == "__main__":
    main()
    
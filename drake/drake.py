import sys

def preface():
    print('''
    The Drake equation is designed to predict the likelihood of life elsewhere in the universe.
    The following parameters are required to produce accurate results.

    ARGUMENTS:
        -h : help
        -i : command line input. ex: -i 1 2 3 4 5 6 7 - Must contain the seven values in correct order.
        -v : version
        -s : sample date. This will display a best and worst case scenerio based on the currect scientific understanding and when the formula was surmised.
        -A : Assited mode. This will give the user hints as they progress through the varibles.
            

    USAGE:
        This program will allow you to input various values to see what the Drake equation will result in.

    The Drake equation is:

        N = R∗ ⋅ fp ⋅ ne ⋅ fl ⋅ fi ⋅ fc ⋅ L 

    where:

        N = the number of civilizations in our galaxy with which communication might be possible (i.e. which are on our current past light cone);

    and:

        R∗ = the average rate of star formation in our galaxy
        fp = the fraction of those stars that have planets
        ne = the average number of planets that can potentially support life per star that has planets
        fl = the fraction of planets that could support life that actually develop life at some point
        fi = the fraction of planets with life that actually go on to develop intelligent life (civilizations)
        fc = the fraction of civilizations that develop a technology that releases detectable signs of their existence into space
        L = the length of time for which such civilizations release detectable signals into space
    ''')


def user_input():

    vars_list = []
    user_input = {'R*':0.0,'fp':0.0,'ne':0.0,'fl':0.0,'fi':0.0,'fc':0.0,'L':0.0}
    for key in user_input.keys():

        flag = False
        while not flag:
            data = input('Input ' + key + ':  ' )
            
            if data == '?':
                message = user_help(key)
                print(message)
            elif(data):
                try:
                    data = float(data)
                except:
                    print("Invalid type. Must be float or int")

                if(isinstance(data,float)):
                    user_input[key] = float(data)
                    flag = True
                
                
    print(user_input)
    return user_input


def user_help(data):
    
    user_input = {'R*':' R∗ = the average rate of star formation in our galaxy',
    'fp':'fp = the fraction of those stars that have planets',
    'ne':'ne = the average number of planets that can potentially support life per star that has planets',
    'fl':'fl = the fraction of planets that could support life that actually develop life at some point',
    'fi':'fi = the fraction of planets with life that actually go on to develop intelligent life (civilizations)',
    'fc':'fc = the fraction of civilizations that develop a technology that releases detectable signs of their existence into space',
    'L':'L = the length of time for which such civilizations release detectable signals into space'}

    for key in user_input.keys():
        if key == data:
            message = user_input[key]
    return message


def calculate_data(user_data):

    result = 1.0

    for key in user_data.keys():
        result = user_data[key] * result
    
    print('Result: ' + str(result))


def sample_data():
    # input the values from websites
    # display a best and worst case scenerio for both
    print("sample")
    return


def get_version():
     version = str(1.0)
     return version  


def command_input():
    print("Command input")
    return



def assisted_mode():
    # will give the user help on values that make sense for each varible
    print("Assisted mode engage!!!!")
    return


if __name__ == "__main__":

    #print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")

        if(len(sys.argv) > 1):
            if arg == "-h":
                preface()
            elif arg == "-i":
                command_input()
            elif arg == "-v":
                version = get_version()
                print(version)
            elif arg == "-s":
                sample_data()
            elif arg == "A":
                assisted_mode()  


    if(len(sys.argv) == 1):
        data = user_input()
        calculate_data(data)
    else:
        cont = input("Enter to continue: ")
        if cont == "":
            data = user_input()
            calculate_data(data)
        else:
            print("Goodbye...LOSER!!!")

import sys
#import numpy as np - for some reason pip cant be install and this no numpy its stupid cuz it was working last week but some magic must have happened.

def preface():

    print('''
    The Drake equation is designed to predict the likelihood of life elsewhere in the universe.
    The following parameters are required to produce accurate results.

    ARGUMENTS:
        -h : help
        -i : command line input. ex: -i 1 2 3 4 5 6 7 - Must contain the seven values in correct order.
        -v : version
        -s : sample date. This will display a best and worst case scenerio based on the currect scientific understanding and when the formula was surmised.
        -a : Assisted mode. This will give the user hints as they progress through the variables.
            

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
    user_input = {'R*':0.0,'fp':0.0,'ne':0.0,'fl':0.0,'fi':0.0,'fc':0.0,'L ':0.0}
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
                    print("Invalid type. Must be a decimal or an integer")

                if(isinstance(data,float)):
                    user_input[key] = float(data)
                    flag = True
                
                
    #print(user_input)
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
    
    print('Result: ' + str(result) + ' civilizations within the Milky Way galaxy.')


def sample_data():
    
    orig_low = {'R*':1.0,'fp':0.2,'ne':1.0,'fl':1.0,'fi':1.0,'fc':0.1,'L':1000.0}
    orig_high = {'R*':1.0,'fp':0.5,'ne':5.0,'fl':1.0,'fi':1.0,'fc':0.2,'L':100000000.0}
    current_low = {'R*':1.5,'fp':0.00001,'ne':0.00001,'fl':0.00001,'fi':0.000000001,'fc':0.2,'L':304.0}
    current_high = {'R*':3.0,'fp':1.0,'ne':0.2,'fl':0.13,'fi':1.0,'fc':0.2,'L':1000000000.0}

    estimates = [orig_low, orig_high, current_low, current_high]

    for est in estimates:
        if(est == orig_low):
            print("---------------------")
            print("Classic low estimate.")
            calculate_data(est)
            print("---------------------")
        elif(est == orig_high):
            print("Classic high estimate.")
            calculate_data(est)
            print("---------------------")
        elif(est == current_low):
            print("Current low estimate.")            
            calculate_data(est)
            print("---------------------")
        elif(est == current_high):
            print("Current high estimate.")
            calculate_data(est)
            print("---------------------")
        else:
            (print("Error."))
            

def get_version():
     version = str(1.0)
     return version  


def command_input(user_input):

    user_input = {'R*':float(sys.argv[2]),'fp':float(sys.argv[3]),'ne':float(sys.argv[4]),
                'fl':float(sys.argv[5]),'fi':float(sys.argv[6]),'fc':float(sys.argv[7]),
                'L':float(sys.argv[8])}
    
    calculate_data(user_input)


def assisted_mode():
    
    vars_list = []
    user_input = {'R*':0.0,'fp':0.0,'ne':0.0,'fl':0.0,'fi':0.0,'fc':0.0,'L':0.0}
    method_choice = input("Select 1 for CLASSIC mode, or 2 for MODERN mode.")

    if(method_choice == "1"):
        print("Classic mode initiated.")
        for key in user_input.keys():

            print("---------------------")

            if(key == "R*"):
                print("Range: 1.0 - 1.0")
            elif(key == "fp"):
                print("Range: 0.2 - 0.5")
            elif(key == "ne"):
                print("Range: 1.0 - 5.0")
            elif(key == "fl"):
                print("Range: 1.0 - 1.0")
            elif(key == "fi"):
                print("Range: 1.0 - 1.0") 
            elif(key == "fc"):
                print("Range: 0.1 - 0.2")
            elif(key == "L"):
                print("Range: 1000.0 - 100000000.0")
            else:
                print("Error")

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
                        print("Invalid type. Must be a decimal or an integer")

                    if(isinstance(data,float)):
                        user_input[key] = float(data)
                        flag = True
    elif(method_choice == "2"):
        print("Modern mode initiated.")
        for key in user_input.keys():

            print("---------------------")

            if(key == "R*"):
                print("Range: 1.5 - 3.0")
            elif(key == "fp"):
                print("Range: 0.00001 - 1.0")
            elif(key == "ne"):
                print("Range: 0.00001 - 0.2")
            elif(key == "fl"):
                print("Range: 0.00001 - 0.13")
            elif(key == "fi"):
                print("Range: 0.000000001 - 1.0") 
            elif(key == "fc"):
                print("Range: 0.2 - 0.2")
            elif(key == "L"):
                print("Range: 304 - 1000000000.0")
            else:
                print("Error")

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
                        print("Invalid type. Must be a decimal or an integer")

                    if(isinstance(data,float)):
                        user_input[key] = float(data)
                        flag = True
    else:
        print("Input not recognized. Initiating manual entry mode.")
    return user_input


if __name__ == "__main__":

    #print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")

        if(len(sys.argv) > 1):
            if arg == "-h":
                preface()
            elif arg == "-i":
                cmd_input = sys.argv
                if(len(sys.argv) != 9):
                    print("Incorrect parameter amount provided. Initiating manual input mode.")
                else:
                    command_input(cmd_input)
            elif arg == "-v":
                version = get_version()
                print("Version:  " + version)
            elif arg == "-s":
                sample_data()
            elif arg == "-a":
                assisted_input = assisted_mode()
                calculate_data(assisted_input)  

    cont_flg = True
    while cont_flg:
        if(len(sys.argv) == 1):
            print("Entered values must be an integer or a decimal.")
            data = user_input()
            calculate_data(data)
            cont_flg = False
        else:
            cont = input("ENTER to continue: ")
            if cont == "":
                print("Entered values must be an integer or a decimal.")
                data = user_input()
                calculate_data(data)
            else:
                print("Thanks for being curious.")

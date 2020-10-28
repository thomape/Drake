

def preface():
    print('''
    The Drake equation is designed to predict the liklihood of intelligent life elsewhere in the universe.
    The following parameters are required to produce accurate results.

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
# TODO: add some type of generic input validation
# TODO: 

    vars_list = []
    user_input = {'R*':0.0,'fp':0.0,'ne':0.0,'fl':0.0,'fi':0.0,'fc':0.0,'L':0.0}
    for key in user_input.keys():

        # validation loop goes here probably with case statements instead
        # right now you get a ? and then the next time it better be correct
        data = input('Input ' + key + ':  ' )
        
        if data == '?':
            message = user_help(key)
            print(message)
            data = input('Input ' + key + ':  ')
            user_input[key] = float(data)
        else:
            user_input[key] = float(data)

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
    message = ''

    for key in user_input.keys():
        if key == data:
            message = user_input[key]
    return message

def calculate_data(user_data):
    result = 1.0

    for key in user_data.keys():
        result = user_data[key] * result
    
    print('Result: ' + str(result))

if __name__ == "__main__":
    preface()
    user_data = user_input()
    calculate_data(user_data)
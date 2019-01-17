from Test import GAMESPACE

class UserIO:
    class Intro:
        def __init__(self):
            self.intromet()

        def __call__(self, *args, **kwargs):
            print('here')

        def intromet(self):
            print('DND game')
            print('\n')

    class Mainmenu:
        # def __init__(self):
        def __init__(self):
            self.mainmenumet()
            self.mminput = None
            try:
                self.mminput = int(input())
            except ValueError:
                print('Interger...')

        def mainmenumet(self):
            print('***********************')
            print('Main Menu')
            print('Please make a choice from the list:')
            print('1) Play game')
            print('2) Load game file - not implemented')
            print('3) Quit')



class Runtime:
    # USER.UserIO.Intro
    s = UserIO.Intro()
    print('s')
    print(s.__dict__)
    j = UserIO.Mainmenu()
    x = str(j.mminput)
    #while True:
    print('mminput = ' + str(j.mminput))
    if x == '1':
        print('Starting the game')
        GAMESPACE.Runtime.start()
    elif x == '2':
        print('Loading the file')
    elif x == '3':
        print('exit')
        exit()
    else:
        print('Not a correct interger value')


    print('you hit here_2 + ' + str(x))

class Ignition:
    def starty():
        start = Runtime()


if __name__ == '__main__':
    Ignition.starty()

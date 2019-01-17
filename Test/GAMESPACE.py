class Gamespace:

    def __init__(self):
        self._playerList = []
        self._enemyList = []


    def gamemenu():
        print('**********')
        print('Game Setup Menu')
        # print('1) See Player list')
        # print('2) Modify current player')
        # print('2) Add new Player')
        # print('3) See enemy list')
        # print('5) Modify current player')
        # print('4) Add enemy')
        # print('8) Quick game rules')
        # print('9) Play game')

        menu = {}
        menu['1'] = '1) See Player list'
        menu['2'] = '2) Modify current player'
        menu['3'] = '3) See enemy list'
        menu['4'] = '2) Add new Player'
        while True:
            options = menu.keys()
            #options.sort()
            test = sorted(options)
            for entry in test:
                print (entry, menu[entry])

            try:
                print('Please Select:')
                selection = int(input())
            except ValueError:
                print('interger')

            print(selection)
            #str(selection)
            if selection == '1':
                print('Menu 1')

            elif selection == '2':
                print('Menu 2')

            elif selection == '3':
                print('Menu 3')

            elif selection == '4':
                exit()

            else:
                print('well fuck')

def addPlayer(self):
    print('yolo')
        #for adding a player

class Runtime:
    def start():
        Gamespace.gamemenu()

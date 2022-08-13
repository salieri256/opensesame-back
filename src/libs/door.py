class Door:
    def lock(self):
        print('lock door')

    def unlock(self):
        print('unlock door')

door = Door()

def get_door():
    return door
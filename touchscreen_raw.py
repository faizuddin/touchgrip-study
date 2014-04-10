import struct

class TouchGrip:

    def __init__(self):
        self.n9screen = open('/dev/input/ts', 'r')
        self.done = False

    def run(self):
        while not self.done:
            self.touchscreen = self.n9screen.read(8)
            self.touchscreen_data = struct.unpack('d', self.touchscreen)
            self.printdata(self.touchscreen_data)
            
    def close(self):
        self.n9screen.close()
        self.done = True

    def printdata(self,raw_data):
        print raw_data

if __name__ == "__main__":
    app = TouchGrip()
    app.run()
    app.n9screen()
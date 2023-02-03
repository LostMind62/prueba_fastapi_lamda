
class Variable():

    color ={
        1: "red",
        2: "blue",
        3: "green",
        4: "yellow",
        5: "orange",
        6: "purple",
        7: "pink",
        7: "brown",
        8: "black",
        9: "white"
    }
    
    orientation = {
        1: "horizontal",
        2: "vertical"
    }

    def __init__(self):
        pass

    def get_color(self, color):
        return self.color[color]

    def get_orientation(self, orientation):
        return self.orientation[orientation]

# test
# def main():
#     a = Variable()
#     print(a.get_color(1))
#     print(a.get_orientation(1))


# if __name__ == "__main__":
#     main()

        
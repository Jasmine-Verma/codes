class Phone:
    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("making phonecall")
    def play_games(self):
        print("playing games")
     

p2=Phone()
p2.set_color("blue")
p2.set_cost("5,000")
p2.show_color()
p2.show_cost()
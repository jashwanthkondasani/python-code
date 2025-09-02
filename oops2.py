class nani:
    def __init__(self,n,o):
        self.name=n
        self.occupation=0
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"player tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots film")
    def speaks(self):
        print(self.name,"hi how are you")

jash=nani("jashwanth ","actor")
jash.do_work()
jash.speaks()

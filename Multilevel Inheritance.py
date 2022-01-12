class V():
    def __init__(self,caption):
        self.caption=caption


class I(V):
    def __init__(self,caption,Child):
        self.Child=Child
        V.__init__(self,caption)

class R(I):

    def __init__(self,caption,Child,tagline):
        self.tagline=tagline


        I.__init__(self,caption,Child)

    def Anushka(self):
        print("VIRAT KHOLI IS CALLED AS",self.caption)
        print("HE HAS A CUTE ANGEL NAMED",self.Child)
        print("ONE OF THE 'GOATS' OF THE GAME",self.tagline)



A=R("kING KHOLI","VAMIKA","Scoring runs for 'FUN'")
A.Anushka()


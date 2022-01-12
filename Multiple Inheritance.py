class V():
    def __init__(self,caption):
        self.caption=caption

class I():
    def __init__(self,Child):
        self.Child=Child

class R(V,I):

    def __init__(self,caption,Child,tagline):
        self.tagline=tagline

        V.__init__(self, caption)
        I.__init__(self,Child)

    def Anushka(self):
        print("VIRAT KHOLI IS CALLED AS",self.caption)
        print("HE HAS A CUTE ANGEL NAMED",self.Child)
        print("ONE OF THE 'GOATS' OF THE GAME",self.tagline)



A=R("kING KHOLI","VAMIKA","Scoring runs for 'FUN'")
A.Anushka()


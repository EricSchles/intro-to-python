#def greeting(name):
#    print "Hello "+name 
    
#greeting("Bianca")

class Butler:
    def __init__(self,master="Bianca"):
        self.master = master
        
    def greeting(self):
        print "Hello "+ self.master
        

class Jeeves(Butler):
        
    def clean(self,room="kitchen"):
        print "Yes "+ self.master+ ", I shall clean " + room
        
jeeves = Jeeves("Eric")
jeeves.greeting()
jeeves.clean()

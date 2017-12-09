@@ -0,0 +1,96 @@

eyeView=""

class Neur:
    

    def __init__(self):
        self.__init__(None)

    
    def __init__(self,out):
        self.fatigue=0
        self.out=out

    def tick(self):
        if(self.fatigue>0):
            self.fatigue=self.fatigue-1

    def stim(self):
        if(self.fatigue<2):
            self.fire()
            
        
    def fire(self):
        self.fatigue=self.fatigue+2
        self.out.stim()



class Motor():

    
    def __init__(self,outLetter):
        self.outLetter=outLetter



    def tick(self):
        pass

    def stim(self):
        # if(fatigue<2):
        self.fire()
        
    def fire(self):
        # self.fatigue=4
        print(self.outLetter),

        global eyeView
        eyeView=self.outLetter


m1=Motor("a")
n1=Neur(m1)


m2=Motor("b")
n2=Neur(m2)

u=[m1,n1, m2, n2]

def tickAll():
    global u, eyeView
    print "\n-",eyeView
    eyeView=""
    
    for o in u:
        o.tick()

seq="aabbaaaa"
print seq

for time in range(10):

    i=0

    if(i<len(seq)): 
        c=seq[i]       
        if c=="a":        
            n1.stim()
            if eyeView=="a":
                pass
            else:
                i=i-1

        if c=="b":        
            n2.stim()
            if eyeView=="b":
                pass
            else:
                i=i-1

        i=i+1
    
    tickAll()
    
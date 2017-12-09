
eyeView=""

class FingAction:
    

    def __init__(self):
        self.__init__(None)

    
    def __init__(self,out):
        self.fatigued=-2
        self.out=out

    def tick(self):
        if(self.fatigued>0):
            self.fatigued=self.fatigued-1

    def stim(self):
        if(self.fatigued<=0):
            self.fire()
            
        
    def fire(self):
        self.fatigued=self.fatigued+2
        self.out.stim()



class CompInput():

    
    def __init__(self,outLetter):
        self.outLetter=outLetter



    def tick(self):
        pass

    def stim(self):
        # if(fatigued<2):
        self.fire()
        
    def fire(self):
        # self.fatigued=4
        print(self.outLetter),

        global eyeView
        eyeView=self.outLetter


ci1=CompInput("a")
f1=FingAction(ci1)


ci2=CompInput("b")
f2=FingAction(ci2)

u=[ci1,f1, ci2, f2]

def tickAll():
    global u, eyeView
    print "-",
    # print "\n-",eyeView
    eyeView=""
    
    for o in u:
        o.tick()

seq="aabbaaaa"
print seq

i=0
for time in range(20):
    if(i<len(seq)): 
        shouldAdvance=True
        c=seq[i]   
        if c=="a":    
            if f1.fatigued>0:
                shouldAdvance=False
                pass
            else:    
                f1.stim()
        elif c=="b":        
            if f2.fatigued>0:
                shouldAdvance=False
                pass
            else:    
                f2.stim()
        
        if shouldAdvance:
            i=i+1
    
    tickAll()
    
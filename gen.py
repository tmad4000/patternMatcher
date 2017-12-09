import math

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


class Lens:
    @classmethod
    def project(cls,inp):
        pass

class RepLens(Lens):
    @classmethod
    def project(cls,inp):
        pass

class NeuralLens(Lens):
    @classmethod
    def project(cls,inp):
        pass


class PolymerLens(Lens):
    @classmethod
    def project(cls,inp):

        isPolymerOfDegN=True
        size=1
        for size in range(1,len(inp)/2+1):
            monomer=inp[0:size]
            print "*",monomer
            isPolymerOfDegN=True
            for i in range(0,len(inp),size):
                if inp[i:i+size] != monomer:
                    isPolymerOfDegN=False
                    break
    
            if isPolymerOfDegN:
                return size
    
        if isPolymerOfDegN:
            return size
        else:
            return 0

class PolymerLens2(Lens):
    @classmethod
    def project(cls,inp):

        isPolymerOfDegN=True
        size=1
        for size in range(1,len(inp)/2+1):
            monomer=inp[0:size]
            # print "*",monomer
            isPolymerOfDegN=True
            for i in range(0,len(inp),size):
                if inp[i:i+size] != monomer:
                    isPolymerOfDegN=False
                    break
    
            if isPolymerOfDegN:
                break
                
        if isPolymerOfDegN:
            # print len(inp)/size, "ddd"
            # return [sprintSeq(monomer)]*(len(inp)/size)
          return ['m']*(len(inp)/size)
        else:
            return ['m']
            
        #     return [None * len(inp)]
             
class PastKnowledgeLens(Lens):
    @classmethod
    def project(cls,inp):
        
        p="boogie"

        pSeq=strToNumSeq(p)

        # allPastKnowledge=[]
        occs=listIndexOfs(inp,pSeq)

        return occs
             

class IncrLens(Lens):
    
    @classmethod
    def project(cls,inp):
        diff=(inp[1])-(inp[0])

        for i in range(0,len(inp)-1):
            if (inp[i+1])-(inp[i]) != diff:
                return False
        
        return diff

class IncrLens2(Lens):
    
    @classmethod
    def project(cls,inp):
        return [(0 if i+1>=len(inp) else (inp[i+1])-(inp[i])) for i,c in enumerate(inp)] 

class QuadLens(Lens):
    
    @classmethod
    def project(cls,inp):
        return IncrLens2.project(IncrLens2.project(seq))
        
class SortedLens(Lens):
    
    @classmethod
    def project(cls,inp):
        return [(0 if i+1>=len(inp) else ((inp[i+1])>(inp[i]))) for i,c in enumerate(inp)] 


class FourierLens(Lens):
    
    @classmethod
    def project(cls,inp):
        pass


class AccLens(Lens):
    
    @classmethod
    def project(cls,inp):
        return [(0 if i+1>=len(inp) else (inp[i+1])+(inp[i])) for i,c in enumerate(inp)] 
        pass

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

#takes list data types, returns tuple showing matched range, [n,m)
def listIndexOfs(haystack,needle):
    matches=[]
    for i,x in enumerate(haystack):
        foundNeedle=True
        for j,y in enumerate(needle):
            if i+j > len(haystack) or haystack[i+j] !=y:
                foundNeedle=False
                break
        if foundNeedle:
            matches.append((i, i+len(needle)))

    return matches


def sprintSeq(s):
    return ''.join((" "+str(x) if x>=0 else str(x))  +""  for x in s)

def strToNumSeq(letterSeq):
    return [ord(c) for c in letterSeq]

letterSeq="aboogiebbabbboogie"
seq=strToNumSeq(letterSeq)
# seq=[math.sin(2*math.pi * x/10) for x in range(0,10)]
# seq=[1,0,1,0,1,0,1,0,1,0,1,0]

print letterSeq
print sprintSeq(seq), "SEQ"
# print sprintSeq(PolymerLens.project(seq)), "PolymerLens"
print sprintSeq(PolymerLens2.project(seq)), "PolymerLens2"
print sprintSeq(IncrLens2.project(seq)), "IncrLens2"
print sprintSeq(QuadLens.project(seq)), "QuadLens"
print sprintSeq(AccLens.project(seq)), "AccLens"
print sprintSeq(SortedLens.project(seq)), "SortedLens"
print sprintSeq(PastKnowledgeLens.project(seq)), "PastKnowledgeLens"

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
    
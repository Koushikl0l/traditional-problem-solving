
class ToH:
    def __init__(self,disk,rod):
        self.disk=disk
        self.rod1=rod
        self.rod2=[]
        self.rod3=[]
        self.odd=False
        self.even=False
        self.move=0

    def odd_or_even(self):
        if (self.disk)%2==0:
            self.even=True
            
        else:
            self.odd=True

    def even_iteration(self):
        for i in range(1):
            #make the legal move between pegs A and B (in either direction)
            if len(self.rod3)!=self.disk:
                if self.rod1==[] and self.rod2!=[]:
                    temp=self.rod2[len(self.rod2)-1]
                    self.rod1.append(temp)
                    self.rod2.pop()
                    print "B--------->A"
                    self.move+=1
                    break
            if self.rod2==[] and self.rod1!=[]:
                temp=self.rod1[len(self.rod1)-1]
                self.rod2.append(temp)
                self.rod1.pop()
                print "A--------->B"
                self.move+=1
                break
            if self.rod2!=[] and self.rod1!=[]:
                if self.rod2[len(self.rod2)-1]>self.rod1[len(self.rod1)-1]:
                    temp=self.rod1[len(self.rod1)-1]
                    self.rod2.append(temp)
                    print "A--------->B"
                    self.rod1.pop()
                    self.move+=1
                    break
                if self.rod1[len(self.rod1)-1]>self.rod2[len(self.rod2)-1]:
                    temp=self.rod2[len(self.rod2)-1]
                    self.rod1.append(temp)
                    print "B--------->A"
                    self.rod2.pop()
                    self.move+=1
                    break
    
        #make the legal move between pegs A and C (in either direction)
        for i in range(1):
          if len(self.rod3)!=self.disk :
            if self.rod1==[] and self.rod3!=[]:
                temp=self.rod3[len(self.rod3)-1]
                self.rod1.append(temp)
                print "C--------->A"
                self.rod3.pop()
                self.move+=1
                break
            if self.rod3==[] and self.rod1!=[]:
                temp=self.rod1[len(self.rod1)-1]
                self.rod3.append(temp)
                self.rod1.pop()
                print "A--------->C"
                self.move+=1
                break
            if self.rod3!=[] and self.rod1!=[]:
                if self.rod3[len(self.rod3)-1]>self.rod1[len(self.rod1)-1]:
                    temp=self.rod1[len(self.rod1)-1]
                    self.rod3.append(temp)
                    self.rod1.pop()
                    print "A--------->C"
                    self.move+=1
                    break
                if self.rod1[len(self.rod1)-1]>self.rod3[len(self.rod3)-1]:
                    temp=self.rod3[len(self.rod3)-1]
                    self.rod1.append(temp)
                    self.rod3.pop()
                    print "C--------->A"
                    self.move+=1
                    break
        for i in range(1):
          #make the legal move between pegs B and C (in either direction)
          if len(self.rod3)!=self.disk:
            if self.rod2==[] and self.rod3!=[]:
                temp=self.rod3[len(self.rod3)-1]
                self.rod2.append(temp)
                self.rod3.pop()
                print "C--------->B"
                self.move+=1
                break
            if self.rod3==[] and self.rod2!=[]:
                temp=self.rod2[len(self.rod2)-1]
                self.rod3.append(temp)
                self.rod2.pop()
                print "B--------->C"
                self.move+=1
                break
            if self.rod2!=[] and self.rod3!=[]:
                if self.rod2[len(self.rod2)-1]>self.rod3[len(self.rod3)-1]:
                    temp=self.rod3[len(self.rod3)-1]
                    self.rod2.append(temp)
                    self.rod3.pop()
                    print "C--------->B"
                    self.move+=1
                    break
                if self.rod3[len(self.rod3)-1]>self.rod2[len(self.rod2)-1]:
                    temp=self.rod2[len(self.rod2)-1]
                    self.rod3.append(temp)
                    self.rod2.pop()
                    print "B--------->C"
                    self.move+=1
                    break
            
    def odd_iteration(self):

        #make the legal move between pegs A and C (in either direction)
        for i in range(1):
          if len(self.rod3)!=self.disk : 
            if self.rod1==[] and self.rod3!=[]:
                temp=self.rod3[len(self.rod3)-1]
                self.rod1.append(temp)
                self.rod3.pop()
                print "C--------->A"
                self.move+=1
                break
            if self.rod3==[] and self.rod1!=[]:
                temp=self.rod1[len(self.rod1)-1]
                self.rod3.append(temp)
                self.rod1.pop()
                print "A--------->C"
                self.move+=1
                break
            if self.rod3!=[] and self.rod1!=[]:
                if self.rod3[len(self.rod3)-1]>self.rod1[len(self.rod1)-1]:
                    temp=self.rod1[len(self.rod1)-1]
                    self.rod3.append(temp)
                    self.rod1.pop()
                    print "A--------->C"
                    self.move+=1
                    break
                if self.rod1[len(self.rod1)-1]>self.rod3[len(self.rod3)-1]:
                    temp=self.rod3[len(self.rod3)-1]
                    self.rod1.append(temp)
                    self.rod3.pop()
                    print "C--------->A"
                    self.move+=1
                    break
        for i in range(1):
         #make the legal move between pegs A and B (in either direction)
         if len(self.rod3)!=self.disk:
            if self.rod1==[] and self.rod2!=[]:
                temp=self.rod2[len(self.rod2)-1]
                self.rod1.append(temp)
                self.rod2.pop()
                print "B--------->A"
                self.move+=1
                break
            if self.rod2==[] and self.rod1!=[]:
                temp=self.rod1[len(self.rod1)-1]
                self.rod2.append(temp)
                self.rod1.pop()
                print "A--------->B"
                self.move+=1
                break
            if self.rod2!=[] and self.rod1!=[]:
                if self.rod2[len(self.rod2)-1]>self.rod1[len(self.rod1)-1]:
                    temp=self.rod1[len(self.rod1)-1]
                    self.rod2.append(temp)
                    self.rod1.pop()
                    print "A--------->B"
                    self.move+=1
                    break
                if self.rod1[len(self.rod1)-1]>self.rod2[len(self.rod2)-1]:
                    temp=self.rod2[len(self.rod2)-1]
                    self.rod1.append(temp)
                    self.rod2.pop()
                    print "B--------->A"
                    self.move+=1
                    break
        for i in range(1):
         #make the legal move between pegs B and C (in either direction)
         if len(self.rod3)!=self.disk:
            if self.rod2==[] and self.rod3!=[]:
                temp=self.rod3[len(self.rod3)-1]
                self.rod2.append(temp)
                self.rod3.pop()
                print "C--------->B"
                self.move+=1
                break
            if self.rod3==[] and self.rod2!=[]:
                temp=self.rod2[len(self.rod2)-1]
                self.rod3.append(temp)
                self.rod2.pop()
                print "B--------->C"
                self.move+=1
                break
            if self.rod2!=[] and self.rod3!=[]:
                if self.rod2[len(self.rod2)-1]>self.rod3[len(self.rod3)-1]:
                    temp=self.rod3[len(self.rod3)-1]
                    self.rod2.append(temp)
                    self.rod3.pop()
                    print "C--------->B"
                    self.move+=1
                    break
                if self.rod3[len(self.rod3)-1]>self.rod2[len(self.rod2)-1]:
                    temp=self.rod2[len(self.rod2)-1]
                    self.rod3.append(temp)
                    self.rod2.pop()
                    print "B--------->C"
                    self.move+=1
                    break
    def do_operation(self,epoc):
        for iteration in range((2**epoc -1)/3+1):
            if self.even==True:
                self.even_iteration()
            else:
               self. odd_iteration()
    def solution(self):
        print "rod3:"+str(self.rod3)
        print "rod1:"+str(self.rod1)
        print "Total move:"+str(self.move)
if __name__=='__main__':
    disks=[6,5,4,3,2,1]
    t=ToH(len(disks),disks)
    t.odd_or_even()
    t.do_operation(len(disks))
    t.solution()
    

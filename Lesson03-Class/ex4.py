class Triangle:
    def printout(self,num):
        for i in range(num):
            for j in range(num - i):
                print('*',end='')
            print()

tri = Triangle()
tri.printout(9)
#not yet
class RelationException(Exception):
    def __init__(self,first,second):
        self.p1 = first
        self.p2 = second
    def __str__(self):
        return "Are you sure that " + self.p1 + " and " + self.p2 + " are in love with each other?"

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    '''try:
        if((relation[pa] or relation[pb]) == False):
            raise Exception
    except Exception:
        print("No relation found")
        raise RelationException(pa, pb)'''
    
    if relation[pa] != pb:
        raise RelationException(pa, pb)
        # TODO: raise exception
        # TIPS: 這個地方會需要 raise 兩種 exception
    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
except RelationException as e:
    print(e)
except Exception:
    print("No relation found")
    print("Are you sure that " + p1 + " and " + p2 + " are in love with each other?")

#it is an keyerror
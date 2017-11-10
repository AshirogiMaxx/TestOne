import copy

class StringProcessor(object):
    '''a class to process strings in various ways.'''
    def __init__(self, st):
        self._st = st
        
    def lowercase(self):
        self._st = self._st.lower()
        return self

    def uppercase(self):
        self._st = self._st.upper()
        return self

    def capitalize(self):
        self._st = self._st.capitalize()
        return self

    def delspace(self):
        self._st = self._st.replace(' ', '')
        return self

    def rep(self):
        return self._st

    def dup(self):
        return copy.deepcopy(self)

def process_string(s):
    print
    sp = StringProcessor(s)
    print 'Original:', sp.rep()
    print 'After uppercase:', sp.dup().uppercase().rep()
    print 'After lowercase:', sp.dup().lowercase().rep()
    print 'After uppercase:', sp.dup().uppercase().rep()
    print 'After uppercase then capitalize:', sp.dup().uppercase().capitalize().rep()
    print 'After delspace:', sp.dup().delspace().rep()

def main():
    print "Demo of method chaining in python:"
    # Use extra spaces between words to show effect pf delspace
    process_string('hOWz  It     GoInG?')
    process_string('The      QUIck   brOWn         fOx')

main()
    

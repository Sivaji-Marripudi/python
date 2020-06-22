class p1:
    def python(self):
        print('good knowledge')
    def java(self):
        print('not bad')
    def mysql(self):
        print('good')
class p2:
    def python(self):
        print('bad')
    def java(self):
        print('good knowledge')
    def mysql(self):
        print('good')
def knowledge_test(men):
    men.python()
def knowledge_test1(men):
    men.java()
siva = p1()
venkat = p2() 
knowledge_test1(siva)
knowledge_test1(venkat)
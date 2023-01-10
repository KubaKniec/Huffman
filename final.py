import heapq

class n:
    def __init__(self, iloscLiter, znak, lewo=None, prawo=None):
        self.iloscLiter = iloscLiter
        self.znak = znak
        self.lewo = lewo
        self.prawo = prawo
        self.huff = ''

    def __lt__(self, a):
        return self.iloscLiter < a.iloscLiter

def printns(n, wart=''):
    nowaWartosc = wart + str(n.huff)
    if (n.prawo):
        printns(n.prawo, nowaWartosc)
    if (n.lewo):
        printns(n.lewo, nowaWartosc)

    if (not n.prawo and not n.lewo):
        print(f"{n.znak} -> {nowaWartosc}")

iloscLiter = [1, 2, 3, 1, 1, 1, 2, 1, 1]
#a s e m b l e r s u p e r
#1 2 3 1 1 1 2 1 1
litery = ['a', 's', 'e', 'm', 'b', 'l', 'r','u','p']
wezly = []

for l in range(len(litery)):
    heapq.heappush(wezly, n(iloscLiter[l], litery[l]))

while len(wezly) > 1:
    lewo = heapq.heappop(wezly)
    prawo = heapq.heappop(wezly)
    lewo.huff = 0
    prawo.huff = 1
    newn = n(lewo.iloscLiter + prawo.iloscLiter, lewo.znak + prawo.znak, lewo, prawo)
    heapq.heappush(wezly, newn)

printns(wezly[0])

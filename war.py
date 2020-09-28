from cards import *
ntrials=10000
result=[]
for i in range(ntrials):
    p1deck=deck()
    p2deck=deck()
    p1deck.shuffle()
    p2deck.shuffle()
    p1score=0
    p2score=0
    while p1deck.cardsleft()>0:
        p1card1=p1deck.dealcard()
        p2card1=p2deck.dealcard()
        if p1card1.value()>p2card1.value():
            p1score+=2
        if p1card1.value()<p2card1.value():
            p2score+=2
        if p1card1.value()==p2card1.value():
            p1score+=1
            p2score+=1
    if p1score>p2score:
        result.append(p1score-p2score)
    if p1score<p2score:
        result.append(p2score-p1score)
    if p1score==p2score:
        result.append(p1score-p2score)
print("0", result.count(0)/ntrials)
print("2", result.count(2)/ntrials)
print("4", result.count(4)/ntrials)
print("6", result.count(6)/ntrials)
print("8", result.count(8)/ntrials)
print("10", result.count(10)/ntrials)
print("12", result.count(12)/ntrials)
print("14", result.count(14)/ntrials)
print("16", result.count(16)/ntrials)
print("18", result.count(18)/ntrials)
print("20", result.count(20)/ntrials)
print("22", result.count(22)/ntrials)
print("24", result.count(24)/ntrials)
print("26", result.count(26)/ntrials)
print("28", result.count(28)/ntrials)
print("30", result.count(30)/ntrials)
print("32", result.count(32)/ntrials)
print("34", result.count(34)/ntrials)
print("36", result.count(36)/ntrials)
print("38", result.count(38)/ntrials)
print("40", result.count(40)/ntrials)
print("42", result.count(42)/ntrials)
print("44", result.count(44)/ntrials)
print("46", result.count(46)/ntrials)
print("48", result.count(48)/ntrials)
print("50", result.count(50)/ntrials)
print("52", result.count(52)/ntrials)
    

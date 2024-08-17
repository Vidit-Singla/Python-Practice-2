class Fighter:

    def __init__(self,name,health,attack_per):
        self.name = name
        self.health = health
        self.attack_per = attack_per

    def __attack__(self,opponent):
        opponent.health-=self.attack_per

def fight(a,b,n1):
    if a.name == n1:
        attacker = a 
    if attacker==a:
        defender = b 

    while a.health>0 and b.health>0:
        attacker.__attack__(defender)
        if defender.health<=0:
            return (attacker.name+' Won')
        return (defender.health, defender.name)
        return (attacker.health, attacker.name)
        attacker,defender=defender,attacker


fighter1 = Fighter('Jake Paul',50,5)
fighter2 = Fighter('Mike Tyson',45,8)

print(fight(fighter1,fighter2,'Jake Paul'))

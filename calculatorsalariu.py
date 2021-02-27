name = input("Enter your name: ")
days = float(input("How many days did you work thin month?: "))
salary = float(input("Your salary per hour?: "))
ore = float(input("How hours per day?: "))

salariu_brut = (salary*ore)*days
transport = salariu_brut* 0.15
sporuri = salariu_brut* 0.20
taxe_impozite = salariu_brut*0.06

salariu_net = salariu_brut+transport+sporuri-taxe_impozite

if salariu_net > 1000:
    print("Congrats" + " " + name + " " + " your work was worth it!")
else:
    print("Keep working" + " " + name + " " + "you're on the right way!")

print("Your net salary is" + " " + str(salariu_net))

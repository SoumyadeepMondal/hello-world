import secrets
avengers=['CaptainAmerica','IronMan','Thor','Hulk','Vision','BlackWidow','ScarletWitch','CaptainMarvel','Hawkeye','BlackPanther','QuickSilver','DoctorStrange','Nebula','Gamora','StarLord','Drax','Mantis','Rocket','Groot','AdamWarlock','AntMan','Deadpool']
def level(avng):
    if avng=='Thor' or avng=='AdamWarlock' or avng=='CaptainMarvel' or avng=='ScarletWitch' or avng=='Hulk':
        return 5
    elif  avng=='IronMan' or avng=='Vision' or avng=='Antman' or avng=='DoctorStramge' or avng=='Deadpool':
        return 4
    elif avng=='CaptainAmerica' or avng=='BlackPanther' or avng=='Nebula' or avng=='Gamora' or avng=='QuickSilver' or avng=='StarLord':
        return 3
    else:
        return 2
flag=1
while flag:
    avng1=secrets.choice(avengers)
    avng2=secrets.choice(avengers)
    if avng1!=avng2:
        flag=0
print(avng1,avng2)
rate1=level(avng1)
rate2=level(avng2)
print('enter two more avengers')
avng3=input()
rate3=level(avng3)
avng4=input()
rate4=level(avng4)
plvl= rate1+rate2+rate3+rate4
print("you have chosen the following AVENGERS: ", avng1, avng2, avng3, avng4)
print('power level of thanos is 17 and power level of your team is: ', plvl)
if plvl>=17:
    print('Congrats you saved the universe!')
else:
    print('thanos killed half the universe!')
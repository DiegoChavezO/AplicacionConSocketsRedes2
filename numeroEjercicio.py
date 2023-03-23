#numero de días de he vivido hasta 8 de marzo del 2023
#29 de octubre del 2000 fue el día en que nací
#el año 2000 y sus sumas de 4 son años biciestos
import tkinter as tk
myYear = 2000
myMont = "octubre"
myDay = 29
thisYear = 2023
thisMont = "marzo"
thisDay = 8
year = 365
months = {"enero":31,"febrero":28,"marzo":31,"abril":30,"mayo":31,"junio":30,"julio":31,"agosto":30,"sepriembre":31,"octubre":31}
game = {0:"buscaminas",1:"gato dummy", 2:"memoria"}

def isyearleap(year):
    if(year%4==0):
        return True
    else:
        return False
    
def YearsLived(myYear,thisYear,year):
    j=0
    daysLivedperYear=0
    for i in range(myYear+1,thisYear):
        j=j+1
        if(j%4==0):
            year = 366
            daysLivedperYear = daysLivedperYear + year
        else:
            year = 365
            daysLivedperYear = daysLivedperYear + year
    #daysLivedperYear = daysLivedperYear + 1 esto puede que lo utilice despues
    return daysLivedperYear
    
def dayAlmostaYear(myMont,months,myDay):
    daysLivedAlmostMonth=0
    for k in months:
        if(k == myMont):
            break
        daysLivedAlmostMonth = daysLivedAlmostMonth + months[k]
    daysLivedAlmostMonth = daysLivedAlmostMonth+myDay
    return daysLivedAlmostMonth
 
yearsLivedperYear = YearsLived(myYear,thisYear,year)
daysLivedfirstYear = abs(dayAlmostaYear(myMont,months,myDay) - 365)#estoy sacando el complemento para el primer año
daysLivedLastYear = dayAlmostaYear(thisMont,months,thisDay)     
totalDaysLived = daysLivedfirstYear + daysLivedLastYear + yearsLivedperYear
game_index = (totalDaysLived)%3
window = tk.Tk()
icono = tk.PhotoImage(file='icono.png')
window.title("Números de días")
window.iconphoto(False,icono)
mensaje = tk.Label(window,text=f"el número total de días que has vivido desde {myDay}/{myMont}/{myYear} hasta {thisDay}/{thisMont}/{thisYear} es : {totalDaysLived}",font=("Arial",20),bg="white", fg="blue", bd=2, relief="solid")
mensaje2 = tk.Label(window,text=f"El ejercicio que voy a hacer de jueguito es el número {game_index} : {game[game_index]}",font=("Arial",20),bg="white", fg="blue", bd=2, relief="solid")
mensaje.pack()
mensaje2.pack()
window.mainloop()
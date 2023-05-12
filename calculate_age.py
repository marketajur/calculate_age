from datetime import date
 
def calculateAge(birthDate):
    date_vykaz = date(1995, 1, 3)
    age = date_vykaz.year - birthDate.year - ((date_vykaz.month, date_vykaz.day) 
                                    <(birthDate.month, birthDate.day))
 
    return age
     
# Driver code
print(calculateAge(date(1992, 7, 3)), "years")
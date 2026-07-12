#Notes
#GOALS
"""
 Write entry: Done
 Check entry: Done
 Exit: Done
 Delete entry: Pending
"""

"""
fileExists = file with text
diaryExists = the text
"""
#Diary format !
"""<EntryStart:{formattedDate}_{lastSerialNumberPlusOne()}>
                    {diaryInput}
                        </EntryEnd:{formattedDate}_{lastSerialNumberPlusOne()}> """

#Imports
from datetime import date


#Function

def readDiary():
    with open("text.txt", "r") as f:
        return f.read()
    


def formatForDateNumberChecker(LOCALdateNumberHolder):
        #return True or False
    day, month, yearPlusNumber = LOCALdateNumberHolder.split("/")
    year, number = yearPlusNumber.split("_")
    if (day).isdigit() and (month).isdigit() and (year).isdigit() and (number).isdigit():
        if len((day)) <3 and len((month)) <3 and len((year)) == 4:
            if int(day) < 32 and int(month) < 13 and int(year) > 2025:
                return(True)
            else:
                return(False)
        else:
            return(False)  
    else:
        return(False)

def lastSerialNumberPlusOne():
    diary = readDiary()
    highest = 1
    try:
        if not diary:
            return(highest)
        
        else:
            for lines in diary.splitlines():
                parts = lines.split()
                for part in parts:
                    if part.startswith(f"<EntryStart:{formattedDate}"):
                        numberPlusExtra = part.split("_")[1]
                        number = int(numberPlusExtra.split(">")[0])
                        if number > highest:
                            highest = number
        
            return(highest+1)
    except ValueError:
        return(highest)
                    

        

#Extras

today = date.today()
formattedDate = today.strftime("%d/%m/%Y")



#Step one- Check if doesn't file exits or is empty.. FILE NAME = text.txt

try:
    with open("text.txt", "r") as f:
        diary = f.read()
        fileExists = True
    if not diary:
        diaryExists = False
    else:
        diaryExists = True
except Exception:
    fileExists = False
    diaryExists = False

if diaryExists == False:
    while True:
        choicer = input("""Past enteries do not exist.
                    Would you like to write a new entry or exit? ('write' or 'exit')
                     > """)
        if choicer.lower().strip() ==  "write" or choicer.lower().strip() == "exit":
            if choicer == "exit":
                exit()
            else:
                break
        else:
            print("Invalid input. Please enter 'write' or 'exit'.")
            continue
            
else:
    while True: 
        choicer = input("""Past enteries exist.
                    Would you like to write a new entry, check a past entry, delete a past entry or exit? ('write', 'check', 'delete'  or 'exit')
                     > """)
        if choicer.lower().strip() ==  "write" or choicer.lower().strip() == "exit" or choicer.lower().strip() == "check" or choicer.lower().strip() == "delete":
            if choicer == "exit":
                exit()
            elif choicer == "check":
                while True:
                    dateForChecking = input("Please enter the date and number of the diary you want to check in this format: ' DD/MM/YYYY_serial number: ")
                    diary = readDiary()
                    if formatForDateNumberChecker(dateForChecking):
                        try:
                            start = diary.find(f"<EntryStart:{dateForChecking}>")
                            end = diary.find(f"</EntryEnd:{dateForChecking}>")
                            text = diary[start+len(f"<EntryStart:{dateForChecking}>"):end]
                            print(f"""Here's your entry:
                                  > {text}""")
                            break
                        except Exception:
                            print("Invalid input.")
                            continue
                    else:
                        print("Invalid input, try again.")
                        continue
            elif choicer == "delete":
                dateForChecking = input("Please enter the date and number of the diary you want to delete in this format: ' DD/MM/YYYY_serial number: ")
                diary = readDiary()
                if formatForDateNumberChecker(dateForChecking):
                    try:
                        start = diary.find(f"<EntryStart:{dateForChecking}>")
                        end = diary.find(f"</EntryEnd:{dateForChecking}>")
                        if start == -1 and end == -1:
                            print("Invalid input.")
                            continue
                        print(start, end)
                        text = diary[:start] + diary[end+len(f"</EntryEnd:{dateForChecking}>"):]
                        with open("text.txt", 'w') as f:
                            f.write(text)
                            print(f"{dateForChecking} has been deleted.")
                    except ValueError:
                        print("Invalid input.")
                        continue

            else:
                # Write diary

                diaryInput = input("""Please write your diary here\n> """)
                serialNumber = lastSerialNumberPlusOne()
                diaryEntryAppend = f"""\n<EntryStart:{formattedDate}_{serialNumber}>\n{diaryInput}\n</EntryEnd:{formattedDate}_{serialNumber}>\n """

                with open("text.txt", 'a') as f:
                    f.write(diaryEntryAppend)
                
        else:
            print("Invalid input. Please enter 'write', 'check', 'delete' or 'exit.")
            continue
            


                

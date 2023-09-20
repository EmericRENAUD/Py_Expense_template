from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]



def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)

    with open('users.csv', mode='a', newline='') as fichier_csv:
        writer=csv.writer(fichier_csv)
        data = [infos['name']]
        writer.writerow(data)
    
    print("User Added !")
    return
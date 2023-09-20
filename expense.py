from PyInquirer import prompt
import csv
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]

#Convertis le csv des users en liste
def getUsers():
    with open('users.csv', mode='r', newline='') as users_csv:
        reader = csv.reader(users_csv)
        user_list = []
        for line in reader:
            user_list.append(line[0])
    return user_list

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    with open('expense_report.csv', mode='a', newline='') as fichier_csv:
        writer=csv.writer(fichier_csv)

        # Check if the User exists
        with open('users.csv', mode='r') as users_csv:
            reader= csv.reader(users_csv)
            for line in reader: 
                #Add Expense if the User exists
                if (str(infos['spender']) == line[0]):
                    user_list = getUsers()
                    
                    #Remove the spender from the list
                    user_list.remove(line[0])

                    involved_users = [
                    {
                        "type": "checkbox",
                        "name": "choice",
                        "message": "Select involved users (press space to check):",
                        "choices": [{"name": user} for user in user_list],
                    },
                    ]

                    involved=prompt(involved_users)

                    #The first user name will always be the Spender.
                    data = [infos['amount'], infos['label'], infos['spender'], involved['choices']]
                    print("User: ", infos['spender'], " found!")
                    writer.writerow(data)
                    print("Expense Added !")
                    return True
    #print(infos)
    print("Spender is not registered yet. Please add a new User.")
    return False



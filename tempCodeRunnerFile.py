def process():
    with open("mylife.txt", "w") as mylife_file:
        insert_line = input("How was you day today? What are your realizations?")
        mylife_file.write(insert_line)
        print(insert_line)
        question_usr = input("Are there any more realizations for today? Enter Y for yes and N for no: ")
        if question_usr == "Y":
            question_usr = question_usr.upper()
            print (question_usr)
        else:
            quit
    mylife_file.close()
points = 0


def QuizGame():

    print("Witam pedale, chcesz rozpocząć quiz? (20 pytań) \n a)tak \n b)nie ")
    print("-------------------------------------------------")
    playing = input()
    if playing != "a":
        print("Zła odpowiedź, jesteś dupsonem")
        print("-------------------------------------------------")
        quit()
#Pytanie numer 1
    question = "1. Kto zazwyczaj jest ostatni w tabeli? \n a) Adolf \n b) Biogozon \n c) Cinuszek \n d) Dupson "
    print("-------------------------------------------------")
    print(question)
    print("-------------------------------------------------")
    answer = input().capitalize()
    if answer != "D":
        print("Niepoprawna odpowiedź, beka z ciebie")
        print("-------------------------------------------------")
        quit
    if answer == "D":
        points + 1
#Pytanie numer 2
    question1 = "2. Jaka postać jest najniższa? \n a) Jett \n b) Neon \n c) Reyna \n d) Baluszek"
    print("-------------------------------------------------")
    print(question1)
    print("-------------------------------------------------")
    answer1 = input().capitalize()
    if answer1 != "B":
        print("-------------------------------------------------")
        print("No chyba nie")
        print("-------------------------------------------------")
        quit()
    if answer1 == "B":
        points + 1
#Pytanie numer 3
    question2 = "3. Jakie była jedna z pierwszych map? Odpowiedź otwarta"
    print("-------------------------------------------------")
    print(question2)
    print("-------------------------------------------------")
    answer2 = input().capitalize()
    #Błędna odpowiedź
    if answer2 != ("Split"):
        if answer2 != ("Bind"):
            if answer2 != ("Haven"):
                print("Siur odpowiedź")
                print("-------------------------------------------------")
                quit()
    #Prawidłowa odpowiedź
    if answer2 == ("Split"):
        if answer2 == ("Bind"):
            if answer2 == ("Haven"):
                points + 1
#Pytanie numer 4
    question3 = "4. Która postać jest z Rosji? a) Jett \n b) Yoru \n c) Sova \n d) OmkoTV "
    print(question3)
    print("-------------------------------------------------")
    answer3 = input().capitalize()
    if answer3 != ("C"):
        if answer3 != "D":
            print("Chyba nie zjesz dzisiaj bigosu...")
            print("-------------------------------------------------")
            quit()
    if answer == "C":
        points + 1

#Pytanie numer 5
    question4 = "5. Jaka mapa znajduje się we Włoszech? Odpowiedź otwarta. "
    print(question4)
    print("-------------------------------------------------")
    answer4 = input().capitalize()
    if answer4 != ("Ascent"):
        print("No chyba nie")
        quit()
    if answer4 == ("Ascent"):
        points + 1
    

print(points)
        
QuizGame()



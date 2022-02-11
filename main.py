
lines = ("-------------------------------------------------")

def QuizGame():
    points = 0
    questions = 20
    print("Witam pedale, chcesz rozpocząć quiz? (20 pytań) \n a)tak \n b)nie ")
    print(lines)
    playing = input()
    if playing != "a":
        print("Zła odpowiedź, jesteś dupsonem")
        print(lines)
        quit()
    # Pytanie numer 1
    question = "1. Kto zazwyczaj jest ostatni w tabeli? \n a) Adolf \n b) Biogozon \n c) Cinuszek \n d) Dupson "
    print(lines)
    print(question)
    print(lines)
    answer = input().capitalize()
    if answer != "D":
        print("Niepoprawna odpowiedź, beka z ciebie")
        print(lines)
        quit()
    if answer == "D":
        points += 1
    # Pytanie numer 2
    question1 = "2. Jaka postać jest najniższa? \n a) Jett \n b) Neon \n c) Reyna \n d) Baluszek"
    print(lines)
    print(question1)
    print(lines)
    answer1 = input().capitalize()
    if answer1 != "B":
        print(lines)
        print("No chyba nie")
        print(lines)
        quit()
    if answer1 == "B":
        points += 1
    # Pytanie numer 3
    question2 = "3. Jakie była jedna z pierwszych map? Odpowiedź otwarta"
    print(lines)
    print(question2)
    print(lines)
    answer2 = input().capitalize()
    # Błędna odpowiedź
    if answer2 != ("Split"):
        if answer2 != ("Bind"):
            if answer2 != ("Haven"):
                print("Siur odpowiedź")
                print(lines)
                quit()
    # Prawidłowa odpowiedź
    if answer2 == ("Split"):
        if answer2 == ("Bind"):
            if answer2 == ("Haven"):
                points += 1
    # Pytanie numer 4
    print(lines)
    question3 = "4. Która postać jest z Rosji? \n a) Jett \n b) Yoru \n c) Sova \n d) OmkoTV "
    print(question3)
    print(lines)
    answer3 = input().capitalize()
    if answer3 != ("C"):
        if answer3 != "D":
            print("Chyba nie zjesz dzisiaj bigosu...")
            print(lines)
            quit()
    if answer3 == "C":
        points += 1

    # Pytanie numer 5
    print(lines)
    question4 = "5. Jaka mapa znajduje się we Włoszech? Odpowiedź otwarta. "
    print(question4)
    print(lines)
    answer4 = input().capitalize()
    if answer4 != ("Ascent"):
        print("No chyba nie")
        quit()
    if answer4 == ("Ascent"):
        points += 1

    print("twoja liczba punktów to: ", int(points), ", czyli jest to:", int(points ) /questions * 100, "% całości wyniku")

QuizGame()
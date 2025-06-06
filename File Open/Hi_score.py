import random as r
def game():
    Score_set= r.randint(1,190)
    print("Game Has Ended")
    return Score_set
with open("Hi_Score.txt","r+")as f:
    c=f.read()
    c=str(c)
    word=c.split()
    High_score=int(word[-1])
    High_score1=game()
    print(f"Thank You for Playing game You have Score {High_score1}")
    if High_score1>High_score:
        f.truncate()
        f.seek(0)
        c="The New High Score is :-  "
        f.write(c+str(High_score1))
        print("Score Change succesfully")
    else :
        print(f"Sorry High score Has not been betten High Score is {High_score} and your is {High_score1}")        
answer1=raw_input("What is the capital of Peru?")
if answer1=="Lima":
    print "Correct!"
else:
    print "Sorry, that is not the correct answer."
    
answer2=raw_input("What country does Evita not want us to cry for?")
if answer2=="Argentina":
    print "Correct!"
else:
    print "Sorry, that is not the correct answer."
    
answer3=raw_input("What country hosts the world's largest Carnaval celebration every year?")
if answer2=="Brazil" or "Brasil":
        print "Correct!"
else:
    print "Sorry, that is not the correct answer."


if answer1=="Lima":
    score1=1
else:
        score1=0
if answer2=="Argentina":
    score2=1
else:
    score2=0
if answer3=="Brazil" or "Brasil":
    score3=1
else:
    score3=0
total_score= score1+score2+score3
print "You scored",total_score,"out of 3"
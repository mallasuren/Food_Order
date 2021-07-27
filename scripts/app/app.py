adjective = input("Enter adjective word: ")
while adjective.isalpha() != True:
    adjective = input("Your input is wrong can you enter adjective word again: ")

city_name = input("Enter any city name: ")
while city_name.isalpha() != True:
    city_name = input("Your input is wrong can you enter any city name again: ")

noun = input("Enter noun: ")
while noun.isalpha() != True:
    noun = input("Your input is wrong can you please enter noun again: ")

second_noun = input("Enter second noun: ")
while second_noun.isalpha() != True:
    second_noun = input("Your input is wrong can you please enter second noun again: ")

third_noun = input("Enter third_noun: ")
while third_noun.isalpha() != True:
    third_noun = input("Your input is wrong can you please enter third noun again: ")

fourth_noum = input("Enter fourth_noun: ")
while fourth_noum.isalpha() != True:
    fourth_noum = input("Your input is wrong can you please enter fourth noun again: ")

action_verb = input("Enter action_verb: ")
while action_verb.isalpha() != True:
    action_verb = input("Your input is wrong can you please enter action verb again: ")

sport_noun = input("Enter sport_noun: ")
while sport_noun.isalpha() != True:
    sport_noun = input("Your input is wrong can you please enter sport noun again: ")

place = input("Enter place name: ")
while place.isalpha() != True:
    place = input("Your input is wrong can you please enter place name again: ")

food_one = input("Enter food name: ")
while food_one.isalpha() != True:
    food_one = input("Your input is wrong can you please enter food name again: ")

food_two = input("Enter another food name: ")
while food_two.isalpha() != True:
    food_two = input("Your input is wrong can you please enter another food name again: ")

drink_one = input("Enter drink name: ")
while drink_one.isalpha() != True:
    drink_one = input("Your input is wrong can you please enter drink name again: ")

drink_two = input("Enter another drink name: ")
while drink_two.isalpha() != True:
    drink_two = input("Your input is wrong can you please enter another drink name again: ")


story = (
            "One day my " + adjective + " friend and I decided to go to the " + sport_noun + " game in " + city_name +". " + 
            "We really wanted to see the "+ noun +" play the " + second_noun +". " +
            "So, we " + action_verb + " our " + third_noun + " down to the " + place + " and bought some " + fourth_noum + "s. " +
            "We got into the game and it was a lot of fun." +
            "We ate some " + food_one + " , " + food_two + " and drank some " + drink_one + " , " + drink_two + "." +
            "We had a great time! We plan to go ahead next year!"
        )
print (story)
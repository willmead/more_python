"""

Rude Chatbot

If you ask Bob a question (e.g. How are you?) he will reply "Sure"
(The last element in a list is user_message[-1])

If shout at Bob (e.g. HELLO) he will reply "Whoa, chill out"
(you can check if a string is capital by using user_message.isupper()

If you shout a question at him (e.g. HOW ARE YOU?) he will
reply "Calm down, I know what I'm doing"

(remember, if we want to check two conditions, we say if condition1 and condition2:)

If you send an empty message " " he says "fine, be that way"

Anything else, he will reply "Whatever"

"""

while True:
    user_message = input("> ")

    if user_message[-1] == "?" and user_message.isupper():
        print("Calm down, I know what I'm doing")
    elif user_message[-1] == "?":
        print("Sure")
    elif user_message.isupper():
        print("Whoa, chill out")
    elif user_message == "":
        print("Fine, be that way")
    else:
        print("Whatever...")


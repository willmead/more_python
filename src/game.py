import random
import operator

with open('high_score.txt', 'r') as reader:
    high_score = int(reader.read())

print(f"HIGH SCORE: {high_score}")

OPERATIONS = {"+": operator.add,
              "-": operator.sub,
              "*": operator.mul
              }
    
score = 0

for round in range(1, 5):
    print()
    print(f"Round {round} out of 10")
    
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation_str, operation = random.choice(list(OPERATIONS.items()))
    
    answer = int(input(f"{number1} {operation_str} {number2} = "))

    if answer == (operation(number1, number2)):
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    
print(f"Final Score: {score} / 10")

if score > high_score:
    with open('high_score.txt', 'w') as writer:
        writer.write(str(score))

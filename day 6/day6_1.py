with open('input.txt') as f:
    inputl = f.read()

groups = inputl.split('\n\n')
sum = 0
for group in groups:
    questions = set()
    for person in group.splitlines():
        for question in person:
            questions.add(question)
    sum += len(questions)

print(sum)

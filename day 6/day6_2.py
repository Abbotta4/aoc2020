with open('input.txt') as f:
    inputl = f.read()

groups = inputl.split('\n\n')
sum = 0
for group in groups:
    questions = []
    people = group.splitlines()
    for question in people[0]:
        present = True
        for person in people[1:]:
            if question not in person:
                present = False
                break
        if present:
            questions.append(question)
    sum += len(questions)

print(sum)

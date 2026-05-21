matrix = []

text = "7iiTsxh%?i #sM $a #t%^r!"

contextual_list = []

# Building the matrix
for (index, element) in enumerate(text):
    contextual_list.append(element)
    # every 3 characters
    if (index + 1) % 3 == 0:
        matrix.append(contextual_list)
        contextual_list = []
print(matrix)
message = ""
number_of_columns = len(matrix[0])

for column in range(number_of_columns):
    for row in range(len(matrix)):
        current_character = matrix[row][column]
        if current_character.isalpha():
            message += current_character
        # replace symbols between letters by a space
        elif len(message) > 0 and message[-1] != " ":
            message += " "
# remove useless spaces at the beginning/end
message = message.strip()

print(message)
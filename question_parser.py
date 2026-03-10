import re

def parse_questions(text):

    questions = []

    lines = text.split("\n")

    current_question = ""

    for line in lines:

        line = line.strip()

        # Detect question numbers like "1", "1.", "1)"
        if re.match(r'^\d+[\.\)]?\s+', line):

            if current_question:
                questions.append(current_question.strip())

            current_question = line

        else:
            if current_question:
                current_question += " " + line

    if current_question:
        questions.append(current_question.strip())

    return questions
scores = {
    "Biologist": 0,
    "Full Stack": 0,
    "AI": 0,
    "Engineer": 0,
    "Educator": 0,
    "Physicist": 0,
    "Physician": 0,
}

questions = [
    [
        "What is your ideal schedule?",
        ["Work remotely", "Work in person", "Work with others"],
        [
            ["AI", "Full Stack"],
            ["Biologist", "Engineer", "Physicist"],
            ["Physician", "Educator"],
        ]
    ],
    [
        "Out of these traits, which describes you best?",
        ["Logical", "Creative", "Tactile", "Helpful"],
        [
            ["Physicist", "AI", "Biologist"],
            ["Full Stack"],
            ["Engineer"],
            ["Educator", "Physician"],
        ]
    ],
    [
        "What sounds like the best way to spend a Saturday?",
        ["Taking things apart and building new things", "Volunteering or helping someone", "Researching and exploring new concepts"],
        [
            ["Engineer", "AI", "Full Stack"],
            ["Educator", "Physician"],
            ["Physicist", "Biologist"],
        ]
    ],
    [
        "What school subject do you look forward to most?",
        ["Math", "Science", "Computer Science", "English / Social Studies"],
        [
            ["Physicist", "AI", "Engineer"],
            ["Biologist", "Physicist", "Physician"],
            ["AI", "Full Stack"],
            ["Educator"],
        ]
    ],
    [
        "What do you look for in future career opportunities?",
        ["Helping others", "High salary", "Creating things", "Discovering new things"],
        [
            ["Educator", "Physician"],
            ["AI", "Engineer", "Full Stack"],
            ["Engineer", "Full Stack"],
            ["Biologist", "Physicist"],
        ]
    ],
    [
        "How do you prefer to solve problems?",
        ["Use formulas and calculations",
         "Write code to create a program",
         "Operate tests and experiments",
         "Converse in groups"],
        [
            ["Engineer", "Physicist", "AI"],
            ["AI", "Full Stack"],
            ["Biologist", "Physicist", "Physician"],
            ["Biologist", "Physicist", "Educator"],
        ]
    ],
    [
        "What problem would you like to solve the most?",
        ["How to make life easier with technology?",
         "How to make safer tools and products?",
         "How to help others and create new solutions?",
         "How can education and training help people?"],
        [
            ["Full Stack", "AI"],
            ["Engineer"],
            ["Physician", "Biologist", "Physicist"],
            ["Educator"],
        ]
    ],
]


for i, q in enumerate(questions):
    question_text = q[0]
    options = q[1]
    careers_maps = q[2]

    print(f"\nQuestion {i+1} of {len(questions)}")
    print(f"\n {question_text}\n")

    for j, option in enumerate(options):
        print(f" {j+1}. {option}")
    while True:
        try:
            choice = int(input("Your choice: "))
            if 1 <= choice <= len(options):
                break
            print(f"Enter 1-{len(options)}.")
        except ValueError:
            print("Enter a number")

    for career in careers_maps[choice - 1]:
        scores[career] += 1

finalChoice = max(scores, key=scores.get)
print(f"\nYour best match: {finalChoice}")

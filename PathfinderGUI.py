import FreeSimpleGUI as sg

# Dictionary to track the user's score for each career
scores = {
    "Biologist": 0, "Full Stack": 0, "AI": 0, "Engineer": 0,
    "Educator": 0, "Physicist": 0, "Physician": 0,
}

# List of questions. Each question contains:
# Index 0: The question string
# Index 1: The multiple-choice options
# Index 2: The careers associated with each option
questions = [
    [
        "What is your ideal schedule?",
        ["Work remotely", "Work in person", "Work with others"],
        [["AI", "Full Stack"], ["Biologist", "Engineer", "Physicist"], ["Physician", "Educator"]],
    ],
    [
        "Out of these traits, which describes you best?",
        ["Logical", "Creative", "Tactile", "Helpful"],
        [["Physicist", "AI", "Biologist"], ["Full Stack"], ["Engineer"], ["Educator", "Physician"]],
    ],
    [
        "What sounds like the best way to spend a Saturday?",
        ["Taking things apart and building new things", "Volunteering or helping someone", "Researching and exploring new concepts"],
        [["Engineer", "AI", "Full Stack"], ["Educator", "Physician"], ["Physicist", "Biologist"]],
    ],
    [
        "What school subject do you look forward to most?",
        ["Math", "Science", "Computer Science", "English / Social Studies"],
        [["Physicist", "AI", "Engineer"], ["Biologist", "Physicist", "Physician"], ["AI", "Full Stack"], ["Educator"]],
    ],
    [
        "What do you look for in future career opportunities?",
        ["Helping others", "High salary", "Creating things", "Discovering new things"],
        [["Educator", "Physician"], ["AI", "Engineer", "Full Stack"], ["Engineer", "Full Stack"], ["Biologist", "Physicist"]],
    ],
    [
        "How do you prefer to solve problems?",
        ["Use formulas and calculations", "Write code to create a program", "Operate tests and experiments", "Converse in groups"],
        [["Engineer", "Physicist", "AI"], ["AI", "Full Stack"], ["Biologist", "Physicist", "Physician"], ["Biologist", "Physicist", "Educator"]],
    ],
    [
        "What problem would you like to solve the most?",
        ["How to make life easier with technology?", "How to make safer tools and products?", "How to help others and create new solutions?", "How can education and training help people?"],
        [["Full Stack", "AI"], ["Engineer"], ["Physician", "Biologist", "Physicist"], ["Educator"]],
    ],
]

# =============================================
# PATHWAY CONTENT
# =============================================

pathways = {
    "Full Stack": {
        "title": "Full Stack Developer",
        "description": (
            "A full stack web-developer develops both frontend and backend software. "
            "Frontend includes code related to user interfaces and interactions. "
            "Backend includes data systems, server-side logic, and processing. "
            "A full stack developer must be comfortable connecting both sides of an application."
        ),
        "courses": [
            ("AP CSP", "Introduces foundational concepts of computer science: data, algorithms, the internet, and cybersecurity."),
            ("AP CSA", "Focuses on object-oriented programming in Java. Builds problem decomposition, data structures, and algorithm design."),
            ("Discrete Mathematics", "Teaches logic, sets, graph theory, and combinatorics — essential for understanding how software and databases are structured."),
        ],
        "extracurriculars": [
            ("Robotics/VEX", "Teaches real-world programming and engineering problem-solving with software-hardware integration."),
            ("Software Engineering Club", "Work on real projects, collaborate with peers, and build a portfolio."),
            ("Internship", "Hands-on experience at real companies applying your skills professionally."),
        ],
        "postsecondary": [
            ("Bachelor's Degree", "Computer Science, Software Engineering, or related field."),
            ("Online Certifications", "HTML, CSS, JavaScript, and frameworks like React or Node.js via Coursera, freeCodeCamp, or Udemy."),
            ("Apprenticeships/Internships", "Structured path into the industry without a traditional degree."),
        ],
        "certifications": "HTML, CSS, JavaScript\nFrontend: HTML, CSS | Backend: JavaScript",
        "jobs": ["Junior Developer", "Internship"],
        "qualifications": ["Portfolio of projects", "Proficiency in HTML, CSS, JavaScript", "Familiarity with frontend/backend frameworks"],
    },
    "AI": {
        "title": "AI Specialist",
        "description": (
            "An AI Specialist designs and develops machine-learning models and algorithms to create intelligent systems. "
            "They optimize software and automate tasks using machine learning, natural language processing, and neural networks."
        ),
        "courses": [
            ("AP Statistics", "Introduces data analysis, probability, and statistical inference — foundational for machine learning."),
            ("AP CSP", "Introduces big-picture computing concepts including data, algorithms, and the internet."),
            ("AP CSA", "Builds programming logic and structure needed to work with AI frameworks and complex algorithms."),
        ],
        "extracurriculars": [
            ("Internship", "Hands-on exposure to real AI projects at tech companies or research labs."),
        ],
        "postsecondary": [
            ("Bachelor's/Master's Degree", "Computer Science, Data Science, or Artificial Intelligence."),
            ("Online Certifications", "Machine learning, neural networks, and AI frameworks via Coursera, edX, or DeepLearning.AI."),
            ("Apprenticeships/Internships", "Real-world experience in AI research or tech companies."),
        ],
        "certifications": "C++, OOP\nC++ is widely used in AI and systems programming. OOP provides a framework for machine learning.",
        "jobs": ["Data Analyst", "Prompt Engineer", "Research Assistant"],
        "qualifications": ["Proficiency in Python, C++", "Understanding of ML frameworks (TensorFlow, PyTorch)", "Knowledge of statistics and linear algebra"],
    },
    "Educator": {
        "title": "General Educator",
        "description": (
            "A general educator is a teacher who delivers instruction and designs academic curriculum for students. "
            "Many educators specialize in a subject area and are required to create an effective classroom environment."
        ),
        "courses": [
            ("AP Psychology", "Introduces human behavior and mental processes — directly applicable to teaching strategies."),
            ("Child Development", "Covers cognitive, social, and emotional growth of children."),
            ("Communications", "Builds verbal, written, and interpersonal skills essential for educators."),
            ("AP Seminar", "Develops critical thinking, research, and collaborative discussion skills."),
        ],
        "extracurriculars": [
            ("NHS", "Demonstrates academic excellence and commitment to service and leadership."),
            ("Student Government/Council", "Builds leadership, communication, and organizational skills."),
            ("Volunteering", "Provides early hands-on experience working with others in community settings."),
        ],
        "postsecondary": [
            ("Bachelor's Degree in Education", "Includes pedagogy, curriculum design, and student teaching."),
            ("Online Certifications", "Teaching methods, special education, or EdTech tools."),
            ("Graduate Programs", "Master's in Education for higher-level teaching or administration roles."),
        ],
        "certifications": "State teaching license/certification",
        "jobs": ["Teacher Assistant", "Substitute Teacher", "Tutor"],
        "qualifications": ["Bachelor's degree in Education or subject area", "State teaching license/certification", "Student teaching experience"],
    },
    "Physician": {
        "title": "Physician",
        "description": (
            "A physician is a highly-trained, licensed healthcare professional with a medical degree. "
            "They examine patients, order diagnostic tests, prescribe medication, and manage medical histories."
        ),
        "courses": [
            ("AP Chemistry", "Builds foundational chemistry knowledge important in medical school."),
            ("AP Biology", "Provides key biological concepts, labs, and critical thinking essential to medicine."),
        ],
        "extracurriculars": [
            ("Lab Report", "Shows ability to complete professional scientific research and analyze data."),
            ("Shadowing", "Gain firsthand experience understanding a career in medicine."),
            ("HOSA", "Student-led organization providing networking, hands-on experience, and competitive events."),
            ("Volunteering", "Shows initiative and provides a wide range of activities and experience."),
        ],
        "postsecondary": [
            ("Bachelor's Degree", "Usually pre-med."),
            ("Medical School", "Requires MCAT scores, transcripts, and letters of recommendation."),
            ("Residency", "Specialized training lasting 3–7 years depending on specialty."),
            ("Fellowship", "Optional advanced training after residency for in-depth specialty knowledge."),
        ],
        "certifications": "MD/DO Degree, Licensing exams",
        "jobs": ["Resident Doctor", "Fellowship", "Practitioner"],
        "qualifications": ["MD/DO Degree", "Licensing exams", "Matching programs"],
    },
    "Biologist": {
        "title": "Biologist",
        "description": (
            "A biologist studies the living organisms of the Earth and their interactions with other organisms. "
            "Biologists conduct laboratory experiments to further develop our understanding of the biological world."
        ),
        "courses": [
            ("AP Chemistry", "Provides chemical knowledge applicable to complex biological processes."),
            ("AP Biology", "Foundational biology concepts, laboratory skills, data analysis, and scientific reasoning."),
            ("AP Seminar/Research", "Develops critical thinking, research, and communication skills needed in a lab."),
        ],
        "extracurriculars": [
            ("Lab Report", "Shows ability to complete professional scientific research and analyze data."),
            ("Shadowing", "Gain firsthand experience in a biology-related career."),
            ("HOSA", "Networking, hands-on experience, and competitive events for future health professionals."),
            ("Volunteering", "Shows initiative and provides a wide range of experiences."),
            ("Science-Related Clubs", "Demonstrates leadership and collaboration in your preferred field."),
        ],
        "postsecondary": [
            ("Bachelor's Degree", "Biology or other specialized fields."),
            ("Internships/Lab Research", "Develop actual skills and experience for a future career."),
            ("Graduate School", "Recommended for advanced research and specialized roles."),
        ],
        "certifications": "Bachelor's degree in Biology or related field",
        "jobs": ["Research Assistant", "Research Technician", "Field Observer"],
        "qualifications": ["Bachelor's degree in Biology or related field", "Organizational and communication skills", "Experience in lab techniques and protocols"],
    },
    "Engineer": {
        "title": "Mechanical Engineer",
        "description": (
            "Mechanical engineering is the application of designing, developing, building, and testing objects "
            "using engineering principles. Mechanical engineers analyze their work to ensure designs function "
            "effectively and safely, aiming to better human life."
        ),
        "courses": [
            ("AP Physics 1", "Algebra-based college-level physics covering Newtonian mechanics, energy, and waves."),
            ("AP Physics 2", "Covers thermodynamics, electricity, magnetism, fluids, and optics."),
            ("AP Physics C", "Calculus-based mechanics and electricity & magnetism."),
            ("AP Calculus AB/BC", "College-level mathematics covering limits, derivatives, integrals, and series."),
        ],
        "extracurriculars": [
            ("Robotics", "Real-world programming and engineering problem-solving."),
            ("Programming/3D Design", "Core parts of engineering curricula that also show initiative."),
        ],
        "postsecondary": [
            ("Bachelor's Degree", "Engineering or related fields."),
            ("Engineering Technology Programs", "Applied engineering principles and technical skills."),
            ("Graduate School", "Recommended for specialized fields and advanced careers."),
            ("Internships", "Provide experience and certification often required in the field."),
        ],
        "certifications": "Engineering licensure (PE exam)",
        "jobs": ["Assistant Engineer", "Mechanical Design Engineer", "Test Engineer"],
        "qualifications": ["Bachelor's degree in Engineering", "Technical proficiency (CAD, programming)", "Hands-on experience"],
    },
    "Physicist": {
        "title": "Physicist",
        "description": (
            "A physicist studies or specializes in the matter and energy governing the universe. "
            "Physicists use mathematics, experiments, and technology to understand the universe."
        ),
        "courses": [
            ("AP Physics 1 & 2", "Introduces classical mechanics, waves, electricity, and magnetism."),
            ("AP Physics C", "Calculus-based mechanics and electromagnetism at a college level."),
            ("AP Calculus", "Equips you with mathematical tools to model and solve physical problems."),
        ],
        "extracurriculars": [
            ("Research under professors", "Exposes you to real scientific inquiry and builds academic credentials."),
            ("Internships", "Hands-on experience and professional connections at research institutions."),
            ("Mathematics Club", "Sharpens quantitative thinking and problem-solving skills."),
        ],
        "postsecondary": [
            ("Bachelor's Degree in Physics", "Covers classical mechanics, quantum mechanics, electromagnetism, and thermodynamics."),
            ("Graduate School", "Master's or PhD to conduct research and specialize in a subfield."),
            ("Research Internships", "Applicable experience that strengthens academic and job applications."),
        ],
        "certifications": "Bachelor's or graduate degree in Physics",
        "jobs": ["Research Assistant", "Entry Level Software Developer"],
        "qualifications": ["Bachelor's or graduate degree in Physics", "Strong math and analytical skills", "Research or lab experience"],
    },
}

# =============================================
# GUI SETUP
# =============================================
sg.theme("LightBlue2")

# Consistent fonts for the UI
HEADER_FONT = ("Helvetica", 16, "bold")
BODY_FONT = ("Helvetica", 11)
LABEL_FONT = ("Helvetica", 12)

def run_quiz():
    current_q = 0
    answers = []

    # Loop through each question in the dataset
    while current_q < len(questions):
        q = questions[current_q]
        question_text = q[0]
        options = q[1]

        # Build the layout dynamically based on the number of options
        progress = int((current_q / len(questions)) * 100)
        layout = [
            [sg.Text(f"Question {current_q + 1} of {len(questions)}", font=("Helvetica", 10), text_color="gray"),
             sg.Push(), sg.ProgressBar(100, orientation="h", size=(18, 14), key="-PROG-", bar_color=("#4A90D9", "#D0D0D0"))],
            [sg.Text(question_text, font=HEADER_FONT, size=(50, 2))],
            [sg.HorizontalSeparator()]
        ]

        # Humanized: Standard loop to add radio buttons to the layout
        for j, opt in enumerate(options):
            layout.append([sg.Radio(opt, "ANSWER", key=f"opt_{j}", font=LABEL_FONT, pad=(10, 8))])

        # Add the next button at the bottom
        layout.append([sg.HorizontalSeparator()])
        layout.append([sg.Push(), sg.Button("Next →", size=(10, 1), font=BODY_FONT), sg.Push()])

        # Create and display the window for the current question
        window = sg.Window("Career Pathfinder", layout, size=(580, 370), finalize=True, element_justification="left", margins=(30, 20))
        window["-PROG-"].update(progress)

        # Event loop to handle button clicks
        while True:
            event, values = window.read()
            
            # If user closes window with the X button
            if event == sg.WIN_CLOSED:
                window.close()
                return None
                
            if event == "Next →":
                # Humanized: Standard for-loop to find the selected answer
                selected = None
                for j in range(len(options)):
                    if values.get(f"opt_{j}") == True:
                        selected = j
                        break
                        
                # Ensure the user actually clicked an option
                if selected is None:
                    sg.popup("Please select an answer before continuing.", title="No selection", font=BODY_FONT)
                else:
                    answers.append(selected)
                    window.close()
                    break

        # Tally the scores for the careers associated with the user's choice
        careers_maps = questions[current_q][2]
        for career in careers_maps[answers[-1]]:
            scores[career] += 1

        current_q += 1

    # Return the career with the highest score
    return max(scores, key=scores.get)


def show_pathway(result):
    p = pathways[result]

    # Helper function to format sections neatly
    def section(title, items, numbered=False):
        lines = [f"── {title} ──\n"]
        for i, item in enumerate(items):
            # Check if the item is a tuple (course/extracurricular) or a flat string
            if isinstance(item, tuple):
                prefix = f"{i+1}. " if numbered else "• "
                lines.append(f"{prefix}{item[0]}")
                lines.append(f"   {item[1]}\n")
            else:
                prefix = f"{i+1}. " if numbered else "• "
                lines.append(f"{prefix}{item}")
        return "\n".join(lines)


    job_str = '\n'.join([f"  {i+1}. {job}" for i, job in enumerate(p['jobs'])])
    qual_str = '\n'.join([f"  • {q}" for q in p['qualifications']])

    content = f"""{'='*55}
{p['title'].upper()}
{'='*55}

{p['description']}

{section('Recommended High School Courses', p['courses'], numbered=True)}
{section('Recommended Extracurriculars', p['extracurriculars'], numbered=True)}
{section('Post-Secondary Options', p['postsecondary'], numbered=True)}

── Key Certifications ──
{p['certifications']}

── Entry Level Jobs ──
{job_str}

── Common Qualifications ──
{qual_str}
"""

    # Layout for the final results screen
    layout = [
        [sg.Text("Your Career Match:", font=("Helvetica", 12), text_color="gray")],
        [sg.Text(p["title"], font=("Helvetica", 22, "bold"), text_color="#2B6CB0")],
        [sg.HorizontalSeparator()],
        # Multiline box acts as a text viewer for the formatted string
        [sg.Multiline(content, size=(68, 26), font=("Courier", 10), disabled=True, key="-OUT-", no_scrollbar=False)],
        [sg.Push(), sg.Button("Close", size=(10, 1), font=BODY_FONT), sg.Push()],
    ]

    window = sg.Window("Career Pathfinder — Results", layout, size=(660, 560), finalize=True, margins=(25, 20))

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Close"):
            break

    window.close()


def main():
    # Layout for the initial welcome screen
    layout = [
        [sg.Text("Career Pathfinder", font=("Helvetica", 28, "bold"), text_color="#2B6CB0")],
        [sg.Text("Discover the STEM career path best suited for you.", font=BODY_FONT, text_color="gray")],
        [sg.Text("Answer 7 short questions to get your personalized result.", font=BODY_FONT, text_color="gray")],
        [sg.HorizontalSeparator()],
        [sg.Button("Start Quiz", size=(14, 1), font=("Helvetica", 12, "bold")), sg.Button("Quit", size=(8, 1), font=BODY_FONT)],
    ]

    window = sg.Window("Career Pathfinder", layout, size=(520, 220), finalize=True, element_justification="center", margins=(40, 30))

    # Event loop for the welcome screen
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            window.close()
            return
        if event == "Start Quiz":
            window.close()
            break

    # Run the main program loop
    result = run_quiz()
    if result:
        show_pathway(result)


if __name__ == "__main__":
    main()


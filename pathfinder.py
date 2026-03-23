import sys

# =============================================
# PATHWAY FUNCTIONS
# =============================================

def ask_continue():
    while True:
        cont = input("Would you like to continue [y/n]?: ")
        if cont.lower() == "y":
            return
        elif cont.lower() == "n":
            sys.exit()
        else:
            print("Please type y or n.")


def fullstack_pathway():
    print("=============================================")
    print("\n")
    print("The career path suited for you is a Full Stack Developer!")
    print("\n")
    print("A full stack web-developer is someone who develops both\nfrontend and backend software. Frontend software includes\ncode related to user interfaces and interactions in the\napplication. On the other hand, backend software includes\ncode required for data systems, server-side logic, and\nprocessing data. A full stack developer must be comfortable\nwith formulating the connectivity between the front-end\nand back-end logic of a software application.")
    print("\n")
    print("=============================================")

    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\npreparations you can make to become a Full Stack Developer,\nincluding courses and extracurriculars.")
    print("\n")
    print("Recommended High School Courses:")
    print("1. AP CSP")
    print("AP Computer Science Principles is a college level course\nthat introduces students to the foundational concepts of\ncomputer science. It covers topics like data, algorithms,\nthe internet, and cybersecurity, providing a broad base\nfor any career in tech.")
    print("\n")
    print("2. AP CSA")
    print("AP Computer Science A focuses on object-oriented\nprogramming using Java. It builds strong programming\nfundamentals — problem decomposition, data structures,\nand algorithm design — all critical for full stack work.")
    print("\n")
    print("3. Discrete Mathematics")
    print("Discrete Mathematics teaches logic, sets, graph theory,\nand combinatorics. These concepts underpin computer\nscience and are essential for understanding how software\nand databases are structured.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future employers.")
    print("\n")
    print("Recommended Extracurriculars:")
    print("1. Robotics/VEX")
    print("Robotics competitions like VEX teach students real-world\nprogramming and engineering problem-solving. They expose\nyou to software-hardware integration and collaborative\nteam-based development.")
    print("\n")
    print("2. Software Engineering Club")
    print("Software Engineering Clubs provide a space to work on\nreal projects, collaborate with peers, and build a\nportfolio of work that demonstrates your programming\nskills to future employers.")
    print("\n")
    print("3. Internship")
    print("Internships offer hands-on experience at real companies.\nThey allow you to apply your skills in a professional\nenvironment and build connections in the industry.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("After high school, there are post-secondary opportunities you\ncan take. Here are some options!")
    print("\n")
    print("1. Bachelor's Degree")
    print("A degree in Computer Science, Software Engineering, or a\nrelated field provides prerequisite coursework and a\nstrong theoretical foundation for full stack development.")
    print("\n")
    print("2. Online Certifications")
    print("Platforms like Coursera, freeCodeCamp, or Udemy offer\nvirtual learning and coursework at your own comfort.\nCertifications in HTML, CSS, JavaScript, and frameworks\nlike React or Node.js are highly valued.")
    print("\n")
    print("3. Apprenticeships/Internships")
    print("On-hand, applicable practice under supervision by\nprofessionals. Apprenticeships provide a structured\npath into the industry without a traditional degree.")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")
    print("Key Certifications:")
    print("HTML, CSS, JavaScript")
    print("The most common programming languages used for web\ndevelopment and design.")
    print("Frontend: HTML, CSS")
    print("Backend: JavaScript")
    print("\n")
    print("Entry Level Jobs:")
    print("1. Junior Developer")
    print("2. Internship")
    print("\n")
    print("Common Qualifications:")
    print("Portfolio of projects")
    print("Proficiency in HTML, CSS, JavaScript")
    print("Familiarity with frontend/backend frameworks")
    print("\n")


def ai_pathway():
    print("=============================================")
    print("\n")
    print("The career path suited for you is an AI Specialist!")
    print("\n")
    print("An AI Specialist designs and develops machine-learning\nmodels and algorithms to create intelligent systems.\nThey optimize software and create systems that can\nautomate tasks. Through their understanding of machine\nlearning algorithms, natural language processing, neural\nnetworks, and other concepts, they push the boundaries\nof what technology can accomplish.")
    print("\n")
    print("=============================================")

    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\npreparations you can make to become an AI Specialist,\nincluding courses and extracurriculars.")
    print("\n")
    print("Recommended High School Courses:")
    print("1. AP Statistics")
    print("AP Statistics introduces data analysis, probability, and\nstatistical inference. These concepts are foundational\nto machine learning, where understanding data\ndistributions and model performance is critical.")
    print("\n")
    print("2. AP CSP")
    print("AP Computer Science Principles introduces the big-picture\nconcepts of computing including data, algorithms, and\nthe internet — all essential groundwork before diving\ninto AI development.")
    print("\n")
    print("3. AP CSA")
    print("AP Computer Science A focuses on object-oriented\nprogramming in Java. It builds the programming logic\nand structure needed to eventually work with AI\nframeworks and complex algorithms.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future employers.")
    print("\n")
    print("Recommended Extracurriculars:")
    print("1. Internship")
    print("Internships at tech companies or research labs offer\nhands-on exposure to real AI projects. They allow\nyou to apply your skills professionally and build\nindustry connections early on.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("After high school, there are post-secondary opportunities you\ncan take. Here are some options!")
    print("\n")
    print("1. Bachelor's/Master's Degree")
    print("A degree in Computer Science, Data Science, or\nArtificial Intelligence provides the prerequisite\ncoursework and research exposure needed to work in\nthe AI field professionally.")
    print("\n")
    print("2. Online Certifications")
    print("Platforms like Coursera, edX, or DeepLearning.AI offer\nvirtual learning in machine learning, neural networks,\nand AI frameworks at your own comfort and pace.")
    print("\n")
    print("3. Apprenticeships/Internships")
    print("On-hand, applicable practice under supervision by\nprofessionals in AI research or tech companies.\nThese provide real-world experience that complements\nformal education.")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")
    print("Key Certifications:")
    print("C++, OOP")
    print("C++ is one of the most efficient programming languages\nand is widely used in AI and systems programming.")
    print("OOP (Object-Oriented Programming) is a programming\nparadigm based on objects that improves reusability\nand organization. OOP provides an easier framework\nand structure for machine learning in artificial intelligence.")
    print("\n")
    print("Entry Level Jobs:")
    print("1. Data Analyst")
    print("2. Prompt Engineer")
    print("3. Research Assistant")
    print("\n")
    print("Common Qualifications:")
    print("Proficiency in Python, C++")
    print("Understanding of ML frameworks (TensorFlow, PyTorch)")
    print("Knowledge of statistics and linear algebra")
    print("\n")


def educator_pathway():
    print("=============================================")
    print("\n")
    print("The career path suited for you is a General Educator!")
    print("\n")
    print("A general educator is a teacher who delivers instruction\nand designs academic curriculum for students. Many\neducators specialize in a subject area and are required\nto create an effective classroom environment.")
    print("\n")
    print("=============================================")

    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\npreparations you can make to become a General Educator,\nincluding courses and extracurriculars.")
    print("\n")
    print("Recommended High School Courses:")
    print("1. AP Psychology")
    print("AP Psychology introduces the study of human behavior\nand mental processes. Understanding how people think\nand learn is directly applicable to developing effective\nteaching strategies and classroom management.")
    print("\n")
    print("2. Child Development")
    print("Child Development covers the cognitive, social, and\nemotional growth of children. This knowledge is\nessential for educators to understand their students\nand tailor instruction to different developmental stages.")
    print("\n")
    print("3. Communications")
    print("A Communications course builds verbal, written, and\ninterpersonal skills. Educators must be able to clearly\nconvey information and connect with students, parents,\nand colleagues effectively.")
    print("\n")
    print("4. AP Seminar")
    print("AP Seminar teaches research, analysis, and\ncollaborative discussion skills. It develops critical\nthinking and the ability to design curriculum and\npresent ideas — core competencies for any educator.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future employers.")
    print("\n")
    print("Recommended Extracurriculars:")
    print("1. NHS (National Honor Society)")
    print("NHS demonstrates academic excellence and a commitment\nto service and leadership — qualities central to\nbeing an effective educator.")
    print("\n")
    print("2. Student Government/Council")
    print("Student Government builds leadership, communication,\nand organizational skills. It prepares you for managing\na classroom and working with diverse groups of people.")
    print("\n")
    print("3. Volunteering")
    print("Volunteering, especially in educational or community\nsettings, provides early hands-on experience working\nwith others and gives you insight into what a career\nin education looks like.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("After high school, there are post-secondary opportunities you\ncan take. Here are some options!")
    print("\n")
    print("1. Bachelor's Degree in Education")
    print("A degree in Education or a subject specialty (e.g.,\nMath Education, English Education) is the standard\npath. Includes prerequisite coursework in pedagogy,\ncurriculum design, and student teaching.")
    print("\n")
    print("2. Online Certifications")
    print("Online certifications in teaching methods, special\neducation, or EdTech tools allow for virtual learning\nand professional development at your own comfort.")
    print("\n")
    print("3. Graduate Programs")
    print("A Master's in Education or a specialized field can\nopen doors to higher-level teaching positions,\nadministration, or curriculum development roles.")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")
    print("Entry Level Jobs:")
    print("1. Teacher Assistant")
    print("2. Substitute Teacher")
    print("3. Tutor")
    print("\n")
    print("Common Qualifications:")
    print("Bachelor's degree in Education or subject area")
    print("State teaching license/certification")
    print("Student teaching experience")
    print("\n")


def physician_pathway():
    print("=============================================")
    print("\n")
    print("The career path suited for you is a Physician!")
    print("\n")
    print("A physician is a highly-trained, licensed healthcare\nprofessional that has earned a medical degree. They\nexamine patients, order diagnostic tests, prescribe\nmedication, and manage medical histories.")
    print("\n")
    print("=============================================")

    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\npreparations you can make to become a physician,\nincluding courses and extracurriculars.")
    print("\n")
    print("Recommended High School Courses:")
    print("1. AP Chemistry")
    print("AP Chemistry is a college level chemistry course designed\nfor high school students. It builds a foundational\nunderstanding and introduction of certain processes that are extremely\nimportant in medical school.")
    print("\n")
    print("2. AP Biology")
    print("AP Biology is a college level biology course for high school\nstudents, and provides a foundational understanding\nof key biological concepts. The curriculum teaches fundamental concepts\nessential to medicine, supports labs and critical thinking, and more.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future jobs.")
    print("\n")
    print("Recommended Extracurriculars:")
    print("1. Lab Report")
    print("Lab reports show that you can complete professional scientific\nresearch and analyze data efficiently.")
    print("\n")
    print("2. Shadowing")
    print("By shadowing a professional, students are able to gain experience\nwhile being able to understand it firsthand. It can\neventually help you decide on your career choices after your education.")
    print("\n")
    print("3. HOSA")
    print("HOSA (Future Health Professionals) is a student-led organization recognized by the US Department of Education and the\nDepartment of Health and Human Services. It can provide networking,\nhands-on experience, and competitive events for a student.")
    print("\n")
    print("4. Volunteering")
    print("Volunteering is similar to shadowing, but it shows initiative and a more wide-ranged of activities and experience you\ncan receive.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("After high school, there are post-secondary opportunities you\ncan take. Here are some options!")
    print("\n")
    print("1. Bachelor's Degree")
    print("Usually pre-med.")
    print("\n")
    print("2. Medical School")
    print("Medical schools require MCAT scores, transcripts, and letters of\nrecommendation.")
    print("\n")
    print("3. Residency")
    print("Residency is a specialized training program for doctors after\ntheir degree, usually lasting from 3 to 7 years depending on specialty.")
    print("\n")
    print("4. Fellowship")
    print("Fellowship is an optional, advanced training program after\ncompleting residency to gain in-depth knowledge in a specific specialty.")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")
    print("Entry Level Jobs:")
    print("1. Resident Doctor")
    print("2. Fellowship")
    print("3. Practitioner")
    print("\n")
    print("Common Qualifications:")
    print("MD/DO Degree")
    print("Licensing exams")
    print("Matching programs")
    print("\n")


def biologist_pathway():
    # Intro
    print("=============================================")
    print("\n")
    print("The career path suited for you is a biologist!")
    print("\n")
    print("A scientist of Biology studies the living organisms\nof the Earth, along with their interactions with other\norganisms. Biologists conduct laboratory experiments\nto further develop the biological world around them.")
    print("\n")
    print("=============================================")

    # High School Courses
    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\nprepartions you can make to become a biologist,\nincluding courses and extracurriculars.")
    print("\n")

    print("Recommended High School Courses:")
    print("1. AP Chemistry")
    print("AP Chemistry is a college level chemistry course designed\nfor high school students. This course is highly beneficial\nfor biologists as it provides a framework of prior chemical\nknowledge that are likely to be in complex biological processes.")
    print("\n")

    print("2. AP Biology")
    print("AP Biology is a college level biology course for high school\nstudents, and provides a foundational understanding of key\nbiological concepts. It helps develops essential labratory\nskills, data analysis, scientific reasoning/research, and more.")
    print("\n")

    print("3. AP Seminar/Research")
    print("AP Seminar is a project-based college level course that helps\nstudents with critical thinking, research, and communication\nskills. All of these are needed to work in a lab.")
    print("\n")
    print("AP Research is a course where students thoroughly explore an\nacademic choice by designing, planning, and conducting a study.\nThis is once needed to have the right collaboration skills in a\nlab.")
    print("\n")

    # Extracurriculars, etc
    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")

    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future jobs.")
    print("\n")

    print("Recommended Extracurriculars:")
    print("1. Lab Report")
    print("Lab reports show that you can complete professional scientific\nresearch and analyze data effeciently.")
    print("\n")

    print("2. Shadowing")
    print("By shadowing a professional, students are able to gain experience\nwhile being able to understand it firsthand. It can\neventually help you decide on your career choices after your education.")
    print("\n")

    print("3. HOSA")
    print("HOSA (Future Health Professionals) is a student-led organization recognized by the US Department of Education and the\nDepartment of Health and Human Services. It can provide networking,\nhands-on experience, and competitive events for a student.")
    print("\n")

    print("4. Volunteering")
    print("Volunteering is similar to shadowing, but it shows initiative and a more wide-ranged of activities and experience you\ncan receive.")
    print("\n")

    print("5. Science-Related Clubs")
    print("If you are unable to participate in any of these activites above, try to see if your high school has any science\nrelated clubs. Clubs are a great extracurricular, and doing something related\nto your preferred field is best, but any clubs show\nleadership and collaboration.")
    print("\n")

    # Post-Secondary options
    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")

    print("After high school, there are post-secondary opportunities you can\ntake. Here are some options!")
    print("\n")

    print("1. Bachelor's Degree")
    print("This can be in biology major or other specialized fields")
    print("\n")

    print("2. Internships/Lab Research")
    print("This will help develop actual experience and skills that will help\nyou in a future career.")
    print("\n")

    print("3. Graduate School")
    print("Graduate school is optional, but recommended for advanced research,\nand special roles")
    print("\n")

    # Professional Skills/Entry Level Jobs
    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")

    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")

    print("Entry Level Jobs")

    print("1. Research Assistant")
    print("2. Research Technician")
    print("3. Field Observer")
    print("\n")

    print("Common Qualifications:")
    print("Bachelor's degree in Biology or related field")
    print("Organizational and communication skills")
    print("Experience in certain techniques and protocols")
    print("Extra training required once accepted")
    print("\n")


def engineer_pathway():
    # Intro
    print("=============================================")
    print("\n")
    print("The career path suited for you is a biologist!")
    print("\n")
    print("Mechanical engineering is the application of\ndesigning, developing, building, and testing any\nobject using the principles of engineering. Mechanical engineers\nanalyze their work and ensure their designs function effectively\nand safely. They aim to better human life and create solutions.")
    print("\n")
    print("=============================================")

    # High School Courses
    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\nprepartions you can make to become a biologist,\nincluding courses and extracurriculars.")
    print("\n")

    print("Recommended High School Courses:")
    print("1. AP Physics 1")
    print("AP Physics 1 is an algebra-based college-level physics course.\nIt provides knowledge in Newtonian mechanics, energy, and waves.")
    print("\n")

    print("2. AP Physics 2")
    print("AP Physics 2 is an algebra-based college-level physics course.\nIt provides knowledge in thermodynamics, electricity,\nmagnetism, fluids, optics, and more.")
    print("\n")

    print("3. AP Physics C")
    print("AP Physics C is a calculus-based, college-level courses: mechanics\nand electricitiy & magnetism.")

    print("4. AP Calculus AB/BC")
    print("AP Calculus consists of college-level mathematics covering limits,\nderivatives, integrals, and series.")

    # Extracurriculars, etc
    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")

    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future jobs.")
    print("\n")

    print("Recommended Extracurriculars:")
    print("1. Robotics")
    print("Lab reports show that you can complete professional scientific\nresearch and analyze data effeciently.")
    print("\n")

    print("2. Programming/3D Design")
    print("Programming and 3D Design are both a part of engineering curriculums\nin college. It also shows initiative.")

    # Post-Secondary options
    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")

    print("After high school, there are post-secondary opportunities you can\ntake. Here are some options!")
    print("\n")

    print("1. Bachelor's Degree")
    print("This can be in an engineering major or other fields")
    print("\n")

    print("2. Engineering Technology programs")
    print("A program focused on applied engineering principles and technical\nskills.")
    print("\n")

    print("3. Graduate School")
    print("Graduate school is optional, but recommended for specialized fields,\nand advance careers.")
    print("\n")

    print("4. Internships")
    print("Often required as internships provide experience and certification")

    # Professional Skills/Entry Level Jobs
    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")

    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")

    print("Entry Level Jobs")

    print("1. Assistant Engineer")
    print("2. Mechanical Design Engineer")
    print("3. Test Engineer")
    print("\n")

    print("Common Qualifications:")
    print("Bachelor's degree in Engineering or related field")
    print("Technical proficiency (CAD, programming, certain applications, more)")
    print("Hands-on experience")
    print("\n")


def physicist_pathway():
    print("=============================================")
    print("\n")
    print("The career path suited for you is a Physicist!")
    print("\n")
    print("A physicist is an expert who studies or specializes in\ngoverning the matter and energy in the universe.\nPhysicists try to understand the universe by using\nmathematics, experiments, and other technologies.")
    print("\n")
    print("=============================================")

    print('\n')
    ask_continue()
    print("\n")
    print("A Pathway Designed for You")
    print("You start out in high school, and there are\npreparations you can make to become a Physicist,\nincluding courses and extracurriculars.")
    print("\n")
    print("Recommended High School Courses:")
    print("1. AP Physics 1 & 2")
    print("AP Physics introduces classical mechanics, waves,\nelectricity, and magnetism — the foundation of all\nphysics study.")
    print("\n")
    print("2. AP Physics C")
    print("AP Physics C is calculus-based and covers mechanics\nand electromagnetism at a college level, preparing\nyou for university physics programs.")
    print("\n")
    print("3. AP Calculus")
    print("Physics is deeply mathematical. AP Calculus equips\nyou with the tools to model and solve physical\nproblems analytically.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("Along with high school courses, you can do extracurriculars to\nimpress colleges and future employers.")
    print("\n")
    print("Recommended Extracurriculars:")
    print("1. Research under professors")
    print("Assisting professors with research exposes you to\nreal scientific inquiry and helps build academic\ncredentials early.")
    print("\n")
    print("2. Internships")
    print("Internships at research institutions or labs give\nyou hands-on experience and professional connections.")
    print("\n")
    print("3. Mathematics Club")
    print("Math clubs sharpen your quantitative thinking and\nproblem-solving skills, both essential for a physicist.")
    print("\n")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("After high school, there are post-secondary opportunities you\ncan take. Here are some options!")
    print("\n")
    print("1. Bachelor's Degree in Physics")
    print("A physics degree covers classical mechanics, quantum\nmechanics, electromagnetism, thermodynamics, and\nexperimental methods.")
    print("\n")
    print("2. Graduate School")
    print("Most physicists pursue a Master's or PhD to conduct\noriginal research and specialize in a subfield such\nas astrophysics, particle physics, or condensed matter.")
    print("\n")
    print("3. Research Internships")
    print("Working in a research lab during or after your degree\nprovides applicable experience and strengthens your\nacademic and job applications.")

    ask_continue()
    print("\n")
    print("=============================================")
    print("\n")
    print("With all these experiences/education, you should have a decent\nskillset that equips your resume when looking for jobs.")
    print("\n")
    print("Entry Level Jobs:")
    print("1. Research Assistant")
    print("2. Entry Level Software Developer")
    print("\n")
    print("Common Qualifications:")
    print("Bachelor's or graduate degree in Physics")
    print("Strong math and analytical skills")
    print("Research or lab experience")
    print("\n")



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



if finalChoice == "Full Stack":
    fullstack_pathway()
elif finalChoice == "AI":
    ai_pathway()
elif finalChoice == "Educator":
    educator_pathway()
elif finalChoice == "Physician":
    physician_pathway()
elif finalChoice == "Biologist":
    biologist_pathway()
elif finalChoice == "Engineer":
    engineer_pathway()
elif finalChoice == "Physicist":
    physicist_pathway()

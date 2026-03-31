import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser

# =============================================
# QUIZ DATA
# =============================================

# Base scores - copied fresh on each quiz run
scores_template = {
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
# Post-secondary entries are 3-tuples: (name, description, url)
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
            ("Bachelor's Degree", "Computer Science, Software Engineering, or related field.", "https://www.coursera.org/browse/computer-science"),
            ("Online Certifications", "HTML, CSS, JavaScript, and frameworks like React or Node.js via Coursera, freeCodeCamp, or Udemy.", "https://www.freecodecamp.org"),
            ("Apprenticeships/Internships", "Structured path into the industry without a traditional degree.", "https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm"),
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
            ("Bachelor's/Master's Degree", "Computer Science, Data Science, or Artificial Intelligence.", "https://www.coursera.org/degrees"),
            ("Online Certifications", "Machine learning, neural networks, and AI frameworks via Coursera, edX, or DeepLearning.AI.", "https://www.deeplearning.ai"),
            ("Apprenticeships/Internships", "Real-world experience in AI research or tech companies.", "https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm"),
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
            ("Bachelor's Degree in Education", "Includes pedagogy, curriculum design, and student teaching.", "https://www.ed.gov/higher-education"),
            ("Online Certifications", "Teaching methods, special education, or EdTech tools.", "https://www.coursera.org/browse/education"),
            ("Graduate Programs", "Master's in Education for higher-level teaching or administration roles.", "https://www.bls.gov/ooh/education-training-and-library/kindergarten-and-elementary-school-teachers.htm"),
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
            ("Bachelor's Degree (Pre-Med)", "Usually pre-med; strong foundation in biology and chemistry.", "https://www.aamc.org/students/aspiring-doctors"),
            ("Medical School", "Requires MCAT scores, transcripts, and letters of recommendation.", "https://students-residents.aamc.org/applying-medical-school"),
            ("Residency", "Specialized clinical training lasting 3-7 years depending on specialty.", "https://www.bls.gov/ooh/healthcare/physicians-and-surgeons.htm"),
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
            ("Bachelor's Degree", "Biology or other specialized fields.", "https://www.asm.org/Careers/Explore-Careers-in-Microbiology"),
            ("Internships/Lab Research", "Develop actual skills and experience for a future career.", "https://www.nsf.gov/crssprgm/reu"),
            ("Graduate School", "Recommended for advanced research and specialized roles.", "https://www.bls.gov/ooh/life-physical-and-social-science/zoologists-and-wildlife-biologists.htm"),
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
            ("Bachelor's Degree", "Engineering or related fields from an ABET-accredited program.", "https://www.abet.org/accreditation/find-programs"),
            ("Engineering Technology Programs", "Applied engineering principles and technical skills.", "https://www.asme.org/career-education/students"),
            ("Graduate School & Internships", "Recommended for specialized fields; internships often required for licensure.", "https://www.bls.gov/ooh/architecture-and-engineering/mechanical-engineers.htm"),
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
            ("Bachelor's Degree in Physics", "Covers classical mechanics, quantum mechanics, electromagnetism, and thermodynamics.", "https://www.aps.org/careers"),
            ("Graduate School", "Master's or PhD to conduct research and specialize in a subfield.", "https://www.nsf.gov/crssprgm/reu"),
            ("Research Internships", "Applicable experience that strengthens academic and job applications.", "https://www.bls.gov/ooh/life-physical-and-social-science/physicists-and-astronomers.htm"),
        ],
        "certifications": "Bachelor's or graduate degree in Physics",
        "jobs": ["Research Assistant", "Entry Level Software Developer"],
        "qualifications": ["Bachelor's or graduate degree in Physics", "Strong math and analytical skills", "Research or lab experience"],
    },
}

# =============================================
# TKINTER APPLICATION
# =============================================

class STEMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Career Pathfinder")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(True, True)

        # Quiz state
        self.scores = {}
        self.current_q = 0
        self.answers = []
        self.selected_var = None
        self.top_match = None

        # Single container frame — all views render inside here
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(fill="both", expand=True)

        self.show_welcome()

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    # ── Welcome Screen ────────────────────────────────────────
    def show_welcome(self):
        self.clear()
        self.root.geometry("560x250")

        inner = tk.Frame(self.frame, bg="#f0f0f0")
        inner.pack(expand=True, padx=40, pady=30)

        tk.Label(inner, text="Career Pathfinder", font=("Helvetica", 28, "bold"),
                 fg="#2B6CB0", bg="#f0f0f0").pack(pady=(0, 6))
        tk.Label(inner, text="Discover the STEM career path best suited for you.",
                 font=("Helvetica", 11), fg="gray", bg="#f0f0f0").pack()
        tk.Label(inner, text="Answer 7 short questions to get your personalized result.",
                 font=("Helvetica", 11), fg="gray", bg="#f0f0f0").pack(pady=(0, 16))

        ttk.Separator(inner).pack(fill="x", pady=8)

        btn_frame = tk.Frame(inner, bg="#f0f0f0")
        btn_frame.pack(pady=6)

        tk.Button(btn_frame, text="Start Quiz", font=("Helvetica", 12, "bold"),
                  bg="#2B6CB0", fg="white", padx=20, pady=8,
                  relief="flat", cursor="hand2",
                  command=self.start_quiz).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Quit", font=("Helvetica", 11),
                  bg="#e0e0e0", padx=15, pady=8,
                  relief="flat", cursor="hand2",
                  command=self.root.quit).pack(side="left", padx=10)

    # ── Quiz Logic ────────────────────────────────────────────
    def start_quiz(self):
        # Reset scores for a fresh quiz
        self.scores = dict(scores_template)
        self.current_q = 0
        self.answers = []
        self.show_question()

    def show_question(self):
        self.clear()
        self.root.geometry("600x420")

        q_data = questions[self.current_q]
        question_text = q_data[0]
        options = q_data[1]

        inner = tk.Frame(self.frame, bg="#f0f0f0")
        inner.pack(fill="both", expand=True, padx=30, pady=20)

        # Progress bar row
        top = tk.Frame(inner, bg="#f0f0f0")
        top.pack(fill="x", pady=(0, 8))
        tk.Label(top, text=f"Question {self.current_q + 1} of {len(questions)}",
                 font=("Helvetica", 10), fg="gray", bg="#f0f0f0").pack(side="left")
        prog = ttk.Progressbar(top, length=220, mode="determinate")
        prog.pack(side="right")
        prog["value"] = int((self.current_q / len(questions)) * 100)

        # Question text
        tk.Label(inner, text=question_text, font=("Helvetica", 16, "bold"),
                 bg="#f0f0f0", wraplength=530, justify="left").pack(anchor="w", pady=(4, 10))

        ttk.Separator(inner).pack(fill="x", pady=4)

        # Radio buttons — standard loop like the original
        self.selected_var = tk.IntVar(value=-1)
        for j, opt in enumerate(options):
            tk.Radiobutton(inner, text=opt, variable=self.selected_var, value=j,
                           font=("Helvetica", 12), bg="#f0f0f0",
                           activebackground="#f0f0f0", pady=5).pack(anchor="w", padx=20)

        ttk.Separator(inner).pack(fill="x", pady=10)

        btn_row = tk.Frame(inner, bg="#f0f0f0")
        btn_row.pack(fill="x")
        tk.Button(btn_row, text="Next \u2192", font=("Helvetica", 11),
                  bg="#2B6CB0", fg="white", padx=16, pady=6,
                  relief="flat", cursor="hand2",
                  command=self.next_question).pack(side="right")

    def next_question(self):
        selected = self.selected_var.get()

        # Ensure the user actually selected an option
        if selected == -1:
            messagebox.showwarning("No Selection", "Please select an answer before continuing.")
            return

        self.answers.append(selected)

        # Tally the scores for the careers associated with the user's choice
        careers_maps = questions[self.current_q][2]
        for career in careers_maps[selected]:
            self.scores[career] += 1

        self.current_q += 1

        if self.current_q < len(questions):
            self.show_question()
        else:
            # Return the career with the highest score
            self.top_match = max(self.scores, key=self.scores.get)
            self.show_dashboard()

    # ── Results Dashboard ──────────────────────────────────────
    def show_dashboard(self):
        self.clear()
        self.root.geometry("660x560")

        inner = tk.Frame(self.frame, bg="#f0f0f0")
        inner.pack(fill="both", expand=True, padx=25, pady=15)

        tk.Label(inner, text="Your Results", font=("Helvetica", 22, "bold"),
                 fg="#2B6CB0", bg="#f0f0f0").pack(pady=(0, 8))

        # Top match highlight card
        top_card = tk.Frame(inner, bg="#d4e8ff", relief="ridge", bd=2)
        top_card.pack(fill="x", pady=(0, 8))
        tk.Label(top_card, text="Your Top Match:", font=("Helvetica", 10),
                 fg="#555", bg="#d4e8ff").pack(anchor="w", padx=12, pady=(8, 0))
        tk.Label(top_card, text=pathways[self.top_match]["title"],
                 font=("Helvetica", 18, "bold"), fg="#2B6CB0", bg="#d4e8ff").pack(anchor="w", padx=12)
        tk.Button(top_card, text="View My Pathway \u2192",
                  font=("Helvetica", 10, "bold"), bg="#2B6CB0", fg="white",
                  relief="flat", cursor="hand2", padx=12, pady=5,
                  command=lambda: self.show_pathway(self.top_match)).pack(anchor="w", padx=12, pady=(4, 10))

        ttk.Separator(inner).pack(fill="x", pady=6)

        tk.Label(inner, text="Explore All 7 STEM Careers:",
                 font=("Helvetica", 11, "bold"), bg="#f0f0f0").pack(anchor="w")

        # Career grid — sorted by score descending
        grid = tk.Frame(inner, bg="#f0f0f0")
        grid.pack(fill="both", expand=True, pady=6)

        sorted_careers = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        for i, (career, score) in enumerate(sorted_careers):
            row, col = divmod(i, 2)
            card = tk.Frame(grid, bg="white", relief="groove", bd=1)
            card.grid(row=row, column=col, padx=6, pady=4, sticky="ew")
            grid.columnconfigure(col, weight=1)

            tk.Label(card, text=pathways[career]["title"],
                     font=("Helvetica", 10, "bold"), bg="white", fg="#222").pack(anchor="w", padx=8, pady=(6, 0))
            tk.Label(card, text=f"Score: {score}",
                     font=("Helvetica", 9), bg="white", fg="gray").pack(anchor="w", padx=8)
            tk.Button(card, text="Explore \u2192", font=("Helvetica", 9),
                      bg="#e8f0fe", fg="#2B6CB0", relief="flat", cursor="hand2", padx=6, pady=2,
                      command=lambda c=career: self.show_pathway(c)).pack(anchor="w", padx=8, pady=(2, 6))

        tk.Button(inner, text="Retake Quiz", font=("Helvetica", 10),
                  bg="#e0e0e0", padx=12, pady=4, relief="flat", cursor="hand2",
                  command=self.start_quiz).pack(pady=(6, 0))

    # ── Pathway Detail View ────────────────────────────────────
    def show_pathway(self, career_key):
        self.clear()
        self.root.geometry("680x580")
        p = pathways[career_key]

        # Canvas + scrollbar for scrollable content
        canvas = tk.Canvas(self.frame, bg="#f0f0f0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg="#f0f0f0")

        inner.bind("<Configure>",
                   lambda _: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Cross-platform mouse wheel scroll
        def _scroll(event):
            if event.delta:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

        canvas.bind_all("<MouseWheel>", _scroll)
        canvas.bind_all("<Button-4>", _scroll)
        canvas.bind_all("<Button-5>", _scroll)

        # ── Pathway Content ──
        tk.Label(inner, text=p["title"], font=("Helvetica", 20, "bold"),
                 fg="#2B6CB0", bg="#f0f0f0").pack(anchor="w", pady=(12, 4), padx=20)
        tk.Label(inner, text=p["description"], font=("Helvetica", 10),
                 bg="#f0f0f0", fg="#333", wraplength=600, justify="left").pack(anchor="w", pady=(0, 8), padx=20)

        def section_header(title):
            tk.Label(inner, text=f"\u2500\u2500 {title} \u2500\u2500",
                     font=("Helvetica", 11, "bold"), fg="#2B6CB0", bg="#f0f0f0").pack(anchor="w", padx=20, pady=(10, 2))
            ttk.Separator(inner).pack(fill="x", padx=20)

        def add_items(items, numbered=False):
            for i, item in enumerate(items):
                prefix = f"{i+1}. " if numbered else "\u2022 "
                if isinstance(item, tuple):
                    tk.Label(inner, text=f"{prefix}{item[0]}",
                             font=("Helvetica", 10, "bold"), bg="#f0f0f0").pack(anchor="w", padx=36, pady=(4, 0))
                    tk.Label(inner, text=item[1], font=("Helvetica", 9),
                             fg="#555", bg="#f0f0f0", wraplength=580, justify="left").pack(anchor="w", padx=46, pady=(0, 2))
                else:
                    tk.Label(inner, text=f"{prefix}{item}",
                             font=("Helvetica", 10), bg="#f0f0f0").pack(anchor="w", padx=36, pady=2)

        section_header("Recommended High School Courses")
        add_items(p["courses"], numbered=True)

        section_header("Recommended Extracurriculars")
        add_items(p["extracurriculars"], numbered=True)

        # Post-secondary with clickable hyperlinks (3 per career)
        section_header("Post-Secondary Options")
        for i, (name, desc, url) in enumerate(p["postsecondary"]):
            row_f = tk.Frame(inner, bg="#f0f0f0")
            row_f.pack(anchor="w", padx=36, pady=(4, 0), fill="x")
            tk.Label(row_f, text=f"{i+1}. {name}",
                     font=("Helvetica", 10, "bold"), bg="#f0f0f0").pack(anchor="w")
            tk.Label(row_f, text=desc, font=("Helvetica", 9),
                     fg="#555", bg="#f0f0f0", wraplength=580, justify="left").pack(anchor="w", padx=10)
            # Clickable hyperlink label — opens in default browser
            link = tk.Label(row_f, text=url, font=("Helvetica", 9, "underline"),
                            fg="#1a73e8", bg="#f0f0f0", cursor="hand2")
            link.pack(anchor="w", padx=10, pady=(0, 4))
            def open_link(_, u=url):
                try:
                    webbrowser.open(u)
                except Exception:
                    messagebox.showinfo("Link", u)
            link.bind("<Button-1>", open_link)

        section_header("Key Certifications")
        tk.Label(inner, text=p["certifications"], font=("Helvetica", 10),
                 bg="#f0f0f0", justify="left").pack(anchor="w", padx=36, pady=(4, 0))

        section_header("Entry Level Jobs")
        for i, job in enumerate(p["jobs"]):
            tk.Label(inner, text=f"  {i+1}. {job}",
                     font=("Helvetica", 10), bg="#f0f0f0").pack(anchor="w", padx=36, pady=2)

        section_header("Common Qualifications")
        for qual in p["qualifications"]:
            tk.Label(inner, text=f"  \u2022 {qual}", font=("Helvetica", 10),
                     bg="#f0f0f0", wraplength=580, justify="left").pack(anchor="w", padx=36, pady=2)

        # Back button — unbinds scroll events before switching views
        def go_back():
            canvas.unbind_all("<MouseWheel>")
            canvas.unbind_all("<Button-4>")
            canvas.unbind_all("<Button-5>")
            self.show_dashboard()

        tk.Button(inner, text="\u2190 Back to Results", font=("Helvetica", 10),
                  bg="#e0e0e0", padx=10, pady=4, relief="flat", cursor="hand2",
                  command=go_back).pack(pady=15, padx=20, anchor="w")


if __name__ == "__main__":
    root = tk.Tk()
    app = STEMApp(root)
    root.mainloop()

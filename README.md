# CodeEcho CLI

## One Sentence Value

CodeEcho is a CLI learning platform designed to help ADHD learners learn programming through synchronized audio explanations and step-by-step code exploration.

---

# Project Overview

CodeEcho is a programming learning platform that runs entirely in the **Command Line Interface (CLI)**.

The platform was designed to help beginners learn programming in a **structured and distraction-reduced environment**, especially learners who struggle with attention and focus such as people with **ADHD (Attention Deficit Hyperactivity Disorder)**.

Unlike traditional platforms that rely heavily on long video explanations, CodeEcho focuses on:

* step-by-step learning
* minimal interface distractions
* synchronized audio explanations
* visual guidance during lessons

The goal of the platform is to make programming learning **clear, focused, and easier to follow**.

---

# The Problem

Most programming platforms teach through **long videos** where instructors explain multiple ideas at once.

This can create several problems for learners:

* difficulty maintaining attention
* cognitive overload
* losing track of the current concept
* getting distracted easily

These problems are especially common for learners with **ADHD**.

---

# The Solution

CodeEcho introduces a different learning approach.

Instead of watching a full video lesson, the learner experiences the lesson as:

Code line
↓
Audio explanation for that line
↓
Move to the next concept

This allows the learner to focus on **one idea at a time**, reducing distraction and improving comprehension.

---

# Core Innovation

The main idea behind CodeEcho is:

## Audio-Synchronized Code Learning

During lessons:

* the code appears on the screen
* an audio explanation is played
* the lesson progresses step by step

This design helps the learner stay focused and follow the explanation more easily.

---

# Code Line Highlighting

While the audio explanation is playing, the **current line of code is highlighted**.

This helps learners:

* identify the exact line being explained
* visually follow the lesson progression
* avoid confusion when reading multiple lines of code
* maintain attention on the current concept

This feature is especially useful for learners with ADHD who may struggle with tracking long blocks of text.

---

# Key Features

## User Authentication

* User registration
* Secure login system
* Password recovery
* Email verification using OTP

---

## Multiple Learning Paths

The platform currently includes several programming learning paths:

* Python
* Java
* C++

Each path contains structured lessons that gradually build programming knowledge.

---

## Step-by-Step Learning

Users cannot randomly jump to advanced lessons.

Lessons follow a clear learning order:

Lesson 1
↓
Lesson 2
↓
Lesson 3

This structure helps learners stay focused and avoid confusion.

---

## Progress Tracking

The system automatically saves the learner's progress including:

* completed lessons
* learning progress
* lesson advancement

This gives learners a **sense of achievement** and encourages them to continue learning.

---

## Focus Mode

Before starting a lesson the platform activates a **focus timer**.

This feature helps learners:

* prepare for a learning session
* reduce external distractions
* enter a focused learning state

---

## Community Questions System

The platform includes a simple community feature where users can:

* ask programming questions
* view questions posted by other learners
* share learning challenges

This helps create a small collaborative learning environment.

---

# Technologies Used

The project was built using the following technologies:

* Python
* JSON (for data storage)
* Colorama (for CLI styling)
* pyttsx3 (text-to-speech audio explanation)
* python-dotenv (environment variables)
* SMTP (email verification)

---

# Installation

Clone the repository:

```bash
git clone <repository-link>
```

Navigate to the project folder:

```bash
cd CodeEcho
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the application using:

```bash
python main.py
```

---

# Usage

After running the program, the user interacts with the platform through the CLI menus.

Example flow:

1. Start the application
2. Register a new account or login
3. Access the dashboard
4. Choose a learning path
5. Select a lesson
6. Follow the step-by-step lesson with synchronized audio explanation
7. Complete the quiz
8. Progress is saved automatically

Example CLI commands inside the platform:

* Select learning path by number
* Enter lesson number to start learning
* Press **Enter** to continue
* Type **B** to go back to the previous menu

---

# Environment Variables

Create a `.env` file and add:

```env
CODEECHO_EMAIL=your_email@gmail.com
CODEECHO_APP_PASSWORD=your_app_password
```

These values are used to send verification emails.

---

# Future Improvements

Future versions of CodeEcho may include:

* AI learning assistant
* deeper programming courses
* personalized learning paths
* adaptive learning for ADHD learners

The long-term goal is to build a platform that improves programming education accessibility for learners with ADHD.

---

# Author

CodeEcho was developed as a Python CLI learning platform prototype focused on improving the learning experience for programmers who struggle with attention and distraction.

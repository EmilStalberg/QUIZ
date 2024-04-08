questions = [
    {
        "question": "What is the capital of Turkey?",
        "options": ["A: Istanbul", "B: Izmir", "C: Ankara", "D: Adana"],
        "answer": "C"
    },

     {
        "question": "What is the capital of China?",
        "options": ["A: Shanghai", "B: Shenzhen", "C: Guangzhou", "D: Beijing"],
        "answer": "D"
    },
   
    {
        "question": "What is the capital of Colombia?",
        "options": ["A: Bogotoa", "B: Cali", "C: Cartagena", "D: Medellin"],
        "answer": "A"
    },
   
    {
        "question": "What is the capital of Morocco?",
        "options": ["A: Casablanca", "B: Marrakech", "C: Tanger", "D: Rabat"],
        "answer": "D"
    },

{
        "question": "What is the capital of Saudi Arabia?",
        "options": ["A: Medina", "B: Mecca", "C: Riyadh", "D: Jeddah"],
        "answer": "C"
    },

{
        "question": "What is the capital of Kosovo?",
        "options": ["A: Mitrovica", "B: Prizren", "C: Ferizaj", "D: Pristina"],
        "answer": "D"
    },

{
        "question": "What is the capital of India?",
        "options": ["A: New Delhi", "B: Mumbai", "C: Chennai", "D: Banglore"],
        "answer": "A"
    },

{
        "question": "What is the capital of Switzerland?",
        "options": ["A: Basel", "B: Bern", "C: Zurich", "D: Geneve"],
        "answer": "B"
    },

    {
        "question": "What is the biggest city in Florida?",
        "options": ["A: Orlando", "B: Tampa", "C: Miami", "D: Jacksonville"],
        "answer": "D"
    },

    {
        "question": "In what country is Nairobi the capital ?",
        "options": ["A: Nigeria", "B: Ghana", "C: Kenya", "D: DR Congo"],
        "answer": "C"
    },

   ]

   # This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")


# Run
run_quiz(questions)
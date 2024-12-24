import google.generativeai as genai

    
genai.configure(api_key="AIzaSyBamCfjQfvXxgYRmOngc6yWwVeQIULspZ8")


BASE_PROMPT = """
You are an assistant helping grade coding assignments. Evaluate the student's code based on the provided marking scheme.
Focus on logic and readability. If the code is incomplete but has a correct approach, assign partial marks. Provide detailed
feedback for improvement.
"""

def generate_feedback(question, code, marking_scheme):

    prompt = f"""
    {BASE_PROMPT}

    Question: {question}

    Marking Scheme: {marking_scheme}

    Student's Code:
    ```
    {code}
    ```

    Evaluate the code and provide a grade along with feedback based on the marking scheme.
    """
    
    try:
       
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        feedback = model.generate_content(prompt)
        
        if feedback and feedback.candidates:
            feedback_text = feedback.candidates[0].content.parts[0].text
            return feedback_text
        else:
            return "No feedback generated. Please check the API response."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    
    question = input("Enter the question:\n")
    
    
    student_code = input("Enter the student's code:\n")

   
    marking_scheme = input("Enter the marking scheme:\n")

 
    feedback = generate_feedback(question, student_code, marking_scheme)
    print("\nFeedback and Grade:\n", feedback)

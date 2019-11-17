"""Trivia Quiz"""

def question(prompt, answer):
    response = input(prompt)

    if response == answer:
        print("You got it!")
        return 1 
    else:
        print("Sorry, wrong answer!")
        return 0  

if __name__ == "__main__":

    prompts = ["Cat urine glows in the dark. Enter a 1 for false and a 0 for true:", 
    "Name the world’s biggest island. Please enter a character from a-e: \na)Greenland\nb)Puerto Rico\nc)Fiji\nd)Sumatra\ne)Luzon\nYour answer: ",
    "Name the world’s largest ocean. Please enter a character from a-d:\na) Atlantic\nb) Pacific\nc) Southern\nd) Indian\n Your answer: ",
    "What is the diameter (in miles) of Earth? Please enter an integer: ",
    "Coprastastaphobia is the fear of constipation. Enter a 0 for false and a 1 for true: "]

    answers = ["1", "a", "b", "8000", "1"]  
    score = 0
    for i in range(len(prompts)):
        score += question(prompts[i], answers[i])    

    print(score)

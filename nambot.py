import speech_recognition as sr
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Error with the speech service.")
        return ""

def predefined_answers(question):
    answers = {
        "what is your name": "I am Heyy Buddyy, your voice assistant!",
        "who created you": "I was created by an awesome developer!",
        "what is raspberry pi": "Raspberry Pi is a small, affordable computer used for learning, coding, and IoT projects.",
        "how does a voice assistant work": "A voice assistant converts speech into text, processes it, and provides a response using AI or predefined data.",
        "who created python": "Python was created by Guido van Rossum and first released in 1991.",
        "what is ai": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines.",
        "tell me a joke": "Why don’t programmers like nature? Too many bugs!",
        "what is the capital of france": "The capital of France is Paris.",
        "where is shetty college": "Shetty College is in Kalburagi.",
        "shetty": "Shetty Institute of Technology (SIT) is an engineering college in Kalburagi, affiliated with VTU and approved by AICTE.",
        "college": "A college is an educational institution that offers higher education and degrees.",
        "shetty institute of technology": "Shetty Institute of Technology (SIT) is located in Kalburagi, Karnataka, and offers B.E. courses in multiple disciplines.",
        "sit kalaburagi": "SIT Kalaburagi is an engineering college affiliated with VTU, offering B.E. courses in CSE, EEE, Civil, and more.",
        "sit courses": "SIT offers B.E. programs in Computer Science, AI & ML, Electrical & Electronics, Civil, and Mechanical Engineering.",
        "sit hostel": "Yes, SIT provides hostel facilities for both boys and girls.",
        "sit admission": "Admissions to SIT are based on KCET, COMEDK, JEE Main, and AIEEE scores.",
        "sit fee": "For exact fee details, please contact the SIT admissions office.",
        "sit placement": "SIT has a placement cell, and the highest package offered has been Rs 3.5 lakh per annum.",
        "sit address": "Shetty Institute of Technology is located on Shahbad Road, Kalaburagi, Karnataka 585105.",
        "sit transport": "SIT is about 8 km from Kalaburagi Junction Railway Station and 15 km from Kalaburagi Airport."
    }
    
    for key in answers:
        if key in question:
            return answers[key]
    
    return "I don't know that. Try asking something else."

def main():
    speak("Heyy Buddyy is ready. How can I help?")
    while True:
        command = listen()
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        response = predefined_answers(command)
        print("Assistant:", response)
        speak(response)

if __name__ == "__main__":
    main()

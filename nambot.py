import speech_recognition as sr
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed for better clarity
    engine.setProperty('voice', 'english')  # Use default espeak voice
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("Error with the speech service.")
            return ""
        except sr.WaitTimeoutError:
            print("No speech detected, try again.")
            return ""

def predefined_answers(question):
    answers = {
        "what is your name": "I am Heyy Buddyy, your Raspberry Pi voice assistant!",
        "who created you": "I was created by an awesome developer!",
        "what is raspberry pi": "Raspberry Pi is a small, affordable computer used for learning, coding, and IoT projects.",
        "how does a voice assistant work": "A voice assistant converts speech into text, processes it, and provides a response using AI or predefined data.",
        "who created python": "Python was created by Guido van Rossum and first released in 1991.",
        "what is ai": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines.",
        "tell me a joke": "Why don’t programmers like nature? Too many bugs!",
        "exit": "Goodbye!"
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

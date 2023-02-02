import pyttsx3

engine = pyttsx3.init()


def speak():
    print("[+] Print exit to quit")
    while True: 
        text = input("What do you want to say?")

        if text == "exit":
            break
        else: 
            engine.say(text)
            engine.runAndWait()


speak()
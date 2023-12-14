############# IMPORT #############
import os
import pyttsx3
import speech_recognition
from datetime import date, datetime

############# init #############
robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
############# Ear #############
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You:", you)
    ############# AI #############
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "turn on music" in you:
        music = ""
        robot_brain = "Whose music do you want to listen to?"
        if music == "":
            robot_brain = "can not open "
    elif "hello" in you:
        robot_brain = "Hello Hope"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "game" in you:
        try:
            game_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\lol.lnk"
            os.startfile(game_path)
            robot_brain = "Playing game"
        except:
            robot_brain = "Không thể mở game"
    elif "bye" in you:
        robot_brain = "good bye, see you again"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"
    print("Robot react:", robot_brain)
    ############# MOUTH #############
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

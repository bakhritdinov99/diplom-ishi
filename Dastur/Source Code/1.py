from tkinter import *
from tkinter import messagebox
import json
import pyttsx3
from difflib import get_close_matches
from show import forshow,openImg
import azure.cognitiveservices.speech as speechsdk
import requests
from itertools import cycle
from PIL import ImageTk, Image

engine=pyttsx3.init()

i=0
def azureAudio():
    speech_config = speechsdk.SpeechConfig(subscription="25b1bfa6df5e4b0f9c0692025532e7a5", region="eastus")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = 'uz-UZ-MadinaNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    text = enterwordentry.get()
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        pass
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))

def azureMeaning():
    speech_config = speechsdk.SpeechConfig(subscription="25b1bfa6df5e4b0f9c0692025532e7a5", region="eastus")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = 'uz-UZ-MadinaNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    # print("Enter some text that you want to speak >")
    text = textarea.get(1.0,END)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        pass
        # print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        # print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                # print("Did you set the speech resource key and region values?")

def wordaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(enterwordentry.get())
    engine.runAndWait()

def  meaningaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

def onClick():
    messagebox.showinfo("Dasturchi haqida.", "Farrux Baxritdinov t.me/mrcoder_99")

def iexit():
    res = messagebox.askyesno('Chiqish', 'Dasturdan chiqmoqchimisiz?')
    if res == True:
        root.destroy()
    else:
        pass

def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0, END)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

def textToSign(word):
    separateWord = list(word)
    openImg(separateWord)



def search():
    data = json.load(open('data.json'))
    word = enterwordentry.get()

    word = word.lower()


    if word in data:
        meaning = data[word]
        textToSign(word)

        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')

        textarea.config(state=DISABLED)

    elif len(get_close_matches(word, data.keys())) > 0:

        close_match = get_close_matches(word, data.keys())[0]

        res = messagebox.askyesno('Diqqat', 'Siz balki ' + close_match + ' ni qidirayotgandirsiz?')

        if res == True:

            meaning = data[close_match]
            textarea.delete(1.0, END)
            textarea.config(state=NORMAL)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')

            textarea.config(state=DISABLED)

        else:
            textarea.delete(1.0, END)
            messagebox.showinfo('Ma\'lumot', "Iltimos,so'zni to'g'ri kiriting")
            enterwordentry.delete(0, END)


    else:
        messagebox.showerror('Xatolik', 'So\'zni to\'g\'ri kiritmadingiz. Iltimos, so\'zni to\'g\'ri kiriting')
        enterwordentry.delete(0, END)

def onlineOffline():
    if is_on==True:
        azureAudio()
    else:
        wordaudio()

def onlineOfflineMeaning():
    if is_on==True:
        azureMeaning()
    else:
        meaningaudio()

def onSearch():
    url = "http://dictionary.firefox.uz/api/words/search"
    wordapi=enterwordentry.get()
    payload = {'key': wordapi}
    files = [
    ]
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    aList = json.loads(response.text)
    meaningList = [aList[0]['definition']]

    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.insert(END, u'\u2022' + meaningList[0] + '\n\n')
    textarea.config(state=DISABLED)

def onlineSearch():
    if is_on == True:
        onSearch()
    else:
        search()

def func(event):
    if is_on == True:
        onSearch()
    else:
        search()

root = Tk()
root.geometry('1000x626+100+50')

root.title("Izohli lug'at")
root.wm_iconbitmap("dic.ico")

root.resizable(0, 0)

# style = Style()

root.configure(bg='#f7f7f7')
bgimage = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=100)


enterwordTitle = Label(root, text="O'zbek tilining elektron izohli lug'atida so'zlarni ovozli taqdim etish va barmoqlar", font=('Times', 22,), fg='red3', bg='whitesmoke')
enterwordTitle.place(x=30, y=10)

enterwordTitle2 = Label(root, text="yordamida imo-ishoralar orqali tasvirlash uchun dasturiy ta'minot", font=('Times', 22,), fg='red3', bg='whitesmoke')
enterwordTitle2.place(x=120, y=42)


enterwordLabel = Label(root, text="So'zni kiriting", font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=500, y=140)

enterwordentry = Entry(root, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
enterwordentry.place(x=510, y=200)

enterwordentry.focus_set()

searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=onlineSearch)
searchButton.place(x=550, y=260)

micimage = PhotoImage(file='volume.png')
micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                   cursor='hand2',command=onlineOffline)
micButton.place(x=640, y=260)

signimage = PhotoImage(file='sign.png')
signButton = Button(root, image=signimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=forshow)
signButton.place(x=730, y=260)


meaninglabel = Label(root, text="Ma'nosi", font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
meaninglabel.place(x=580, y=330)

textarea = Text(root, font=('arial', 18, 'bold'), height=5, width=34, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=472, y=380)

#about programmer

aboutimage = PhotoImage(file='information.png')
aboutButton = Button(root, image=aboutimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                     cursor='hand2',command=onClick)
aboutButton.place(x=480, y=555)

# Keep track of the button state on/off
global is_on
is_on = True

# Create Label
my_label = Label(root,
                 text="Online rejim faol!",
                 fg="green",
                 font=("Helvetica", 18))

my_label.pack(pady=20)
my_label.place(x=0, y=100)

# Define our switch function
def switch():
    global is_on


    # Determine is on or off
    if is_on:
        on_button.config(image=off)
        my_label.config(text="Online rejim nofaol!",
                        fg="grey")
        is_on = False
    else:

        on_button.config(image=on)
        my_label.config(text="Online rejim faol!", fg="green")
        is_on = True


# Define Our Images
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

# Create A Button
on_button = Button(root, image=on, bd=0,
                   command=switch)
on_button.pack(pady=50)
on_button.place(x=55, y=133)

audioimage = PhotoImage(file='volume2.png')
audioButton = Button(root, image=audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                     cursor='hand2',command=onlineOfflineMeaning)
audioButton.place(x=570, y=555)

picimage = PhotoImage(file='speakpic.png')
picButton = Button(root, image=picimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                     cursor='hand2',command=forshow)
picButton.place(x=660, y=555)

clearimage = PhotoImage(file='clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2'
                     , command=clear)
clearButton.place(x=750, y=555)

exitimage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                    command=iexit)
exitButton.place(x=850, y=555)
# for enter button
root.bind('<Return>', func)

root.mainloop()
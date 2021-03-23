import speech_recognition as sr

def convert():
    r = sr.Recognizer()
    repeat_keywords = {'Once':1,'Double':2, 'Triple':3, 'once':1,'double':2, 'triple':3}
    rules = {'C M':'CM','c m':'CM', 'dollars':'$', 'Dollars':'$'}
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        s = r.recognize_google(audio)
        print(s)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    repeats = 0
    s = [ss.strip() for ss in s.split()][::-1]

    for i in range(len(s) - 1):
        if s[i - repeats + 1] in repeat_keywords:
            s[i - repeats] *= repeat_keywords[s[i - repeats + 1]]

            del s[i - repeats + 1]
            repeats += 1

        if s[i - repeats + 1] in rules:
            s[i - repeats] = rules[s[i - repeats + 1]]

        print(' '.join(s[::-1])) 
import speech_recognition as speech_recog

def speech(lang="pl-PL"):
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Zbieranie dźwięków tła...")
        recog.adjust_for_ambient_noise(audio_file)
        print("Nagrywanie...")
        audio = recog.listen(audio_file)
        print("Transkrypcja, proszę czekać...")

        return recog.recognize_google(audio, language=lang)
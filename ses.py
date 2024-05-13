import speech_recognition as sr
import cv2

# Initialize the recognizer for speech-to-text
r = sr.Recognizer()

def speech_to_text_turkish():
    """Performs speech-to-text recognition in Turkish."""
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:
            print("Sesinizi kaydediyorum...")  # Inform user about recording (Turkish)

            # Adjust for ambient noise to improve accuracy
            r.adjust_for_ambient_noise(source, duration=0.2)

            # Listen for user input
            audio = r.listen(source)

            # Recognize speech using Google Speech Recognition with Turkish model
            text = r.recognize_google(audio, language='tr-TR')
            print("Dinledim: ", text)  # Display recognized text (Turkish)
            return text.lower()

    except sr.RequestError as e:
        print("İstek işlenemedi; {0}".format(e))  # Error message in Turkish
        return None
    except sr.UnknownValueError:
        print("Bilinmeyen hata oluştu")  # Generic error message in Turkish
        return None

while True:
    user_text = speech_to_text_turkish()
    if user_text:
        print("Kullanıcı dedi ki:", user_text)  # Print the recognized text
        
    # Check if 'q' key is pressed to break out of the loop
    key = cv2.waitKey(1)
    if key & 0xFF == ord('a'):
        break

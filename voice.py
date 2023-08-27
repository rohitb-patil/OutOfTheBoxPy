import speech_recognition as sr
import webbrowser

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print("Please say something:")
    audio = recording.listen(source)

try:
    user_input = recording.recognize_google(audio)
    print("You said:\n" + user_input)

    # Use the user_input variable as the query
    query = user_input
    search_results = list(search(query, tld="co.in", num=10, stop=10, pause=2))

    if search_results:
        first_result = search_results[0]
       # webbrowser.open(first_result)
    else:
        print("No search results found.")

except Exception as e:
    print(e)
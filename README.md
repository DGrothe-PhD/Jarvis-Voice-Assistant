----------------  Voice Assistant Bot (Jarvis)  ----------------

The Voice Assistant Bot, named Jarvis, is a Python-based voice assistant that leverages various libraries to provide a conversational interface and perform a range of tasks based on voice commands. Jarvis can play music, provide current time information, fetch Wikipedia summaries, crack jokes, and more.
But be informed that Jarvis only answers if you call his name.

• Features

1. Speech Recognition: The bot utilizes the SpeechRecognition library to convert speech into text, allowing users to interact with Jarvis using voice commands.

2. Text-to-Speech Conversion: The pyttsx3 library is used to convert text-based responses into speech, enabling Jarvis to provide audio feedback to users.

3. YouTube Music Playback: Jarvis can play music on YouTube using the pywhatkit library. Users can command Jarvis to play a specific song, and it will fetch and play the song from YouTube.

4. Time Information: By recognizing voice commands containing the word "time," Jarvis provides the current time using the datetime library.

5. Wikipedia Summary: Jarvis can fetch a summary from Wikipedia based on voice commands starting with words like "who," "what," "when," or "where."

6. Jokes: Jarvis can crack jokes using the pyjokes library. Users can ask Jarvis for a joke, and it will generate and share a random joke.

• Prerequisites

To run Jarvis, you need to have the following libraries installed:
1. speech_recognition
2. pyttsx3
3. pywhatkit
4. datetime
5. wikipedia
6. pyjokes

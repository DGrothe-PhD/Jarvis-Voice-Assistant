Voice Assistant Bot (Jarvis)

The Voice Assistant Bot, named Jarvis, is a Python-based voice assistant that leverages various libraries to provide a conversational interface and perform a range of tasks based on voice commands. Jarvis can play music, provide current time information, fetch Wikipedia summaries, crack jokes, and more.

Features
Speech Recognition: The bot utilizes the SpeechRecognition library to convert speech into text, allowing users to interact with Jarvis using voice commands.

Text-to-Speech Conversion: The pyttsx3 library is used to convert text-based responses into speech, enabling Jarvis to provide audio feedback to users.

YouTube Music Playback: Jarvis can play music on YouTube using the pywhatkit library. Users can command Jarvis to play a specific song, and it will fetch and play the song from YouTube.

Time Information: By recognizing voice commands containing the word "time," Jarvis provides the current time using the datetime library.

Wikipedia Summary: Jarvis can fetch a summary from Wikipedia based on voice commands starting with words like "who," "what," "when," or "where." The wikipedia library is used to retrieve the summary.

Jokes: Jarvis can crack jokes using the pyjokes library. Users can ask Jarvis for a joke, and it will generate and share a random joke.

Prerequisites
To run Jarvis, you need to have the following libraries installed:

speech_recognition
pyttsx3
pywhatkit
datetime
wikipedia
pyjokes

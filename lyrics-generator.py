from openai import OpenAI

# remove this before committing
API_KEY = ""

client = OpenAI(api_key=API_KEY)

audio_file = open("/filepath.m4p", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcript.text)
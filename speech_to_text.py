import whisper
import json
import os
model = whisper.load_model("large-v2")
audios = os.listdir("audios")
for audio in audios:
    print(audio)
    result = model.transcribe(audio="",language = "hi",task = "translate" ,word_timestamps=False)


    chunks = []
    for segment in result["segments"]:
        chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

    print(chunks)

    with open("output.json", "w") as f:
        json.dump(chunks,f)
        
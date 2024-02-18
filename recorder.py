from pvrecorder import PvRecorder
import soundfile as sf
import time
import transcript
import numpy as np
import speech_recognition as sr

def audio_transcription_thread(audio_file):
    transcript.audio_to_latex(audio_file)

def start_record():
    recognizer = sr.Recognizer()
    for index, device in enumerate(PvRecorder.get_available_devices()):
        print(f"[{index}] {device}")
    #change to microphone index you want to use
    recorder = PvRecorder(device_index=0, frame_length=512)
    audio = []
    t_start = time.time()
    try:
        recorder.start()
        while recorder.is_recording:
            frame = recorder.read()
            audio.extend(frame)
            # t_elapsed = time.time() - t_start
            #print(f"Recording duration: {t_elapsed:.2f} seconds", end='\r')
            # add real time api calls

            #save temp audio file
            # audio_np = np.array(audio, dtype='int16')
            # with sf.SoundFile("resources/.temp.flac", 'w', samplerate=16000, channels=1, subtype="PCM_16") as f:
            #     f.write(audio_np)
                # Multithreading for audio transcription
                # thread = threading.Thread(target=audio_transcription_thread, args=("ressources/.temp.flac",))
                # thread.start()
            
    except KeyboardInterrupt:
        recorder.stop()
        audio_np = np.array(audio, dtype='int16')
        with sf.SoundFile("resources/output.flac", 'w', samplerate=16000, channels=1, subtype="PCM_16") as f:
            f.write(audio_np)
    finally:
        recorder.delete()
    # transcript.audio_to_latex("resources/output.flac")
    return "resources/output.flac"

if __name__ == "__main__":
    start_record()
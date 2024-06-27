from pydub import AudioSegment
from pydub import AudioSegment
import os

def merge_wav_files(input_files, output_file):
    # Initialize an empty AudioSegment
    combined = AudioSegment.empty()

    # Loop through the input files and append them to the combined AudioSegment
    for file in input_files:
        audio = AudioSegment.from_wav(file)
        combined += audio

    # Export the combined AudioSegment to a new file
    combined.export(output_file, format="wav")

# List of input WAV files
input_files = []  # Replace with your file names
for i in range(1,155):
    input_files.append(f"static/wavs/{i}.wav")
    print(input_files)
# Output file name
output_file = "combined4.wav"

# Merge the files
merge_wav_files(input_files, output_file)

print(f"Combined WAV file saved as {output_file}")

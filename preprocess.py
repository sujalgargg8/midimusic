from magenta.music import midi_io
import tensorflow as tf
import os

def convert_midi(directory):
    sequences = []
    for filename in os.listdir(directory):
        if filename.endswith('.mid') or filename.endswith('.midi'):
            midi_path = os.path.join(directory, filename)
            sequence = midi_io.midi_to_note_sequence(tf.io.gfile.GFile(midi_path, 'rb').read())
            sequences.append(sequence)
    return sequences

if __name__ == '__main__':
    data_dir = './data'
    note_sequences = convert_midi(data_dir)
    print(f"Processed {len(note_sequences)} MIDI files.")

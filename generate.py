from magenta.models.music_vae import TrainedModel, configs
from magenta.music import note_seq

def generate():
    config = configs.CONFIG_MAP['cat-mel_2bar_small']
    music_vae = TrainedModel(config, batch_size=4, checkpoint_dir_or_path='./training_checkpoints')
    generated_sequences = music_vae.sample(n=10)
    for sequence in generated_sequences:
        note_seq.plot_sequence(sequence)
        note_seq.play_sequence(sequence, synth=note_seq.fluidsynth)

if __name__ == '__main__':
    generate()

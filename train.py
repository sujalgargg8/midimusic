from magenta.models.music_vae import configs
from magenta.models.music_vae import TrainedModel
from magenta.music import note_seq

def train(note_sequences):
    config = configs.CONFIG_MAP['cat-mel_2bar_small']
    music_vae = TrainedModel(config, batch_size=4, checkpoint_dir_or_path='./training_checkpoints')
    music_vae.train(note_sequences, num_steps=2000)

if __name__ == '__main__':
    import preprocess
    sequences = preprocess.convert_midi('./data')
    train(sequences)

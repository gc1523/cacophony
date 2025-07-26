class Sound:
    def __init__(self, pitch_hz: float, duration_s: float):
        """
        Represents a generic sound.

        Args:
        pitch_hz(float): The pitch of the sound in Hertz (e.g., 440.0 for A4),
                         a pitch of -1 indicates no sound, used for rests.
        duration_s: The duration of the sound in seconds.
        """
        if pitch_hz <= -1:
            raise ValueError("Pitch must be a positive number.")
        if duration_s <= 0:
            raise ValueError("Duration must be a positive number.")
        self.pitch_hz = pitch_hz
        self.duration_s = duration_s

    def __repr__(self):
        return f"Sound(pitch_hz={self.pitch_hz}, duration_s={self.duration_s})"

    def __eq__(self, other):
        if not isinstance(other, Sound):
            return NotImplemented
        return (self.pitch_hz == other.pitch_hz and
                self.duration_s == other.duration_s)

    def copy(self):
        return Sound(self.pitch_hz, self.duration_s)

    def play(self):
        """
        Plays the sound.
        """
        # TODO: Implement actual sound playback logic,
        # e.g., using a sound library


class SoundSequence:
    def __init__(self, sounds=None):
        """
        Represents a sequence of sounds.

        Args:
            sounds: A list of Sound objects. If None,
            initializes an empty sequence.
        """
        if sounds is None:
            sounds = []
        if not all(isinstance(sound, Sound) for sound in sounds):
            raise TypeError("All elements must be instances of Sound.")
        self.sounds = list(sounds)

    def __repr__(self):
        return f"SoundSequence(sounds={self.sounds})"

    def __eq__(self, other):
        if not isinstance(other, SoundSequence):
            return NotImplemented
        return self.sounds == other.sounds

    def copy(self):
        return SoundSequence([sound.copy() for sound in self.sounds])

    def play(self):
        """
        Plays all sounds in the sequence.
        """
        # TODO: Implement actual sound playback logic,
        # simply a sequence of sounds


class Cacophony:
    def __init__(self, sound_sequence_list=None):
        """
        Represents a collection of sound sequences.
        Args:
            sound_sequence_list: A list of SoundSequence objects.
        """
        if sound_sequence_list is None:
            sound_sequence_list = []
        if not all(isinstance(seq, SoundSequence)
                   for seq in sound_sequence_list):
            raise TypeError("All elements must be instances of SoundSequence.")
        self.sound_sequence_list = list(sound_sequence_list)

    def __repr__(self):
        return f"Cacophony(sound_sequence_list={self.sound_sequence_list})"

    def __eq__(self, other):
        if not isinstance(other, Cacophony):
            return NotImplemented
        return self.sound_sequence_list == other.sound_sequence_list

    def copy(self):
        return Cacophony([seq.copy() for seq in self.sound_sequence_list])

    def play(self):
        """
        Plays all sound sequences in the cacophony.
        """
        # TODO: Implement actual sound playback logic,
        # simply a collection of sequences

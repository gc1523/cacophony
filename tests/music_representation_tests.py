from src.music.representation import Sound, SoundSequence, Cacophony


def test_sound():
    sound1 = Sound(440.0, 1.0)
    sound2 = Sound(880.0, 1.0)

    assert sound1.pitch_hz == 440.0
    assert sound1.duration_s == 1.0
    assert repr(sound1) == "Sound(pitch_hz=440.0, duration_s=1.0)"
    assert sound1 == Sound(440.0, 1.0)
    assert sound1 != sound2

    print("Sound class tests passed.")


def test_sound_sequence():
    sound1 = Sound(440.0, 1.0)
    sound2 = Sound(880.0, 1.0)
    sequence = SoundSequence([sound1, sound2])

    assert len(sequence.sounds) == 2
    assert sequence.sounds[0] == sound1
    assert sequence.sounds[1] == sound2
    assert repr(sequence) == (
        f"SoundSequence(sounds=[{repr(sound1)}, {repr(sound2)}])"
    )
    assert sequence == SoundSequence([sound1, sound2])

    sequence_copy = sequence.copy()
    assert sequence_copy == sequence
    assert sequence_copy is not sequence
    print("SoundSequence class tests passed.")


def test_cacophony():
    sound1 = Sound(440.0, 1.0)
    sound2 = Sound(880.0, 1.0)
    sequence = SoundSequence([sound1, sound2])
    cacophony = Cacophony([sequence])

    assert cacophony.sound_sequence_list[0] == sequence
    assert len(cacophony.sound_sequence_list) == 1
    assert repr(cacophony) == (
        f"Cacophony(sound_sequence_list=[{repr(sequence)}])"
    )

    cacophony_copy = cacophony.copy()
    assert cacophony_copy == cacophony
    assert cacophony_copy is not cacophony

    print("Cacophony class tests passed.")


if __name__ == "__main__":
    test_sound()
    test_sound_sequence()
    test_cacophony()
    print("All tests passed.")

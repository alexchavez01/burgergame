def mystery(sound):
    new_sound = media.makeEmptySound(media.getLength(sound))
    source_index = 0
    
    for target_index in range(media.getLength(sound) - 1, -1, -1):
        value = media.getSampleValueAt(sound, source_index)
        media.setSampleValueAt(new_sound, target_index, value)
        source_index += 1

    return new_sound
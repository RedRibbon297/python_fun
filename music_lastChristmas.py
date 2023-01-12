import musicalbeeps

player=musicalbeeps.Player(volume = 0.3,mute_output = False)

full=1
half=0.5
quarter = 0.25
eighth=0.125

player.play_note("G5",quarter-eighth)
player.play_note("G5",quarter)
player.play_note("F5",quarter)
player.play_note("pause",eighth)

player.play_note("C5",eighth)
player.play_note("G5",eighth)
player.play_note("G5",eighth)
player.play_note("A5",eighth)
player.play_note("F5",quarter-eighth)
player.play_note("pause",quarter)

player.play_note("D5",eighth)
player.play_note("F5",eighth)
player.play_note("G5",eighth)
player.play_note("G5",eighth)
player.play_note("A5",quarter)
player.play_note("F5",quarter-eighth)
player.play_note("pause",quarter)

player.play_note("D5",eighth)
player.play_note("E5",eighth)
player.play_note("F5",eighth)
player.play_note("E5",eighth)
player.play_note("D5",quarter-eighth)
player.play_note("pause",quarter)

player.play_note("A5",quarter-eighth)
player.play_note("A5",quarter-eighth)
player.play_note("G5",quarter-eighth)
player.play_note("pause",quarter)
player.play_note("D5",eighth)
player.play_note("A5",eighth)
player.play_note("A5#",eighth)
player.play_note("A5",eighth)
player.play_note("G5",quarter-eighth)

player.play_note("pause",eighth)
player.play_note("F5",eighth)
player.play_note("E5",eighth)
player.play_note("F5",eighth)
player.play_note("F5",eighth)
player.play_note("E5",quarter)
player.play_note("F5",quarter)
player.play_note("E5",quarter)
player.play_note("C5",quarter-eighth)

player.play_note("pause",half)


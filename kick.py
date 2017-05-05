import Nsound as ns

sr = 44100.0

kick = ns.DrumKickBass(sr, 300, 20)

pb = ns.AudioPlayback(sr, 2, 16);

kick >> pb

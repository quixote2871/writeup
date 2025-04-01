from cipher import STREAM

cipher = "3cef03c64ac240c349971d9e4c951cc14ec4199f409249c21e964ac540c540944f901c934cc240934d96419f4b9e4d9f1cc41dc61dc34e9219c31bc11a914f9141c61ada"
cipher = bytes.fromhex(cipher)

for seed in range(0, 65536):
    Bob = STREAM(seed, 16)
    plane = Bob.decrypt(cipher)
    if b"DH{" in plane:
        print(plane.decode())

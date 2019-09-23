# ···· · −·−−   ·−−− ··− −·· ·
# H    E  Y  ' '  J   U   D  E

morse_code = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "x",
    "-.--": "Y", "--..": "Z", ".----": 1, "..---": 2, "...--": 3, "....-": 4,
    ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9, "-----": 0
}


def decodeMorse(morseCode):
    string = []
    for s in morseCode.split(" "):
        s.replace("   ", " ")
        if s in morse_code:
            string.append((morse_code[s]))
        else:
            string.append(s)
    return "".join(string)

    # string.append(morse_code[s])
    # return string


print(decodeMorse(".... . -.--   .--- ..- -.. ."))

import subprocess
from Translator_py_ly.translator import *
from Translator_py_ly.Automatic_bass.Bass import melody_bass_translate
from Decorators.Decorators import decorator_octava

def initialize_sheet():                     # Initial text of LilyPond coding, includes title, composer and instrument
    #title = input("Title: ")
    #composer = input("Composer: ")
    #instrument = input("Instrument: ")

    title = "asd"
    composer = "MUSE"
    instrument = "Piano"

    initial = ["\\version \"2.22.2\" ", 
               "\\header {", 
               "title = \"" + title + "\"",
               "composer = \"" + composer + "\"",
               "}",
               "\\score {\\new PianoStaff \\with { instrumentName = \"" +instrument+ "\" }"]

    with open("prueba.txt", "w") as f:
        f.write('\n'.join(initial))
    return

def start_sheet(reference, key_signature):          # Time signature, metronome and clef
    # time = input("Define a time signature (f.e. 3/4): ")
    time = "3/4"

    #figure, metronome = input("Define a metronome tempo (figure tempo): ").split()
    figure, metronome = "4", "120"

    #clef = input("Define a cleff (treble/alto/tenor/bass): ")
    clef = "treble"

    #anacruse = input("Do you want to start with an anacruse? (Yes/No): ")       # Anacruse start check
    anacruse = "No"
    if anacruse == "Yes":
        time_anacruse = input("Rythm anacruse (in quarter notes): ")
    else:
        time_anacruse = str(0)

    oct = int(reference[1]) - 3

    start = ["\n <<",
             "\\new Staff \\relative " + pitchly[reference[0]] + octaves[oct] + "{",
             "\\clef " + clef,
             "\\key " + key_ly(key_signature)[0] + " \\" + key_ly(key_signature)[1],
             "\\time " + time,
             "\\tempo " + figure + " = " + metronome,
             "\\partial " + time_anacruse + "\n"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(start))

    return

def start_translator(melody_py, reference, key_signature):          # Melody translation

    melody_ly = melody_translate(melody_py, reference, key_signature)
    melody_ly_decorated = decorator_octava(melody_ly)
    finish_staff = ["\n \\bar \"|.\"}"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(melody_ly_decorated))
        #f.write('\n'.join(melody_ly))
        f.write('\n'.join(finish_staff))

    return


def start_bass(melody_py, reference, key_signature):            # Bass translation and generation
    
    bass_ly = melody_bass_translate(melody_py, key_signature)

    start_bass = ["\n <<",
                  "\\new Staff \\relative " + "{",
                  "\\clef bass",
                  "\\key " + key_ly(key_signature)[0] + " \\" + key_ly(key_signature)[1],
                  "\\chordmode " + "{"]

    finish_bass = [ "\n" + "}" + "}",
                   ">>"]
                  
    with open("prueba.txt", "a") as f:
        f.write('\n'.join(start_bass))
        f.write('\n'.join(bass_ly))
        f.write('\n'.join(finish_bass))

    return 


def compile_PDF():

    finish = ["\n >>",
              "\\layout {}",
              "\\midi {}",
              "}"]

    with open("prueba.txt", "a") as f:
        f.write('\n'.join(finish))

    path_to_Lylipond = "D:\\Program Files\\LilyPond\\usr\\bin\\lilypond.exe"
    path_to_file = "D:\\Descargas\\Aeroespecial\\MUSE 1\\Matematicas\\Programacion\\Programas\\Music Maker\\prueba.txt"
    
    return subprocess.call([path_to_Lylipond,path_to_file])


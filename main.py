from initialize import *

reference = "G4"
key_signature = "CM"
melody = "G-G | A_ G C | B__ G-G | A_ G D5 | C__ G-G | G5_ E C | B A__ | F5-F E_ C | D C__^ | C__. ||"

#melody = "E_ E F G | G F E D | C C D E | E_. D- D__ ||"

#reference = "C5"
#key_signature = "AbM"
#coldplay = "R_ R- C- C_ C | C__. D- B-^ | B__ R- B_ A- | B_ B-A C_ E4- F-^ | F-C5 C-C C-C C_ | C__. D- B-^ | B__ R- B_ A- | B_ B B C- A-^ | A- F_. R__ | R__ R_ R- E5- | " \
#            + "F_ F F-E F- E-^ | E_ B- C_ D_. | E_ E E-C E- C-^ | C_ F4- G_ A_. ||"

initialize_sheet()
start_sheet(reference, key_signature)
start_translator(melody, reference, key_signature)
start_bass(melody, reference, key_signature)
compile_PDF()



import argparse


def convert_note_to_SHARP_view(note: str) -> str:
    '''
    Конвертирует ноту из вида NOTE_XSX в вид NOTE_XX_SHARP.

    Например:
        NOTE_DS4 -> NOTE_DS_SHARP
    '''
    if note == 'PAUSE':
        return note
    if note.find('SHARP') > 0:
        return note
    if note.find('S') >= 0:
        note = note.replace('S', '')
        note += '_SHARP'
    return note


def convert_note_from_SHARP_view(note: str) -> str:
    '''
    Конвертирует ноту из вида NOTE_XX_SHARP в вид NOTE_XSX.

    Например:
        NOTE_DS_SHARP -> NOTE_DS4
    '''
    if note.find('SHARP') >= 0:
        note = note.replace('_SHARP', '')
        note = note[:-1] + 'S' + note[-1:]
    return note


def convert_PAUSE_to_RESET(note: str) -> str:
    '''
    Конвертирует ноту PAUSE в RESET.
    '''
    if note == 'PAUSE':
        return 'RESET'
    return note


def convert_RESET_to_PAUSE(note: str) -> str:
    '''
    Конвертирует ноту RESET в PAUSE.
    '''
    if note == 'RESET':
        return 'PAUSE'
    return note


def convert_key_to_note(key: str) -> str:
    '''
    Конвертирует клавишу в соответствующую ноту.
    '''
    # Первая октава
    if key == 'q':
        return 'NOTE_C4'
    if key == '2':
        return 'NOTE_C4_SHARP'
    if key == 'w':
        return 'NOTE_D4'
    if key == '3':
        return 'NOTE_D4_SHARP'
    if key == 'e':
        return 'NOTE_E4'
    if key == 'r':
        return 'NOTE_F4'
    if key == '5':
        return 'NOTE_F4_SHARP'
    if key == 't':
        return 'NOTE_G4'
    if key == '6':
        return 'NOTE_G4_SHARP'
    if key == 'y':
        return 'NOTE_A4'
    if key == '7':
        return 'NOTE_A4_SHARP'
    if key == 'u':
        return 'NOTE_B4'
    # Вторая октава
    if key == 'i':
        return 'NOTE_C5'
    if key == '9':
        return 'NOTE_C5_SHARP'
    if key == 'o':
        return 'NOTE_D5'
    if key == '0':
        return 'NOTE_D5_SHARP'
    if key == 'p':
        return 'NOTE_E5'
    if key == '[':
        return 'NOTE_F5'
    if key == '=':
        return 'NOTE_F5_SHARP'
    if key == ']':
        return 'NOTE_G5'
    if key == "\\":
        return "NOTE_G5_SHARP"
    if key == '.':
        return "NOTE_A5"
    if key == ';':
        return "NOTE_A5_SHARP"
    if key == '/':
        return "NOTE_B5"
    # Малая октава
    if key == 'z':
        return 'NOTE_C3'
    if key == 's':
        return 'NOTE_C3_SHARP'
    if key == 'x':
        return 'NOTE_D3'
    if key == 'd':
        return 'NOTE_D3_SHARP'
    if key == 'c':
        return 'NOTE_E3'
    if key == 'v':
        return 'NOTE_F3'
    if key == 'g':
        return 'NOTE_F3_SHARP'
    if key == 'b':
        return 'NOTE_G3'
    if key == 'h':
        return 'NOTE_G3_SHARP'
    if key == 'n':
        return 'NOTE_A3'
    if key == 'j':
        return 'NOTE_A3_SHARP'
    if key == 'm':
        return 'NOTE_B3'

    return 'PAUSE'


def convert_note_to_key(key: str) -> str:
    '''
    Конвертирует ноту в соответствующую клавишу.
    '''
    # Первая октава
    if key == 'NOTE_C4':
        return 'q'
    if key == 'NOTE_C4_SHARP':
        return '2'
    if key == 'NOTE_D4':
        return 'w'
    if key == 'NOTE_D4_SHARP':
        return '3'
    if key == 'NOTE_E4':
        return 'e'
    if key == 'NOTE_F4':
        return 'r'
    if key == 'NOTE_F4_SHARP':
        return '5'
    if key == 'NOTE_G4':
        return 't'
    if key == 'NOTE_G4_SHARP':
        return '6'
    if key == 'NOTE_A4':
        return 'y'
    if key == 'NOTE_A4_SHARP':
        return '7'
    if key == 'NOTE_B4':
        return 'u'
    # Вторая октава
    if key == 'NOTE_C5':
        return 'i'
    if key == 'NOTE_C5_SHARP':
        return '9'
    if key == 'NOTE_D5':
        return 'o'
    if key == 'NOTE_D5_SHARP':
        return '0'
    if key == 'NOTE_E5':
        return 'p'
    if key == 'NOTE_F5':
        return '['
    if key == 'NOTE_F5_SHARP':
        return '='
    if key == 'NOTE_G5':
        return ']'
    if key == 'NOTE_G5_SHARP':
        return "\\"
    if key == 'NOTE_A5':
        return "."
    if key == 'NOTE_A5_SHARP':
        return ";"
    if key == 'NOTE_B5':
        return "/"
    # Малая октава
    if key == 'NOTE_C3':
        return 'z'
    if key == 'NOTE_C3_SHARP':
        return 's'
    if key == 'NOTE_D3':
        return 'x'
    if key == 'NOTE_D3_SHARP':
        return 'd'
    if key == 'NOTE_E3':
        return 'c'
    if key == 'NOTE_F3':
        return 'v'
    if key == 'NOTE_F3_SHARP':
        return 'g'
    if key == 'NOTE_G3':
        return 'b'
    if key == 'NOTE_G3_SHARP':
        return 'h'
    if key == 'NOTE_A3':
        return 'n'
    if key == 'NOTE_A3_SHARP':
        return 'j'
    if key == 'NOTE_B3':
        return 'm'

    return ' '


def convert_song_from_notes_to_keys(filepath: str, newfile: str) -> None:
    '''
    Принимает на вход путь к файлу с нотами музыки,
    конвертирует ноты в соответствии с их клавишами
    и выводит результат конвертации в файл, указанный вторым аргументом.
    '''
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        content = content.upper()
        content = content.replace('\n', ' ')
        content = content.replace('\r', ' ')
        content = content.replace('\t', ' ')
        content = content.replace(' ', '')
        notes = content.split(',')

    with open(newfile, "w", encoding="utf-8") as file:
        for note in notes:
            note = convert_note_to_SHARP_view(note)
            file.write(convert_note_to_key(note))


def convert_song_from_keys_to_notes(filepath: str, newfile: str) -> None:
    '''
    Принимает на вход путь к файлу с клавишами музыки,
    конвертирует клавиши в соответствии с нотами
    и выводит результат конвертации в файл, указанный вторым аргументом.
    '''
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        content = content.lower()
        content = content.replace('\n', ' ')
        content = content.replace('\r', ' ')
        content = content.replace('\t', ' ')

    notes = ""
    for _, key in enumerate(content):
        note = convert_key_to_note(key)
        notes += note + ', '
    notes = notes[:-2]

    with open(newfile, "w", encoding="utf-8") as file:
        file.write(notes)


def main():
    '''
    Интерфейс для работы с пользователем.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--from_keys_to_notes", action='store_true',
                        help="Конвертировать клавиши в ноты")
    parser.add_argument("--from_notes_to_keys", action='store_true',
                        help="Конвертировать ноты в клавиши")
    parser.add_argument('--filepath', type=str, required=True,
                        help="Путь к файлу с содержимым")
    parser.add_argument('--newfile', type=str, default='conv_melody.txt',
                        help="Путь к файлу, куда записывать\
                              конвертированное содержимое")
    args = parser.parse_args()

    if args.from_keys_to_notes and args.from_notes_to_keys:
        print("Выберите либо from_keys_to_notes, либо from_notes_to_key.")
    elif args.from_keys_to_notes:
        convert_song_from_keys_to_notes(args.filepath, args.newfile)
    elif args.from_notes_to_keys:
        convert_song_from_notes_to_keys(args.filepath, args.newfile)
    else:
        print("Выберите либо from_keys_to_notes, либо from_notes_to_keys.")


if __name__ == '__main__':
    main()

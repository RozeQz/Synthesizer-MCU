import os
import unittest

from melody_converter import convert_note_to_SHARP_view
from melody_converter import convert_note_from_SHARP_view
from melody_converter import convert_PAUSE_to_RESET
from melody_converter import convert_RESET_to_PAUSE
from melody_converter import convert_key_to_note
from melody_converter import convert_note_to_key
from melody_converter import convert_song_from_keys_to_notes
from melody_converter import convert_song_from_notes_to_keys


class TestNoteConverter(unittest.TestCase):
    '''
    Tests for note converter.
    '''
    def test_to_SHARP_view(self):
        '''
        Test convert_note_to_SHARP_view function.
        '''
        was = "NOTE_AS5"
        now = "NOTE_A5_SHARP"
        self.assertEqual(convert_note_to_SHARP_view(was), now)

        was = "NOTE_A5"
        now = "NOTE_A5"
        self.assertEqual(convert_note_to_SHARP_view(was), now)

        was = "PAUSE"
        now = "PAUSE"
        self.assertEqual(convert_note_to_SHARP_view(was), now)

        was = "NOTE_A5_SHARP"
        now = "NOTE_A5_SHARP"
        self.assertEqual(convert_note_to_SHARP_view(was), now)

    def test_from_SHARP_view(self):
        '''
        Test convert_note_from_SHARP_view function.
        '''
        was = "NOTE_A5_SHARP"
        now = "NOTE_AS5"
        self.assertEqual(convert_note_from_SHARP_view(was), now)

        was = "NOTE_A5"
        now = "NOTE_A5"
        self.assertEqual(convert_note_from_SHARP_view(was), now)

        was = "PAUSE"
        now = "PAUSE"
        self.assertEqual(convert_note_from_SHARP_view(was), now)

        was = "NOTE_AS5"
        now = "NOTE_AS5"
        self.assertEqual(convert_note_from_SHARP_view(was), now)

    def test_to_RESET(self):
        '''
        Test convert_PAUSE_to_RESET function.
        '''
        was = "PAUSE"
        now = "RESET"
        self.assertEqual(convert_PAUSE_to_RESET(was), now)

        was = "NOTE_AS5"
        now = "NOTE_AS5"
        self.assertEqual(convert_PAUSE_to_RESET(was), now)

    def test_to_PAUSE(self):
        '''
        Test convert_RESET_to_PAUSE function.
        '''
        was = "RESET"
        now = "PAUSE"
        self.assertEqual(convert_RESET_to_PAUSE(was), now)

        was = "NOTE_AS5"
        now = "NOTE_AS5"
        self.assertEqual(convert_RESET_to_PAUSE(was), now)

    def test_key_to_note(self):
        '''
        Test convert_key_to_note function.
        '''
        self.assertEqual(convert_key_to_note('q'), 'NOTE_C4')
        self.assertEqual(convert_key_to_note('2'), 'NOTE_C4_SHARP')
        self.assertEqual(convert_key_to_note('w'), 'NOTE_D4')
        self.assertEqual(convert_key_to_note('3'), 'NOTE_D4_SHARP')
        self.assertEqual(convert_key_to_note('e'), 'NOTE_E4')
        self.assertEqual(convert_key_to_note('r'), 'NOTE_F4')
        self.assertEqual(convert_key_to_note('5'), 'NOTE_F4_SHARP')
        self.assertEqual(convert_key_to_note('t'), 'NOTE_G4')
        self.assertEqual(convert_key_to_note('6'), 'NOTE_G4_SHARP')
        self.assertEqual(convert_key_to_note('y'), 'NOTE_A4')
        self.assertEqual(convert_key_to_note('7'), 'NOTE_A4_SHARP')
        self.assertEqual(convert_key_to_note('u'), 'NOTE_B4')
        self.assertEqual(convert_key_to_note('i'), 'NOTE_C5')
        self.assertEqual(convert_key_to_note('else'), 'PAUSE')

    def test_note_to_key(self):
        '''
        Test convert_note_to_key function.
        '''
        self.assertEqual(convert_note_to_key('NOTE_C4'), 'q')
        self.assertEqual(convert_note_to_key('NOTE_C4_SHARP'), '2')
        self.assertEqual(convert_note_to_key('NOTE_D4'), 'w')
        self.assertEqual(convert_note_to_key('NOTE_D4_SHARP'), '3')
        self.assertEqual(convert_note_to_key('NOTE_E4'), 'e')
        self.assertEqual(convert_note_to_key('NOTE_F4'), 'r')
        self.assertEqual(convert_note_to_key('NOTE_F4_SHARP'), '5')
        self.assertEqual(convert_note_to_key('NOTE_G4'), 't')
        self.assertEqual(convert_note_to_key('NOTE_G4_SHARP'), '6')
        self.assertEqual(convert_note_to_key('NOTE_A4'), 'y')
        self.assertEqual(convert_note_to_key('NOTE_A4_SHARP'), '7')
        self.assertEqual(convert_note_to_key('NOTE_B4'), 'u')
        self.assertEqual(convert_note_to_key('NOTE_C5'), 'i')
        self.assertEqual(convert_note_to_key('PAUSE'), ' ')


class TestMelodyConverter(unittest.TestCase):
    '''
    Tests for melody converter.
    '''
    def test_song_from_keys_to_notes(self):
        '''
        Test convert_song_from_keys_to_notes function.
        '''
        testfile_1 = 'test_file_1.txt'

        with open(testfile_1, "w", encoding="utf-8") as file:
            file.write("q2w3er5t6y7ui9o0p[=]\\")

        testfile_2 = 'test_file_2.txt'

        convert_song_from_keys_to_notes(testfile_1, testfile_2)

        os.remove(testfile_1)

        with open(testfile_2, "r", encoding="utf-8") as file:
            content = file.read()

        result = "NOTE_C4, NOTE_C4_SHARP, NOTE_D4, NOTE_D4_SHARP, NOTE_E4, " +\
                 "NOTE_F4, NOTE_F4_SHARP, NOTE_G4, NOTE_G4_SHARP, NOTE_A4, " +\
                 "NOTE_A4_SHARP, NOTE_B4, NOTE_C5, NOTE_C5_SHARP, NOTE_D5, " +\
                 "NOTE_D5_SHARP, NOTE_E5, NOTE_F5, NOTE_F5_SHARP, NOTE_G5, " +\
                 "NOTE_G5_SHARP"

        self.assertEqual(content, result)

        os.remove(testfile_2)

    def test_song_from_notes_to_keys(self):
        '''
        Test convert_song_from_notes_to_keys function.
        '''
        testfile_1 = 'test_file_1.txt'

        melody = "NOTE_C4, NOTE_C4_SHARP, NOTE_D4, NOTE_D4_SHARP, NOTE_E4, " +\
                 "NOTE_F4, NOTE_F4_SHARP, NOTE_G4, NOTE_G4_SHARP, NOTE_A4, " +\
                 "NOTE_A4_SHARP, NOTE_B4, NOTE_C5, NOTE_C5_SHARP, NOTE_D5, " +\
                 "NOTE_D5_SHARP, NOTE_E5, NOTE_F5, NOTE_F5_SHARP, NOTE_G5, " +\
                 "NOTE_G5_SHARP"

        with open(testfile_1, "w", encoding="utf-8") as file:
            file.write(melody)

        testfile_2 = 'test_file_2.txt'

        convert_song_from_notes_to_keys(testfile_1, testfile_2)

        os.remove(testfile_1)

        with open(testfile_2, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertEqual(content, "q2w3er5t6y7ui9o0p[=]\\")

        os.remove(testfile_2)


if __name__ == "__main__":
    unittest.main()

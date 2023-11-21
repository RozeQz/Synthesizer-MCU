# Synthesizer-MCU

An 8-bit synthesizer using **atmega8515** with 4 operating modes.

1. **Piano mode**:
   Play like a simple piano using the buttons.

2. **Music mode**:
   Listen to already downloaded melodies.

3. **Load mode**:
   You can download a melody via UART using a terminal (for example [PUTTY](https://www.putty.org/)).\
   The melody is loaded using the entered keys. If you have notes for a melody, you can convert it to the right keys using [`melody_converter.py`](./melody_converter.py).

4. **PC mode**:
   You can play the piano, using your PC keybord. Just connect via UART using a terminal (for example [PUTTY](https://www.putty.org/)).

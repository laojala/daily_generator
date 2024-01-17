''' 
Daily Generator

Prints a random order of the ATTENDEES and QUESTIONS for daily.

If run in Mac OS, copies the output to the clipboard.
'''

import sys
import platform
import subprocess
from random import shuffle
from io import StringIO

# Modidy this list for attendees
ATTENDEES =  ['Blaze',
              'Smith'
	          'Sola',
              'Star']

# Modify this list for questions
QUESTIONS = ['How are you doing?',
             'Wins',
             'Blockers',
             'Focus',
             'Help needed']


def print_numbered_list(printing:list) -> None:
    '''Prints numbered list. List is given in arguments.'''
    for number, item in enumerate(printing,1):
        print(f'{number}. {item}')

def print_daily_questions() -> None:
    '''Prints static list QUESTIONS'''
    print('\n\nDAILY QUESTIONS:')
    print_numbered_list(QUESTIONS)

def print_random_attendees_order() -> None:
    '''Prints random order from a static list ATTENDEES'''
    print('\nDAILY ORDER:')
    to_random = ATTENDEES[:]
    shuffle(to_random)
    print_numbered_list(to_random)

def main() -> None:
    '''Prints daily questions and attendees, and if on macOS, copies them to the clipboard.'''
    # Redirect stdout to a buffer
    buffer = StringIO()
    sys.stdout = buffer

    # Print questions and attendees
    print_daily_questions()
    print_random_attendees_order()

    # Reset stdout to its normal behavior
    sys.stdout = sys.__stdout__

    # Get the buffered output
    output = buffer.getvalue()

    # If on macOS, copy the output to the clipboard
    if platform.system() == "Darwin":
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(output.encode())

    # Print the output to the console as well
    print(output)

if __name__ == "__main__":
    sys.exit(main())

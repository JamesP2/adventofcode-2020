import argparse

parser = argparse.ArgumentParser(description="Rambunctious Recitation")
parser.add_argument("file", metavar="INPUT_FILE", type=str, help="Input filename")
parser.add_argument("--turn", "-t", type=int, default=2020, help="Turn number to stop after")
parser.add_argument(
    "--verbose", "-v", action="store_true", default=False, help="Verbose output"
)

args = parser.parse_args()


def vprint(*x):
    if args.verbose:
        if len(x) == 1:
            print(x[0])
        else:
            print(x)


lines = [line.rstrip("\n") for line in open(args.file)]
numbers = [int(number) for number in lines[0].split(",")]

# Key: Number, Value: Times spoken
times_spoken = {}

# Key: Number, Value: Turn number when last spoken, and the time before that
last_turn = {}
turn_before_last = {}

# The last number spoken
last_spoken = None

current_turn = 1


# Speak the number and update the last turn (and the turn before it!)
def speak(number):
    global times_spoken, last_spoken
    times_spoken[number] = 1 if number not in times_spoken else times_spoken[number] + 1

    if number in last_turn:
        turn_before_last[number] = last_turn[number]
    last_turn[number] = current_turn
    last_spoken = number

    vprint("Turn {}, Spoken {}".format(current_turn, number))


for number in numbers:
    speak(number)
    current_turn += 1

vprint("After read in: Last {}, turns: {}".format(last_spoken, times_spoken))

while current_turn <= args.turn:
    # Consider the most recently spoken number
    # If that was the first time the number has been spoken, speak 0
    if times_spoken[last_spoken] == 1:
        speak(0)
    # Otherwise the number had been spoken before, the current player announces
    # how many turns apart the number is from when it was previously spoken
    else:
        speak(last_turn[last_spoken] - turn_before_last[last_spoken])
    
    current_turn += 1

print(last_spoken)
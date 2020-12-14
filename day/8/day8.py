import argparse
import re

parser = argparse.ArgumentParser(description="Handheld Halting")
parser.add_argument("file", metavar="INPUT_FILE", type=str, help="Input filename")
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


# Array of [# Executions, Instruction Name, Argument]
program = []
current_index = 0
accumulator_value = 0


def run_current_instruction():
    global program, current_index, accumulator_value

    if current_index >= len(program):
        vprint("Program terminating normally")
        return

    current_instruction = program[current_index]
    vprint(
        "Acc {}, Current Instruction: {}".format(accumulator_value, current_instruction)
    )

    # If this instruction has been ran before then return
    if current_instruction[0] > 0:
        vprint("Second execution attempt on this instruction! Stopping")
        return

    # We're running this instruction now so increment the # of Executions
    current_instruction[0] += 1

    # Switch depending on instruction
    if current_instruction[1] == "nop":
        pass
    elif current_instruction[1] == "acc":
        accumulator_value += current_instruction[2]
    elif current_instruction[1] == "jmp":
        current_index += current_instruction[2]
        return run_current_instruction()

    # Increment current index to execute next instruction
    current_index += 1
    run_current_instruction()


with open(args.file) as file:
    for line in file:
        line = line.replace("\n", "")
        instruction = [0] + line.split(" ")
        instruction[2] = int(instruction[2])
        program.append(instruction)

vprint(program)
run_current_instruction()
print(accumulator_value)

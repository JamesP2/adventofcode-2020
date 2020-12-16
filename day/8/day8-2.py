import argparse

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


# Array of [# Executions, Instruction Name, Argument, Tried Fix]
program = []
current_index = 0
accumulator_value = 0


def run_current_instruction():
    global program, current_index, accumulator_value

    if current_index >= len(program):
        vprint("Program terminating normally")
        return True

    current_instruction = program[current_index]
    vprint(
        "Index {}, Acc {}, Current Instruction: {}".format(current_index, accumulator_value, current_instruction)
    )

    # If this instruction has been ran before then return
    if current_instruction[0] > 0:
        vprint("Second execution attempt on this instruction! Stopping")
        return False

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
    return run_current_instruction()

def try_run():
    global program, current_index, accumulator_value

    current_try_index = 0
    swapped_index = None
    old_try_instruction = None

    while not run_current_instruction():
        # If this is a run AFTER we've tried changing something, change it back
        if old_try_instruction != None:
            program[swapped_index][1] = old_try_instruction

        for index in range(current_try_index, len(program) - 1):
            # Skip this line if we've ALREADY tried to fix it
            if program[index][3]:
                continue

            # We're trying to fix this line so remember that
            program[index][3] = True

            # Reset the current index and acc value for the next run
            current_index = 0
            accumulator_value = 0

            # Reset # execution counter for each line
            for line in program:
                line[0] = 0

            # If its a nop try a jump
            if program[index][1] == "nop" and program[index][2] != 0:
                old_try_instruction = "nop"
                program[index][1] = "jmp"
                current_try_index = index
                swapped_index = index
                break

            # Or if its a jump try a nop
            elif program[index][1] == "jmp":
                old_try_instruction = "jmp"
                program[index][1] = "nop"
                current_try_index = index
                swapped_index = index
                break




with open(args.file) as file:
    for line in file:
        line = line.replace("\n", "")
        instruction = [0] + line.split(" ") + [False]
        instruction[2] = int(instruction[2])
        program.append(instruction)

try_run()
print(accumulator_value)

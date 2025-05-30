import argparse
import hashlib
import re
import sys

from stack import Stack


def main(argv: list[str]) -> None:
    filename = ""
    about = "Finds unique Java stack traces in a log file and counts their occurrences."
    debug = False

    # if no arguments
    if not len(argv) > 1:
        sys.exit(2)

    # init parser
    parser = argparse.ArgumentParser(description=about)
    parser.add_argument("-f", "--file", help="log file")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="enable debug output"
    )
    args = parser.parse_args()

    if args.file:
        filename = args.file
        debug = args.debug

    file_stacks: list[str] = parse_file(filename, debug)
    stack_objects = process_stacks(file_stacks)
    print_results(get_sorted_stacks(stack_objects))


def parse_file(filename: str, debug: bool) -> list[str]:
    patterns = [
        # stack trace
        re.compile(
            r"^Stack trace:.*(?:(?:\n|\r\n?)+^\s*[at|Caused by]+.*)+", re.MULTILINE
        ),
        # datastax driver stack trace
        re.compile(
            r"^.*?com\.datastax\.driver\.core\.exceptions.*(?:(?:\n|\r\n?)+^\s*[at|Caused by]+.*)+",
            re.MULTILINE,
        ),
        # Exception stack trace
        re.compile(
            r"^.*?Exception.*(?:(?:\n|\r\n?)+^\s*[at|Caused by]+.*)+", re.MULTILINE
        ),
    ]

    try:
        with open(filename, "r") as open_file:
            content = open_file.read()  # Read file content once
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    # Collect all unique matches from all patterns
    stacks: list[str] = []
    for pattern in patterns:
        print(f"Searching for pattern: {pattern.pattern}") if debug else None
        matches = [match.group(0) for match in pattern.finditer(content)]
        print(
            f"Found {len(matches)} stack traces for pattern in {filename}"
        ) if debug else None
        stacks.extend(matches)  # Add matches to the list
    return stacks


def process_stacks(stacks: list[str]) -> list[Stack]:
    stack_objects: list[Stack] = []

    for stack in stacks:
        encoded_stack = stack.encode()
        hash_stack = hashlib.sha256(encoded_stack).hexdigest()
        match = False

        if len(stack_objects) > 0:
            # Update existing stack counts if the hash matches
            for stack_object in stack_objects:
                if hash_stack == stack_object.get_stack_hash():
                    match = True
                    stack_object.increment_count()

            # Create a new stack if it did not aleady exist
            if match is False:
                stack_object = Stack(hash_stack, stack)
                stack_objects.append(stack_object)
        # Run on first stack
        else:
            stack_object = Stack(hash_stack, stack)
            stack_objects.append(stack_object)

    return stack_objects


# Function to sort stack objects by count in descending order
def get_sorted_stacks(stack_objects: list[Stack]) -> list[Stack]:
    # Sort list by Stack.get_count descending
    return sorted(stack_objects, key=lambda x: x.get_count(), reverse=True)


def print_results(stack_objects: list[Stack]) -> None:
    for obj in stack_objects:
        print("======================================================")
        print("Count: {}".format(obj.get_count()))
        print("Stack:\n{}".format(obj.get_stack()))


if __name__ == "__main__":
    main(sys.argv)

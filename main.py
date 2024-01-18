import argparse
import hashlib
import re
import sys

from stack import Stack


def main(argv):
    filename = ""
    about = ""

    # if no arguments
    if not len(argv) > 1:
        sys.exit(2)

    # init parser
    parser = argparse.ArgumentParser(description=about)
    parser.add_argument("-f", "--file", help="log file")
    args = parser.parse_args()

    if args.file:
        filename = args.file

    file_stacks = parse_file(filename)
    stack_objects = process_stacks(file_stacks)
    print_results(stack_objects)


def parse_file(filename):
    regex_stack_trace = re.compile(r"^Stack trace:.*(?:(?:\n|\r\n?)+^\s*[at|Caused by]+.*)+", re.MULTILINE)
    regex_datastax_stack = re.compile(r"^.*?com\.datastax\.driver\.core\.exceptions.*(?:(?:\n|\r\n?)+^\s*[at|Caused by]+.*)+", re.MULTILINE)
    regex_full_stack = re.compile(r"^.*?Exception.*(?:(?:\n|\r\n?)+^\s*[at|Caused by]+.*)+", re.MULTILINE)
    open_file = open(filename, "r")
    stacks = [match.group(0) for match in regex_stack_trace.finditer(open_file.read())]
    return stacks


def process_stacks(stacks):
    stack_objects = []

    for stack in stacks:
        encoded_stack = stack.encode()
        hash_stack = hashlib.sha256(encoded_stack).hexdigest()
        match = False

        if len(stack_objects) > 0:
            for stack_object in stack_objects:
                if hash_stack == stack_object.get_stack_hash():
                    match = True
                    stack_object.increment_count()

            if match is False:
                stack_object = Stack(hash_stack, stack)
                stack_objects.append(stack_object)
        else:
            stack_object = Stack(hash_stack, stack)
            stack_objects.append(stack_object)

    return stack_objects


def print_results(stack_objects):
    for obj in stack_objects:
        print("======================================================")
        print("Count: {}".format(obj.get_count()))
        print("Stack:\n{}".format(obj.get_stack()))


if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

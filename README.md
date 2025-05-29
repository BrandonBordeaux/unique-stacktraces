# Unique Stacks Project

Finds Java stack traces in logs and reports on unique stacks and the number of them found.

Usage:

```bash
python main.py -h
usage: main.py [-h] [-f FILE]

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  log file
```

NOTE: There are multiple regex in `parse_file` where only one is used. In the current state, the code must be modified to use a different regex.

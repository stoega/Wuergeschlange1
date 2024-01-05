import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--program', type=str, required=True, help="Name of program to be executed.")
parser.add_argument('-a', '--args', type=str, nargs='+', default=[], help="Arguments to be passed to the program.")
parser.add_argument('-t', '--timeout', type=float, default=60, help="Timeout in seconds for the execution of the program.")

parser_args = parser.parse_args()

program = parser_args.program
args = parser_args.args
timeout = parser_args.timeout
print(args)


try:
    if args:
        print(f"Running program '{program}' with arguments {args} with a {timeout}s timeout")
    else:
        print(f"Running program '{program}' without any arguments with a {timeout}s timeout")
        
    result = subprocess.run([program] + args, text=True, capture_output=True, timeout=timeout)
    print(f"The '{program}' finished with exit code {result.returncode}")

    if result.stderr.strip():
        print(f"The '{program}' produced the following error output:")
        print(result.stderr)

    if result.stdout.strip():
        print(f"The '{program}' produced the following standard output:")
        print(result.stdout)

except FileNotFoundError:
    print(f"The specified program '{program}' could not be found")

except subprocess.TimeoutExpired:
    print("The program execution timed out")
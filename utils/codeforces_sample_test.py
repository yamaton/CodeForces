#!/usr/bin/env python3
"""
CodeForces Sample Test

@author yamaton
@date 2015-08-31
      2015-09-27
"""
from extract_samples import extract_samples, is_proper
import subprocess
import sys
import os
import json
import re


class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def bold(s):
    return colors.BOLD + s + colors.ENDC


def green(s):
    return colors.OKGREEN + s + colors.ENDC


def red(s):
    return colors.FAIL + s + colors.ENDC


def extract_id(filename):
    """
    Extract Codeforces problem ID in filename string.

    Args:
        s (str): filename
    Returns:
        str or None

    >>> extract_id('525A.cpp')
    '525A'

    >>> extract_id('33C-foobar.py')
    '33C'

    >>> extract_id('1A what.py')
    '1A'

    >>> extract_id('123_baz.py')
    None

    If filename contains directories like '/foo/bar/32A-abc.py',
    basename ('32A-abc.py') is taken first.
    """
    base = os.path.basename(filename)
    candidate = re.split("[-_\.\s]", base)[0]
    return candidate if is_proper(candidate) else None


def id_and_filename_from_argv():
    """
    Obtain problem ID and filename from the argment variables.
    argv[2] is neglected if the ID is found in filename (argv[1]).

    Returns:
        (str, str).   problem ID and filename
    """
    if len(sys.argv) < 2:
        sys.exit('Usage: python {} <file-name>'.format(sys.argv[0]))
    filename = sys.argv[1]
    problem_id = extract_id(filename)

    try:
        problem_id = problem_id or sys.argv[2]
    except IndexError:
        sys.exit('Usage: python {} <file-name> <problem-id>'.format(sys.argv[0]))

    if not os.path.exists(sys.argv[1]):
        sys.exit('ERROR: python script {} was not found!'.format(filename))

    return (problem_id, filename)


def run_python(filename, inp):
    """
    Run Python code against given inp

    Args:
        filename  (str): filename of python code
        inp       [str]: list of sample input
    """
    p = subprocess.Popen([sys.executable, filename],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    out, _ = p.communicate(inp.encode())    # encode: string -> bytestring
    out = out.decode().strip()              # decode: bytestring -> string
    return out


def compare(inputs, outputs, expected):
    """
    inputs   [str]
    outputs  [str]
    expected [str]
    """

    assert len(inputs) == len(outputs) == len(expected)

    for i, (inp, out, exp) in enumerate(zip(inputs, outputs, expected)):
        print('Case {}: '.format(i+1), end='')
        out = out.strip()
        exp = exp.strip()
        if exp == out:
            print(green('ok'))
        else:
            print(red('==================Incorrect!=================='))
            print('input:', inp)
            print('output:  ', out)
            print('expected:', exp)


def main():
    """
    1. Get filename of Python code and problem ID
    2. Go to the CodeForces website and get input and output samples in JSON
    3. Get input/ouput string from JSON
    4. Run Python code with the sample input, and compare its outcome with the
    sample output.
    """
    problem_id, filename = id_and_filename_from_argv()
    print('\nTesting samples in CodeForces {}: {}'.format(
            bold(problem_id), bold(filename)))

    json_str = extract_samples(problem_id, is_contest=True)
    json_dict = json.loads(json_str)
    assert problem_id == json_dict['id']

    inputs = ['\n'.join(d['input']) for d in json_dict['sample_io']]
    expected = ['\n'.join(d['output']) for d in json_dict['sample_io']]
    outputs = [run_python(filename, inp) for inp in inputs]
    compare(inputs, outputs, expected)


if __name__ == '__main__':
    main()

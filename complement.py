#!/usr/bin/env python
""" script to calculate complement of a DNA sequence """
import argparse


def parse_command_line_args(test_override=None):
    """Parse options from the command line, unless override
    list test_override is specified (this is for testing).

    Sets up the command line options using argparse including
    the help message.

    returns a tuple containing:
      (sequence (str),
       reverse (boolean)
      )
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('SEQUENCE')
    parser.add_argument('-reverse', action='store_true')
    if test_override is not None:
        args = parser.parse_args(test_override)
    else:
        args = parser.parse_args()
    return args.SEQUENCE, args.reverse


def complement(seq):
    """ Returns the complement of the input DNA sequence """
    complement_mapping = str.maketrans('ATGC', 'TACG')
    return seq.translate(complement_mapping)

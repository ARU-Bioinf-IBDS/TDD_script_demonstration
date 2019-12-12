""" script to calculate complement of a DNA sequence """


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


def complement(seq):
    """ Returns the complement of the input DNA sequence """
    complement_mapping = str.maketrans('ATGC', 'TACG')
    return seq.translate(complement_mapping)

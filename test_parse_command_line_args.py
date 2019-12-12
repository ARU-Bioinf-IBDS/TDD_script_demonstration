""" unit tests for parse_command_line_args
to handle command line stuff
"""
from complement import parse_command_line_args
import pytest


def test_supply_a_sequence():
    assert parse_command_line_args(test_override=['TEST']) == \
           ('TEST', False)


def test_supply_sequence_and_minus_filter():
    args = ['-reverse', 'TEST']
    assert parse_command_line_args(test_override=args) == ('TEST', True)


def test_help_message():
    # TODO osmart 12 Dec 2019
    pass


def test_with_empty_args_raises_error():
    """ User passes no arguments
    This is invalid as they have to specify at least one input file/seq
    """
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=[])


def test_with_invalid_option_raises_error():
    """ User passes a string and -invalid option.
    This must raise SystemExit.
    """
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=['A', '-invalid'])


def test_supply_two_sequences_raises_error():
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=['1', '2'])

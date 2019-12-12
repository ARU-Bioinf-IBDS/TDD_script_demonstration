from complement import main
import pytest


def test_a(capsys):
    main(test_override=['A'])
    capture_output = capsys.readouterr().out
    assert capture_output == 'T\n'


def test_atgc(capsys):
    main(test_override=['ATGC']) 
    capture_output = capsys.readouterr().out
    assert capture_output == 'TACG\n'


def test_given_example(capsys):
    main(test_override=['CAATTTGGGG']) 
    capture_output = capsys.readouterr().out
    assert capture_output == 'GTTAAACCCC\n'


# TODO test -reverse option

""" script to calculate complement of a DNA sequence """


def complement(seq):
    """ Returns the complement of the input DNA sequence """
    complement_mapping = str.maketrans('ATGC', 'TACG')
    return seq.translate(complement_mapping)

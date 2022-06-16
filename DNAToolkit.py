from ast import FormattedValue
import collections

Nucleotideos = [ 'A', 'C', 'G', 'T' ]

# Validar sequencia de caracteres, para verificar se é um trecho do DNA
def validateSequence(sequence_dna: str):
    sequence = sequence_dna.upper()

    for seq in sequence:
        if seq not in Nucleotideos:
            return False
    return True


# Calcular a frequencia dos nucleotidos, do trecho de DNA
def calcularFrequenciaNucleotideos(sequence_dna: str):

    isValid = validateSequence(sequence_dna)

    if isValid is False:
        raise ValueError('Sequencia invalida!')

    return dict(collections.Counter(sequence_dna))

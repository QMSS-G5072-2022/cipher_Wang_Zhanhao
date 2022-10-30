def cipher(text, shift, encrypt=True):
    """
    Encrypt or decrypt the letters by replacing each letter by a letter some fixed number of positions down the alphabet

    Parameters
    ----------
    text: the text contains letters that you want to encrypt or decrypt
        a string
    shift: some fixed number of positions
        an integer

    Returns
    -------
    a string
    The new text that you encrypt or decrypt

    Examples
    --------
    >>>import cipher_zw2744
    >>>text = 'abc'
    >>>shift = 2
    >>>cipher_zw2744.cipher(text, shift, encrpty = True)
    ['cde']
    >>>cipher_zw2744.cipher(text, shift, decrpty = False)
    ['YZa']
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

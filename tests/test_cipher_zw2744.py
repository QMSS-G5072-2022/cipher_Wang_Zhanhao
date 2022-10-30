from cipher_zw2744 import cipher_zw2744

def test_cipher_una_symbols():
    text = 'a//b'
    shift = 2
    expected = 'c//d'
    actual = cipher_zw2744.cipher(text,shift)
    assert expected==actual


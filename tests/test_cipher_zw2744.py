from cipher_zw2744 import cipher_zw2744
@pytest.mark.parametrize("actual, shift, expected", [
    ('a', 2, 'c'),
    ('abc',2,'cde'),
    ('ABC',2,'CDE'),
    ('a b c',2,'c d e')
])
def test_cipher_looping_(actual, shift, expected):
    result = cipher_zw2744.cipher(actual, shift)
    assert result == expected

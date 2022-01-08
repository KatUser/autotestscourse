full_string = 'fulltext'
substring = 'some_value'

def test_substring(full_string, substring):
    assert (substring in full_string), f"expected \'{substring}\' to be substring of \'{full_string}\'"

print(f"expected \'{substring}\' to be in \'{full_string}\'")

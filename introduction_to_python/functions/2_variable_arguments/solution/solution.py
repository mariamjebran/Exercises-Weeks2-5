def concat_args(*args):
    final_string = ''
    for string in args:
        final_string += string
    return final_string

concat_args('hello', 'there', 'mariam')
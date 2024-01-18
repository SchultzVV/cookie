# code for preprocessing the project data
# you can costumize this code as you want
# and write your own documentation/comments
# this docstring is just an example

### EXAMPLE CODE ###


def preprocessing(x: int = None) -> int:
    """
    Preprocesses the data.

    :param df: the dataframe to preprocess
    :return: the preprocessed dataframe
    """
    if x is None:
        x = 0
    x = x + 1
    return x

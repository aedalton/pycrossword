import pytest
from crossword import grid_fill


@pytest.fixture
def wordlist_fixture():
    wordlist = ["BUBBLE", "ELEPHANTS", "BEEZOR", "BAFFLE"]
    return wordlist


@pytest.fixture
def crossgen_fixture(wordlist_fixture):
    gfg = grid_fill.CrosswordGenerator(wordlist_fixture)
    return gfg


@pytest.fixture
def grid_fixture():
    # input of grid of size n1 x n1
    matrix = []
    matrix.append(list("*#********"))
    matrix.append(list("*#********"))
    matrix.append(list("*#****#***"))
    matrix.append(list("*##***##**"))
    matrix.append(list("*#****#***"))
    matrix.append(list("*#****#***"))
    matrix.append(list("*#****#***"))
    matrix.append(list("*#*######*"))
    matrix.append(list("*#********"))
    matrix.append(list("***#######"))
    return matrix


def test_grid_fill(crossgen_fixture, grid_fixture):
    crossgen_fixture.pretty_print_grid(grid_fixture)
    crossgen_fixture.solve_puzzle(grid_fixture, 0, 10);
    assert crossgen_fixture

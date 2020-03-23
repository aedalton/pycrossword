class CrosswordGenerator:
    invalid_marker = "@"
    blank_marker = "#"

    def __init__(self, wordlist):
        self.possible_ways = 0
        self.wordlist = wordlist

    def pretty_print_grid(self, grid):
        print()
        for row in grid:
            print(row)

    def check_horizontal(self, pos_x, pos_y, grid, current_word):
        """ TO BE DRY'ED """
        current_word_len = len(current_word) - 1
        for idx in range(current_word_len):
            if grid[pos_x][pos_y + idx] == self.blank_marker or \
               grid[pos_x][pos_y + idx] == current_word[idx]:
                grid[pos_x][pos_y + idx] = current_word[idx]
            else:
                grid[0][0] = self.invalid_marker
                return grid
        return grid

    def check_vertical(self, pos_x, pos_y, grid, current_word):
        current_word_len = len(current_word) - 1

        for idx in range(current_word_len):
            if grid[pos_x + idx][pos_y] == self.blank_marker or \
               grid[pos_x + idx][pos_y] == current_word[idx]:
                grid[pos_x + idx][pos_y] = current_word[idx]
            else:
                grid[0][0] = self.invalid_marker
                return grid

        return grid

    def solve_puzzle(self, grid, idx_i, n):
        if idx_i < len(self.wordlist):
            current_word = self.wordlist[idx_i]
            max_len = n - len(current_word)
            for idx_j in range(n -1):
                for idx_k in (idx_j, max_len):
                    tmp = self.check_vertical(idx_j, idx_k, grid, current_word)

                    if tmp[0][0] != self.invalid_marker:
                        self.solve_puzzle(tmp, idx_i + 1, n)
            for idx_j in range(n):
                for idx_k in range(idx_j, max_len):
                    tmp = self.check_horizontal(idx_j, idx_k, grid, current_word)
                    if tmp != self.invalid_marker:
                        self.solve_puzzle(tmp, idx_i, n)
        else:
            print(f"ways to solve: {self.possible_ways + 1}")
            self.pretty_print_grid(grid, n)
            self.possible_ways += 1

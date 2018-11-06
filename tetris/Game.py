import random
import utilities.cube


class TetrisGame:

    # board[x][y][z] means board[front to back][bottom to top][right to left]
    # see https://docs.google.com/document/d/1-LGIlPrV1G8JojxiikUIvX7hAX0S8LZAeEbLJSfVa48
    # for an explanation.
    board = []

    # The score the player has (= #rows eliminated)
    score = 0

    # all possible blocks that can fall from the sky
    # [a, b, c] = [z, y, x] positions
    possible_blocks = [
        [[1, 3, 1], [1, 3, 2]], # simple 2-segment block
        [[1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 4, 2]], # upside-down T-shape
        [[1, 3, 1]], # a dot.
        [[1, 3, 1], [1, 3, 2], [1, 4, 1]] # an L - shape
    ]

    # current block that the user is going to place
    current_block = []

    # Field is all the blocks that are already placed.
    field = []

    # game_over keeps track of when the game is over.
    game_over = False

    # [[=========]]
    # [[FUNCTIONS]]
    # [[=========]]

    def __init__(self):
        self.board = self.setup_board()
        self.current_block = self.possible_blocks[random.randint(0, (len(self.possible_blocks) - 1))]

    # initializes the board so all values are False (meaning all LEDs should be off)
    def setup_board(self):
        return utilities.cube.get_cube(offset=32)

    # clears the board: sets every square as not active.
    def clear_board(self,):
        for plane in self.board:
            for row in plane:
                for val in row:
                    val[1] = False

    # move the current block based on direction input
    def move_current(self, direction):
        updated = self.current_block.copy()
        valid_move = True

        if direction == "back":
            # increment every z-index if possible
            for i, segment in enumerate(self.current_block):
                if segment[0] == 3:
                    # don't go out of bounds, end function
                    valid_move = False
                    break
                else:
                    z, y, x = segment[0], segment[1], segment[2]
                    updated[i] = [z + 1, y, x]
        elif direction == "front":
            for i, segment in enumerate(self.current_block):
                if segment[0] == 0:
                    # don't go out of bounds, end function
                    valid_move = False
                    break
                else:
                    z, y, x = segment[0], segment[1], segment[2]
                    updated[i] = [z - 1, y, x]
        elif direction == "left":
            for i, segment in enumerate(self.current_block):
                if segment[2] == 3:
                    # don't go out of bounds, end function
                    valid_move = False
                    break
                else:
                    z, y, x = segment[0], segment[1], segment[2]
                    updated[i] = [z, y, x + 1]
        elif direction == "right":
            for i, segment in enumerate(self.current_block):
                if segment[2] == 0:
                    # don't go out of bounds, end function
                    valid_move = False
                    break
                else:
                    z, y, x = segment[0], segment[1], segment[2]
                    updated[i] = [z, y, x - 1]
        elif direction == "down":
            for i, segment in enumerate(self.current_block):
                z, y, x = segment[0], segment[1], segment[2]
                updated[i] = [z, y - 1, x]

        if valid_move:
            for segment in updated:
                if segment in self.field or segment[1] < 0:
                    # block placed!
                    print("block placed!")
                    for part in self.current_block:
                        if not part in self.field:
                            self.field.append(part)
                    self.current_block = self.possible_blocks[random.randint(0, (len(self.possible_blocks) - 1))]
                    return
                else:
                    self.current_block = updated

    # does everything necessary to correctly update the board.
    def update_board(self):
        self.clear_board()
        for segment in self.current_block:
            z, y, x = 3 - segment[0], 3 - segment[1], 3 - segment[2]
            # draw parts of the current block as active
            if z in range(0, 4) and y in range(0, 4) and x in range(0, 4):
                self.board[z][y][x][1] = True

        print(self.field)
        for segment in self.field:
            z, y, x = 3 - segment[0], 3 - segment[1], 3 - segment[2]
            self.board[z][y][x][1] = True

    def field_is_filled(self):
        count = 0
        for segment in self.field:
            if segment[1] == 0:
                count += 1
        return count == 16

    def update_field(self):
        if self.field_is_filled():
            self.score += 1
            for segment in self.field:
                if segment[1] == 0:
                    self.field.remove(segment)
                else:
                    segment[1] -= 1

    # return the board as an array of the bits to be sent to the FPGA
    # see the protocol for what the representation means
    def get_board_as_sendable(self):
        data = []
        brightness = []

        # chunk is 8 bits
        chunk = []
        for z_index, z in enumerate(self.board):
            for y_index, y in enumerate(z):
                if len(chunk) >= 8:
                    data.append(chunk)
                    chunk = []
                for x_index, x in enumerate(y):
                    if not x[1]:
                        # there is nothing at this position
                        brightness = [0, 0, 0, 0, 0, 0, 0, 0]
                    else:
                        brightness = [1, 1, 1, 1, 1, 1, 1, 1]
                    data.append(brightness)
        return data







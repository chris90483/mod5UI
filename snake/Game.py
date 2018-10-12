class SnakeGame:

    # board[x][y][z] means board[front to back][bottom to top][right to left]
    # see https://docs.google.com/document/d/1-LGIlPrV1G8JojxiikUIvX7hAX0S8LZAeEbLJSfVa48
    # for an explanation.
    board = []

    # The score the player has (= #apples eaten)
    score = 0

    # Heading of the snake
    # Convention: x, y or z and then + or - to indicate lower or higher in the index
    heading = "x+"

    #snake body, expressed in coordinates
    snake_body = [(0, 0, 0), (0, 0, 1)]

    # [[=========]]
    # [[FUNCTIONS]]
    # [[=========]]

    # initializes the board so all values are False (meaning all LEDs should be off)
    def setup_board(self):
        board = []
        for x in range(0, 4):
            board.append(self.make_plane())
        return board

    # [[===========================]]
    # [[internal stuff, just ignore]]
    # [[===========================]]

    def make_plane(self):
        plane = []
        for x in range(0, 4):
            plane.append(self.make_layer())
        return plane


    def make_layer(self):
        return [False] * 4
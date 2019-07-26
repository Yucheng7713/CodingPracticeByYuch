class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = collections.deque([[0, 0]])
        self.food = collections.deque(food)
        self.width = width
        self.height = height
        self.dirt = {
            "U": [-1, 0],
            "D": [1, 0],
            "L": [0, -1],
            "R": [0, 1]
        }

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # The next new snake head according to the direction
        new_head = [self.snake[0][0] + self.dirt[direction][0], self.snake[0][1] + self.dirt[direction][1]]
        # Game Over conditions
        if new_head[0] < 0 or new_head[0] > self.height - 1 or \
           new_head[1] < 0 or new_head[1] > self.width - 1 or \
           (new_head in self.snake and new_head != self.snake[-1]):
            return -1
        # Eat food
        if self.food and new_head == self.food[0]:
            self.snake.appendleft(self.food.popleft())
        # Moving snake
        else:
            self.snake.appendleft(new_head)
            self.snake.pop()
        # The score is exact the length of the snake
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

class SnakeBlock:
    def __init__(self):
        self.dir = None
        self.snake = None
        self.food = None

class SnakeGame_II:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        # Parameters
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        # Construct game board
        self.board = [[SnakeBlock() for _ in range(self.width)] for _ in range(self.height)]
        # Snake initialize
        self.board[0][0].snake = True
        self.snakeHead = (0, 0)
        # Food initialize
        f = food.pop(0)
        self.board[f[0]][f[1]].food = True

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # Game over conditions
        if (self.snakeHead[0] == 0 or self.board[self.snakeHead[0]-1][self.snakeHead[1]].snake) and direction == "L" \
                or (self.snakeHead[0] == width - 1 or self.board[self.snakeHead[0]+1][self.snakeHead[1]].snake) and direction == "R" \
                or (self.snakeHead[1] == 0 or self.board[self.snakeHead[0]][self.snakeHead[1]-1].snake) and direction == "U" \
                or (self.snakeHead[1] == height-1 or self.board[self.snakeHead[0]][self.snakeHead[1]+1].snake) and direction == "D":
            return -1
        # Assign directions for each block
        for i in range(height):
            for j in range(width):
                if not board[i][j].snake:
                    board[i][j].dir = direction
        # Update only the direction for the block that is occupied by snake head
        board[self.snakeHead[0]][self.snakeHead[1]] = direction
        # Moving snake
        for i in range(height):
            for j in range(width):
                if self.board[i][j].dir == 'R'


        # Your SnakeGame object will be instantiated and called as such:
        # obj = SnakeGame(width, height, food)
        # param_1 = obj.move(direction)
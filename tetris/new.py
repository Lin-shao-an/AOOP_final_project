import pygame
import random

keys = []

config = open('config.txt','r')
for i in config:
    k = i.split("= ")[1]
    k = k.split("\n")[0]
    k = k.lower()
    match k:
        case 'a' : keys.append(pygame.K_a)
        case 'b' : keys.append(pygame.K_b)
        case 'c' : keys.append(pygame.K_c)
        case 'd' : keys.append(pygame.K_d)
        case 'e' : keys.append(pygame.K_e)
        case 'f' : keys.append(pygame.K_f)
        case 'g' : keys.append(pygame.K_g)
        case 'h' : keys.append(pygame.K_h)
        case 'i' : keys.append(pygame.K_i)
        case 'j' : keys.append(pygame.K_j)
        case 'k' : keys.append(pygame.K_k)
        case 'l' : keys.append(pygame.K_l)
        case 'm' : keys.append(pygame.K_m)
        case 'n' : keys.append(pygame.K_n)
        case 'o' : keys.append(pygame.K_o)
        case 'p' : keys.append(pygame.K_p)
        case 'q' : keys.append(pygame.K_q)
        case 'r' : keys.append(pygame.K_r)
        case 's' : keys.append(pygame.K_s)
        case 't' : keys.append(pygame.K_t)
        case 'u' : keys.append(pygame.K_u)
        case 'v' : keys.append(pygame.K_v)
        case 'w' : keys.append(pygame.K_w)
        case 'x' : keys.append(pygame.K_x)
        case 'y' : keys.append(pygame.K_y)
        case 'z' : keys.append(pygame.K_z)
        case 'left' : keys.append(pygame.K_LEFT)
        case 'right' : keys.append(pygame.K_RIGHT)
        case 'up' : keys.append(pygame.K_UP)
        case 'down' : keys.append(pygame.K_DOWN)
        case 'space' : keys.append(pygame.K_SPACE)
        case 'esc' : keys.append(pygame.K_ESCAPE)
        case _: keys.append(pygame.K_ESCAPE)

leftKey = keys[0]
rightKey = keys[1]
softDropKey = keys[2]
hardDropKey = keys[3]
rotateLeftKey = keys[4]
rotateRightKey = keys[5]
holdKey = keys[6]
quitKey = keys[7]

pygame.init()
screen = pygame.display.set_mode((600, 760))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

background = pygame.image.load("assets/bg2.png")
iSprite = pygame.image.load("assets/I.png")
jSprite = pygame.image.load("assets/J.png")
lSprite = pygame.image.load("assets/L.png")
oSprite = pygame.image.load("assets/O.png")
sSprite = pygame.image.load("assets/S.png")
tSprite = pygame.image.load("assets/T.png")
zSprite = pygame.image.load("assets/Z.png")
minoSprite = [pygame.image.load("assets/IM.png"),
              pygame.image.load("assets/JM.png"),
              pygame.image.load("assets/LM.png"),
              pygame.image.load("assets/OM.png"),
              pygame.image.load("assets/SM.png"),
              pygame.image.load("assets/TM.png"),
              pygame.image.load("assets/ZM.png"),
              pygame.image.load("assets/ghost.png")]

board = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #20
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

kickTableN = [[[ 0, 0], [-1, 0], [-1, 1], [ 0,-2], [-1,-2]], # 0->1 & 2->1
              [[ 0, 0], [ 1, 0], [ 1,-1], [ 0, 2], [ 1, 2]], # 1->0 & 1->2
              [[ 0, 0], [ 1, 0], [ 1, 1], [ 0,-2], [ 1,-2]], # 0->3 & 2->3
              [[ 0, 0], [-1, 0], [-1,-1], [ 0, 2], [-1, 2]]] # 3->0 & 3->2

kickTableI = [[[ 0, 0], [-2, 0], [ 1, 0], [-2,-1], [ 1, 2]], # 0->1 & 3->2
              [[ 0, 0], [ 2, 0], [-1, 0], [ 2, 1], [-1,-2]], # 1->0 & 2->3
              [[ 0, 0], [-1, 0], [ 2, 0], [-1, 2], [ 2,-1]], # 0->3 & 1->2
              [[ 0, 0], [ 1, 0], [-2, 0], [ 1,-2], [-2, 1]]] # 3->0 & 2->1

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.image = None
        self.rect = None
        self.x = 0
        self.y = 0
        self.state = [0]
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 0
        self.type = " "
        self.das = 100  # Delay Auto Shift (milliseconds)
        self.arr = 10   # Auto Repeat Rate (milliseconds)
        self.left_key_timer = None
        self.right_key_timer = None
        self.last_shift_time = None

    def fall(self):
        self.rect.y += 30
        self.y += 1

    def move(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        # Handle left movement
        if keys[leftKey]:
            if self.left_key_timer is None:  # Key just pressed
                self.left_key_timer = current_time
                self.last_shift_time = None
                self.try_move(-1, 0, board)  # Immediate move
            elif current_time - self.left_key_timer >= self.das:  # DAS activated
                if self.last_shift_time is None or current_time - self.last_shift_time >= self.arr:
                    self.try_move(-1, 0, board)
                    self.last_shift_time = current_time
        else:
            self.left_key_timer = None  # Reset when key is released

        # Handle right movement
        if keys[rightKey]:
            if self.right_key_timer is None:  # Key just pressed
                self.right_key_timer = current_time
                self.last_shift_time = None
                self.try_move(1, 0, board)  # Immediate move
            elif current_time - self.right_key_timer >= self.das:  # DAS activated
                if self.last_shift_time is None or current_time - self.last_shift_time >= self.arr:
                    self.try_move(1, 0, board)
                    self.last_shift_time = current_time
        else:
            self.right_key_timer = None  # Reset when key is released

        # Handle soft drop
        if keys[softDropKey]:
            self.try_move(0, 1, board)  # Immediate move down

        return True

    def try_move(self, dx, dy, board):
        canMove = True
        for i in range(self.size):
            for j in range(self.size):
                if self.space[i][j] == 1:
                    new_x = self.x + j + dx
                    new_y = self.y + i + dy
                    if new_x < 0 or new_x >= len(board[0]) or new_y < 0 or new_y >= len(board) or board[new_y][new_x] == 1:
                        canMove = False
        if canMove:
            self.x += dx
            self.y += dy
            self.rect.x += dx * 30
            self.rect.y += dy * 30

    def hardDrop(self):
        move = 0
        canMove = True
        while(canMove):
            move += 1
            for i in range(self.size):
                for j in range(self.size):
                    if self.space[i][j] == 1 and board[self.y + i+move][self.x + j] == 1:
                        move -= 1
                        canMove = False
        self.y += move
        self.rect.y += 30*move

    def rotate(self):
        keys = pygame.key.get_pressed()
        if keys[rotateRightKey]: #right rotate
            if not self.rotating:
                if self.type == "I":
                    match(self.idx):
                        case 0: table = kickTableI[0]
                        case 1: table = kickTableI[2]
                        case 2: table = kickTableI[1]
                        case 3: table = kickTableI[3]
                if self.type == "O":
                    return
                else:
                    match(self.idx):
                        case 0: table = kickTableN[0]
                        case 1: table = kickTableN[1]
                        case 2: table = kickTableN[2]
                        case 3: table = kickTableN[3]
                for i in range(len(table)):
                    canRotate = True
                    tempX = self.x + table[i][0]
                    tempY = self.y - table[i][1]
                    for j in range (self.size):
                        for k in range (self.size):
                            if self.state[(self.idx+1)%4][j][k] == 1 and board[tempY + j][tempX + k] == 1:
                                canRotate = False
                                break
                        if not canRotate:
                            break
                    if canRotate:
                        self.image = pygame.transform.rotate(self.image, -90)
                        self.idx = (self.idx+1)%4
                        self.space = self.state[self.idx]
                        self.rect.x += table[i][0]*30
                        self.rect.y -= table[i][1]*30
                        self.x = tempX
                        self.y = tempY
                        break
            self.rotating = True
        elif keys[rotateLeftKey]: #left rotate
            if not self.rotating:
                if self.type == "I":
                    match(self.idx):
                        case 0: table = kickTableI[3]
                        case 1: table = kickTableI[1]
                        case 2: table = kickTableI[2]
                        case 3: table = kickTableI[0]
                if self.type == "O":
                    return
                else:
                    match(self.idx):
                        case 0: table = kickTableN[2]
                        case 1: table = kickTableN[1]
                        case 2: table = kickTableN[0]
                        case 3: table = kickTableN[3]
                for i in range(len(table)):
                    canRotate = True
                    tempX = self.x + table[i][0]
                    tempY = self.y - table[i][1]
                    for j in range (self.size):
                        for k in range (self.size):
                            if self.state[(self.idx+3)%4][j][k] == 1 and board[tempY + j][tempX + k] == 1:
                                canRotate = False
                                break
                        if not canRotate:
                            break
                    if canRotate:
                        self.image = pygame.transform.rotate(self.image, 90)
                        self.idx = (self.idx+3)%4
                        self.space = self.state[self.idx]
                        self.rect.x += table[i][0]*30
                        self.rect.y -= table[i][1]*30
                        self.x = tempX
                        self.y = tempY
                        break
            self.rotating = True
        else:
            self.rotating = False


    def stop(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.space[i][j] == 1 and board[self.y + i+1][self.x + j] == 1:
                    return True
        return False
    
class Mino(pygame.sprite.Sprite):
    def __init__(self, x, y, idx):
        super(Mino, self).__init__()
        self.image = minoSprite[idx]
        self.rect = self.image.get_rect()
        self.rect.x = (120 + x*30)
        self.rect.y = (20 + y*30)
        self.y = y

class I(Block):
    def __init__(self):
        super(I, self).__init__()
        self.image = iSprite
        self.rect = self.image.get_rect()
        self.rect.x = 190 + 50
        self.rect.y = -30 + 50
        self.x = 4
        self.y = 0
        self.state = [[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
                      [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
                      [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
                      [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]]
        #   ........   #   ....[]..   #   ........   #   ..[]....
        #   [][][][]   #   ....[]..   #   ........   #   ..[]....
        #   ........   #   ....[]..   #   [][][][]   #   ..[]....
        #   ........   #   ....[]..   #   ........   #   ..[]....
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 4
        self.type = 'I'

class J(Block):
    def __init__(self):
        super(J, self).__init__()
        self.image = jSprite
        self.rect = self.image.get_rect()
        self.rect.x = 190 + 50
        self.rect.y = -30 + 50
        self.x = 4
        self.y = 0
        self.state = [[[1, 0, 0], [1, 1, 1], [0, 0, 0]],
                      [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
                      [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
                      [[0, 1, 0], [0, 1, 0], [1, 1, 0]]]
        #   []....   #   ..[][]   #   ......   #   ..[]..
        #   [][][]   #   ..[]..   #   [][][]   #   ..[]..
        #   ......   #   ..[]..   #   ....[]   #   [][]..
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 3
        self.type = 'J'

class L(Block):
    def __init__(self):
        super(L, self).__init__()
        self.image = lSprite
        self.rect = self.image.get_rect()
        self.rect.x = 190 + 50
        self.rect.y = -30 + 50
        self.x = 4
        self.y = 0
        self.state = [[[0, 0, 1], [1, 1, 1], [0, 0, 0]],
        
                      [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
                      [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
                      [[1, 1, 0], [0, 1, 0], [0, 1, 0]]]
        #   ....[]   #   ..[]..   #   ......   #   [][]..
        #   [][][]   #   ..[]..   #   [][][]   #   ..[]..
        #   ......   #   ..[][]   #   []....   #   ..[]..
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 3
        self.type = 'L'

class O(Block):
    def __init__(self):
        super(O, self).__init__()
        self.image = oSprite
        self.rect = self.image.get_rect()
        self.rect.x = 220 + 50
        self.rect.y = -30 + 50
        self.x = 5
        self.y = 0
        self.state = [[[1, 1], [1, 1]],
                      [[1, 1], [1, 1]], 
                      [[1, 1], [1, 1]], 
                      [[1, 1], [1, 1]]]
        #   [][]   #   [][]   #   [][]   #   [][]
        #   [][]   #   [][]   #   [][]   #   [][]
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 2
        self.type = 'O'

class S(Block):
    def __init__(self):
        super(S, self).__init__()
        self.image = sSprite
        self.rect = self.image.get_rect()
        self.rect.x = 190 + 50
        self.rect.y = -30 + 50
        self.x = 4
        self.y = 0
        self.state = [[[0, 1, 1], [1, 1, 0], [0, 0, 0]], 
                      [[0, 1, 0], [0, 1, 1], [0, 0, 1]], 
                      [[0, 0, 0], [0, 1, 1], [1, 1, 0]], 
                      [[1, 0, 0], [1, 1, 0], [0, 1, 0]]]
        #   ..[][]   #   ..[]..   #   ......   #   []....
        #   [][]..   #   ..[][]   #   ..[][]   #   [][]..
        #   ......   #   ....[]   #   [][]..   #   ..[]..
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 3
        self.type = 'S'

class T(Block):
    def __init__(self):
        super(T, self).__init__()
        self.image = tSprite
        self.rect = self.image.get_rect()
        self.rect.x = 190 + 50
        self.rect.y = -30 + 50
        self.x = 4
        self.y = 0
        self.state = [[[0, 1, 0], [1, 1, 1], [0, 0, 0]], 
                      [[0, 1, 0], [0, 1, 1], [0, 1, 0]], 
                      [[0, 0, 0], [1, 1, 1], [0, 1, 0]], 
                      [[0, 1, 0], [1, 1, 0], [0, 1, 0]]]
        #   ..[]..   #   ..[]..   #   ......   #   ..[]..
        #   [][][]   #   ..[][]   #   [][][]   #   [][]..
        #   ......   #   ..[]..   #   ..[]..   #   ..[]..
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 3
        self.type = 'T'

class Z(Block):
    def __init__(self):
        super(Z, self).__init__()
        self.image = zSprite
        self.rect = self.image.get_rect()
        self.rect.x = 190 + 50
        self.rect.y = -30 + 50
        self.x = 4
        self.y = 0
        self.state = [[[1, 1, 0], [0, 1, 1], [0, 0, 0]], 
                      [[0, 0, 1], [0, 1, 1], [0, 1, 0]], 
                      [[0, 0, 0], [1, 1, 0], [0, 1, 1]], 
                      [[0, 1, 0], [1, 1, 0], [1, 0, 0]]]
        #   [][]..   #   ....[]   #   ......   #   ..[]..
        #   ..[][]   #   ..[][]   #   [][]..   #   [][]..
        #   ......   #   ..[]..   #   ..[][]   #   []....
        self.idx = 0
        self.space = self.state[self.idx]
        self.rotating = False
        self.size = 3
        self.type = 'Z'

blocks = pygame.sprite.Group()
currBlock = pygame.sprite.Group()
holdBlock = pygame.sprite.Group()
nextBlock = pygame.sprite.Group()
ghostPiece = pygame.sprite.Group()
bag1 = random.sample(range(0, 6 + 1), 7)
bag2 = random.sample(range(0, 6 + 1), 7)

running = True
spawn = 1
fallTimer = 0
moveTimer = 0
lockDelay = 60
startLockDelay = False
movement = 0
hardDropDelay = 0
fallSpeed = 200
line = 0
temp = 0
holdPiece = " "
holded = False
firstHold = True
minoAdded = False
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == quitKey:
                running = False

    ghostPiece.empty()
    if(spawn == 1 and hardDropDelay == 0):
        currBlock.empty()
        match bag1[0]:
            case 0: newBlock = I() 
            case 1: newBlock = J()
            case 2: newBlock = L()
            case 3: newBlock = O()
            case 4: newBlock = S()
            case 5: newBlock = T()
            case 6: newBlock = Z()
        bag1.pop(0)
        if(not bag1):
            bag1 = bag2
            bag2 = random.sample(range(0, 6 + 1), 7)
        tempBag = bag1 + bag2
        nextBlock.empty()
        for i in range(5):
            match tempBag[i]:
                case 0: nextB = I() 
                case 1: nextB = J()
                case 2: nextB = L()
                case 3: nextB = O()
                case 4: nextB = S()
                case 5: nextB = T()
                case 6: nextB = Z()
            if i == 0:
                nextB.rect.centerx = 515
                nextB.rect.centery = 180
            else:
                nextB.image = pygame.transform.scale(nextB.image, (nextB.size*20, nextB.size*20))
                nextB.rect.centerx = 515
                nextB.rect.centery = 200 + 95*i
                if nextB.type == "O":
                    nextB.rect.centerx -= 5
                    nextB.rect.centery -= 10
                if nextB.type == "I":
                    nextB.rect.centerx += 5
            nextBlock.add(nextB)
        for i in range (len(newBlock.space)):
            for j in range (len(newBlock.space)):
                if newBlock.space[i][j] == 1 and board[newBlock.y + i][newBlock.x + j] == 1:
                    running = False
        currBlock.add(newBlock)
        spawn = 0
        if(firstHold):
            firstHold = False
        else:
            holded = False
        minoAdded = False

    move = 0
    canMove = True
    while(canMove):
        move += 1
        for i in range(newBlock.size):
            for j in range(newBlock.size):
                if newBlock.space[i][j] == 1 and board[newBlock.y + i+move][newBlock.x + j] == 1:
                    move -= 1
                    canMove = False
    for i in range(newBlock.size):
        for j in range(newBlock.size):
            if(newBlock.space[i][j] == 1):
                newGhost = Mino(newBlock.x + j, newBlock.y + i+move, 7)
                ghostPiece.add(newGhost)
    
    if(moveTimer >= 4):
        movement = False
        moveTimer = 0

    if movement == False and hardDropDelay == 0:
        movement = newBlock.move()
        if movement != 0:
            if startLockDelay:
                lockDelay += 2
            moveTimer = 0

    keys = pygame.key.get_pressed()
    if keys[hardDropKey] and not hardDropped: 
        newBlock.hardDrop()
        hardDropDelay = 5
        hardDropped = True
    if not keys[hardDropKey]:
        hardDropped = False

    if keys[holdKey] and not holded: 
        holded = True
        holdBlock.empty()
        if holdPiece == " ":
            holdPiece = newBlock.type
            spawn = 1
            currBlock.empty()
            firstHold = True
        else:
            tempPiece = holdPiece
            holdPiece = newBlock.type
            currBlock.empty()
            match tempPiece:
                case "I": newBlock = I() 
                case "J": newBlock = J()
                case "L": newBlock = L()
                case "O": newBlock = O()
                case "S": newBlock = S()
                case "T": newBlock = T()
                case "Z": newBlock = Z()
            currBlock.add(newBlock)
        match holdPiece:
            case "I": holding = I() 
            case "J": holding = J()
            case "L": holding = L()
            case "O": holding = O()
            case "S": holding = S()
            case "T": holding = T()
            case "Z": holding = Z()
        holding.rect.centerx = 85
        holding.rect.centery = 180
        holdBlock.add(holding)

    if hardDropDelay == 0:
        newBlock.rotate()

    if(newBlock.stop()):
        startLockDelay = True
        if hardDropped == True:
            lockDelay = 0
    else:
        startLockDelay = False
        lockDelay = 40

    if(fallTimer >= fallSpeed and not startLockDelay):
        newBlock.fall()
        fallTimer = 0

    if lockDelay == 0:
        startLockDelay = False
        movement = False
        lockDelay = 40
        currBlock.empty() 
        spawn = 1
        if(not minoAdded):
            for i in range (newBlock.size):
                for j in range (newBlock.size):
                    if(newBlock.space[i][j] == 1):
                        match newBlock.type:
                            case "I": newMino = Mino(newBlock.x + j, newBlock.y + i, 0)
                            case "J": newMino = Mino(newBlock.x + j, newBlock.y + i, 1)
                            case "L": newMino = Mino(newBlock.x + j, newBlock.y + i, 2)
                            case "O": newMino = Mino(newBlock.x + j, newBlock.y + i, 3)
                            case "S": newMino = Mino(newBlock.x + j, newBlock.y + i, 4)
                            case "T": newMino = Mino(newBlock.x + j, newBlock.y + i, 5)
                            case "Z": newMino = Mino(newBlock.x + j, newBlock.y + i, 6)
                        blocks.add(newMino)
                        board[newBlock.y + i][newBlock.x + j] = 1
        minoAdded = True

    for i in range(22):
        clearLine = True
        for j in range(10):
            if board[i+1][j+1] == 0:
                clearLine = False
        if clearLine:
            line += 1
            temp += 1
            clear_mino = [sprite for sprite in blocks if sprite.y == i+1]
            for mino in clear_mino:
                mino.kill()
            lower_mino = [sprite for sprite in blocks if sprite.y < i+1]
            for mino in lower_mino:
                mino.rect.y += 30
                mino.y += 1
            for k in range(i+1):
                board[i+1-k] = board[i-k]
                            
        board[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


    fallTimer += 1
    moveTimer += 1
    if startLockDelay:
        lockDelay -= 1
        fallTimer = 0

    if hardDropDelay:
        hardDropDelay -= 1

    if temp >= 10:
        fallSpeed = int(fallSpeed * 0.9)
        if fallSpeed-temp < 1:
            fallSpeed = 1
        temp -= 10

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    blocks.draw(screen)
    currBlock.draw(screen)
    holdBlock.draw(screen)
    nextBlock.draw(screen)
    ghostPiece.draw(screen)
    pygame.display.update()
    pygame.display.flip()

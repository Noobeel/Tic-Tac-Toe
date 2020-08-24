import random, pygame, os, sys
from pygame.locals import *

def main() :
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)
    pygame.init()
    gameicon = pygame.image.load('./icon.png')
    pygame.display.set_icon(gameicon)
    pygame.display.set_caption('Tic Tac Toe')
    screen_info = pygame.display.Info()
    size = (screen_info.current_w,screen_info.current_h)
    screen = pygame.display.set_mode(size, RESIZABLE)

    clock = pygame.time.Clock()

    done = False
    introend = False
    choiceselected = False
    gameended = False

    while not done :
        for event in pygame.event.get() :
            if event.type == QUIT :
                done = True
            if event.type == MOUSEBUTTONDOWN : 
                if event.button == 1 : #Left Mouse Button
                    continue

            if event.type == KEYDOWN :
                if event.key == K_SPACE :
                    if not introend :
                        fadein(screen,size)
                        fadeout(screen,size)
                    introend = True

            if event.type == VIDEORESIZE:
                size = (event.w, event.h)
                screen = pygame.display.set_mode(size, RESIZABLE)
                screen.fill((255,255,255))
                screen.convert()
                pygame.display.update()
    
        if not introend :
            showintro(size[0],size[1],screen)
            pygame.display.update()
        
        if introend and not choiceselected:
            choice = ask_input(screen,size)
            screen.fill((255,255,255))
            pygame.display.update()
            choiceselected = True

        if choiceselected and not gameended :
            game(screen,size,choice)
            screen.fill((255,255,255))
            pygame.display.update()
            gameended = True
        
        if gameended :
            if ask_restart(screen, size) :
                choiceselected =  False
                gameended = False
                fadein(screen,size)
                fadeout(screen,size)
            else :
                break

        clock.tick(60) #fps
    pygame.quit()
    sys.exit()


def showintro(width, height, screen) :
    menu_text = pygame.font.Font('GlueGun-GW8Z.ttf',40)
    textSurface = menu_text.render('Welcome To Tic Tac Toe', True, (0,0,0))
    textrec = textSurface.get_rect()
    textrec.center = (width//2, int(height - height//2.5))

    CommandText = pygame.font.Font('GlueGun-GW8Z.ttf',40)
    textsurf = CommandText.render('Press Space Bar To Continue', True, (0,0,0))
    textrectangle = textsurf.get_rect()
    textrectangle.center = (width//2, height - height//3)

    pic = pygame.image.load('./XO.png')
    pic_surf = pygame.Surface((width,height))
    pic_surf.fill((255,255,255))
    pic_surf.blit(pic, ((width//2)-(int(pic.get_width()//2.25)), height//4))

    screen.blit(pic_surf, (0,0))
    screen.blit(textsurf,textrectangle) 
    screen.blit(textSurface,textrec)
    pygame.display.update()

def fadein(screen, size): 
    fadein = pygame.Surface((size[0], size[1]))
    fadein.fill((0,0,0))
    for alpha in range(0, 200):
        fadein.set_alpha(alpha)
        screen.fill((255,255,255))
        screen.blit(fadein, (0,0))
        pygame.display.update()
        pygame.time.delay(2)

def fadeout(screen, size): 
    fadeout = pygame.Surface((size[0], size[1]))
    fadeout.fill((0,0,0))
    for alpha in range(200, 0, -1):
        fadeout.set_alpha(alpha)
        screen.fill((255,255,255))
        screen.blit(fadeout, (0,0))
        pygame.display.update()
        pygame.time.delay(2)

def ask_restart(screen, size) :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN :
                if event.key == K_r :
                    return True
                if event.key == K_ESCAPE :
                    return False
            if event.type == VIDEORESIZE:
                size = (event.w, event.h)
                screen = pygame.display.set_mode(size, RESIZABLE)
                screen.fill((255,255,255))
                screen.convert()
                pygame.display.update()

        text = pygame.font.Font('GlueGun-GW8Z.ttf',60)
        
        endsurf = text.render('Press R To Restart', True, (0,0,0))
        exitsurf = text.render('Press Esc Or Click The Top-Right Button To Leave', True, (0,0,0))
        
        exitrectangle = exitsurf.get_rect()
        exitrectangle.center = (size[0]//2, size[1]//3 + 100)
        screen.blit(exitsurf,exitrectangle)

        endrectangle = endsurf.get_rect()
        endrectangle.center = (size[0]//2, size[1]//3)
        screen.blit(endsurf,endrectangle)
        pygame.display.update() 

def ask_input(screen, size) :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN :
                if event.button == 1 :
                    if xrect.collidepoint(event.pos) :
                        optionchosen = 'X'
                        return optionchosen
                    if yrect.collidepoint(event.pos) :
                        optionchosen = 'O'
                        return optionchosen
            if event.type == VIDEORESIZE:
                size = (event.w, event.h)
                screen = pygame.display.set_mode(size, RESIZABLE)
                screen.fill((255,255,255))
                screen.convert()
                pygame.display.update()

        xrect = Rect(size[0]//3, size[1]//2, 200, 150)
        ximage = pygame.image.load('./x.png')
        ximage = pygame.transform.scale(ximage, (200,150))
        
        yrect = Rect(size[0]//2 + 80, size[1]//2, 200, 150)
        yimage = pygame.image.load('./o.png')
        yimage = pygame.transform.scale(yimage, (200,150))

        optiontext = pygame.font.Font('GlueGun-GW8Z.ttf',50)
        optionsurf = optiontext.render('Choose Your Character By Clicking On One Of The Options Below', True, (0,0,0))
        optionrect = optionsurf.get_rect()
        optionrect.center = (size[0]//2, size[1]//3)

        screen.fill((255,255,255))
        screen.blit(optionsurf,optionrect)
        screen.blit(ximage, (size[0]//3, size[1]//2))
        screen.blit(yimage, (size[0]//2 + 80, size[1]//2))
        pygame.display.update()

def game(screen,size,playeroption) :

    #Board Squares (Numbered like numpad)
    rectangle_7, rectangle_8, rectangle_9 = Rect(400,25,200,200),   Rect(606,25,200,200),   Rect(812,25,200,200)
    rectangle_4, rectangle_5, rectangle_6 = Rect(400,231,200,200), Rect(606,231,200,200), Rect(812,231,200,200)
    rectangle_1, rectangle_2, rectangle_3 = Rect(400,437,200,200), Rect(606,437,200,200), Rect(812,437,200,200)

    board = {7:' ',8:' ',9:' ',
             4:' ',5:' ',6:' ',
             1:' ',2:' ',3:' ' 
             }
    
    if playeroption == 'X' :
        computeroption = 'O'
    else :
        computeroption = 'X'

    def check_empty(move) :
        if board[move] == 'X' or board[move] == 'O' :
            return False
        return True

    def check_win_player(option, given_board) :
        if option == 'X' :
            if (given_board.get(7) == 'X' and given_board.get(8) == 'X' and given_board.get(9) == 'X') or (given_board.get(4) == 'X' and given_board.get(5) == 'X' and given_board.get(6) == 'X') or (given_board.get(1) == 'X' and given_board.get(2) == 'X' and given_board.get(3) == 'X') or (given_board.get(7) == 'X' and given_board.get(4) == 'X' and given_board.get(1) == 'X') or (given_board.get(8) == 'X' and given_board.get(5) == 'X' and given_board.get(2) == 'X') or (given_board.get(9) == 'X' and given_board.get(6) == 'X' and given_board.get(3) == 'X') or (given_board.get(7) == 'X' and given_board.get(5) == 'X' and given_board.get(3) == 'X') or (given_board.get(1) == 'X' and given_board.get(5) == 'X' and given_board.get(9) == 'X') :
                return True
        else :
            if (given_board.get(7) == 'O' and given_board.get(8) == 'O' and given_board.get(9) == 'O') or (given_board.get(4) == 'O' and given_board.get(5) == 'O' and given_board.get(6) == 'O') or (given_board.get(1) == 'O' and given_board.get(2) == 'O' and given_board.get(3) == 'O') or (given_board.get(7) == 'O' and given_board.get(4) == 'O' and given_board.get(1) == 'O') or (given_board.get(8) == 'O' and given_board.get(5) == 'O' and given_board.get(2) == 'O') or (given_board.get(9) == 'O' and given_board.get(6) == 'O' and given_board.get(3) == 'O') or (given_board.get(7) == 'O' and given_board.get(5) == 'O' and given_board.get(3) == 'O') or (given_board.get(1) == 'O' and given_board.get(5) == 'O' and given_board.get(9) == 'O') :
                return True
        return False

    def check_win_computer(option, given_board) :
        if option == 'X' :
            if (given_board.get(7) == 'X' and given_board.get(8) == 'X' and given_board.get(9) == 'X') or (given_board.get(4) == 'X' and given_board.get(5) == 'X' and given_board.get(6) == 'X') or (given_board.get(1) == 'X' and given_board.get(2) == 'X' and given_board.get(3) == 'X') or (given_board.get(7) == 'X' and given_board.get(4) == 'X' and given_board.get(1) == 'X') or (given_board.get(8) == 'X' and given_board.get(5) == 'X' and given_board.get(2) == 'X') or (given_board.get(9) == 'X' and given_board.get(6) == 'X' and given_board.get(3) == 'X') or (given_board.get(7) == 'X' and given_board.get(5) == 'X' and given_board.get(3) == 'X') or (given_board.get(1) == 'X' and given_board.get(5) == 'X' and given_board.get(9) == 'X') :
                return True
        else :
            if (given_board.get(7) == 'O' and given_board.get(8) == 'O' and given_board.get(9) == 'O') or (given_board.get(4) == 'O' and given_board.get(5) == 'O' and given_board.get(6) == 'O') or (given_board.get(1) == 'O' and given_board.get(2) == 'O' and given_board.get(3) == 'O') or (given_board.get(7) == 'O' and given_board.get(4) == 'O' and given_board.get(1) == 'O') or (given_board.get(8) == 'O' and given_board.get(5) == 'O' and given_board.get(2) == 'O') or (given_board.get(9) == 'O' and given_board.get(6) == 'O' and given_board.get(3) == 'O') or (given_board.get(7) == 'O' and given_board.get(5) == 'O' and given_board.get(3) == 'O') or (given_board.get(1) == 'O' and given_board.get(5) == 'O' and given_board.get(9) == 'O') :
                return True
        return False

    def get_computer_move() :
        possibleMoves = []
        for x in range(1,10) :
            if board.get(x) == ' ' :
                possibleMoves.append(x)
        
        for i in possibleMoves :
            copy = board.copy()
            copy[i] = computeroption
            if check_win_computer(computeroption, copy) :
                chosen = i
                return chosen

        for i in possibleMoves :
            copy = board.copy()
            copy[i] = playeroption
            if check_win_player(playeroption, copy) :
                chosen = i
                return chosen
        
        if 5 in possibleMoves:
            chosen = 5
            return chosen

        corners = []
        for i in possibleMoves:
            if i in [1,3,7,9]:
                corners.append(i)
        if len(corners) > 0:
            r = random.randrange(0, len(corners))
            chosen = corners[r]
            return chosen

        edges = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edges.append(i)
        if len(edges) > 0:
            r = random.randrange(0, len(edges))
            chosen = edges[r]
            return chosen

    def add_move(move, option) :
        board[move] = option

    def display_board() :
        pygame.draw.line(screen,(0,0,0),(602,25),(602,636),6) ; pygame.draw.line(screen,(0,0,0),(808,25),(808,636),6) #vertical
        pygame.draw.line(screen,(0,0,0),(400,227),(1011,227),6) ; pygame.draw.line(screen,(0,0,0),(400,433),(1011,433),6) #horizontal

        for key,value in board.items() :
            if key == 1 :
                x = 400
                y = 437
            if key == 2 :
                x = 606
                y = 437
            if key == 3 :
                x = 812
                y = 437
            if key == 4 :
                x = 400
                y = 231
            if key == 5 :
                x = 606
                y = 231
            if key == 6 :
                x = 812
                y = 231
            if key == 7 :
                x = 400
                y = 25
            if key == 8 :
                x = 606
                y = 25
            if key == 9 :
                x = 812
                y = 25
            if value == "X" :
                image = pygame.image.load('./x.png')
            elif value == "O" :
                image = pygame.image.load('./o.png')
            else :
                continue
            image = pygame.transform.scale(image,(200,200))
            screen.blit(image,(x,y))

        pygame.display.update()

    def chosenmove(move,current_count) :
        add_move(move, playeroption)
        display_board()
        pygame.time.delay(200)
        
        if check_win_player(playeroption, board) :
            return 1

        if current_count != 4 :
            computer_move = get_computer_move()
            add_move(computer_move, computeroption)
            pygame.time.delay(200)
            display_board()
            pygame.time.delay(200)

        if check_win_computer(computeroption, board) :
            return 2

        return 

    computerturn = False
    winner = None
    count = 0
    game_end = False

    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN :
                if event.button == 1 :
                    if count < 5 :
                        if rectangle_1.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(1) :
                                winner = chosenmove(1,count)
                                count += 1
                        if rectangle_2.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(2) :
                                winner = chosenmove(2,count)
                                count += 1
                        if rectangle_3.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(3) :    
                                winner = chosenmove(3,count)
                                count += 1
                        if rectangle_4.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(4) :
                                winner = chosenmove(4,count)
                                count += 1
                        if rectangle_5.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(5) :
                                winner = chosenmove(5,count)
                                count += 1
                        if rectangle_6.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(6) :
                                winner = chosenmove(6,count)
                                count += 1
                        if rectangle_7.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(7) :
                                winner = chosenmove(7,count)
                                count += 1
                        if rectangle_8.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(8) :
                                winner = chosenmove(8,count)
                                count += 1
                        if rectangle_9.collidepoint(event.pos): #checks if clicked in square
                            if check_empty(9) :
                                winner = chosenmove(9,count)
                                count += 1
            if event.type == VIDEORESIZE:
                size = (event.w, event.h)
                screen = pygame.display.set_mode(size, RESIZABLE)
                screen.fill((255,255,255))
                screen.convert()
                pygame.display.update()

            if count == 5 :
                if (not check_win_computer(computeroption, board)) and (not check_win_player(playeroption, board)) :
                    winner = 0

            if winner != None :
                screen.fill((255,255,255))
                pygame.display.update()
                if winner == 0 :
                    winner_text = pygame.font.Font('GlueGun-GW8Z.ttf',100)
                    winnerSurface = winner_text.render("It's A Draw", True, (0,0,0))
                    winner_rec = winnerSurface.get_rect()
                    winner_rec.center = (size[0]//2, size[1]//2)
                if winner == 1 :
                    winner_text = pygame.font.Font('GlueGun-GW8Z.ttf',100)
                    winnerSurface = winner_text.render("Player Has Won", True, (0,0,0))
                    winner_rec = winnerSurface.get_rect()
                    winner_rec.center = (size[0]//2, size[1]//2)
                if winner == 2 :
                    winner_text = pygame.font.Font('GlueGun-GW8Z.ttf',100)
                    winnerSurface = winner_text.render("Computer Has  Won", True, (0,0,0))
                    winner_rec = winnerSurface.get_rect()
                    winner_rec.center = (size[0]//2, size[1] - size[1]//2)

                screen.blit(winnerSurface, winner_rec)
                pygame.display.update()
                pygame.time.delay(1500)
                game_end = True
             
        if game_end :
            return
        display_board()

if __name__ == "__main__" :
    main()

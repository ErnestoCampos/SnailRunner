import pygame
from sys import exit

pygame.init() # Inicializa nuestro juego
screen = pygame.display.set_mode((800,400)) # Crea la pantalla del juego
pygame.display.set_caption("Snail Runner")
clock = pygame.time.Clock()
text_font = pygame.font.Font(r"C:\Users\campo\OneDrive\Escritorio\Game\font\Pixeltype.ttf",70)
bg_music = pygame.mixer.Sound(r"C:\Users\campo\OneDrive\Escritorio\Game\audio\music.wav")
bg_music.play()

# Superficies 
player_surface = pygame.image.load(r"C:\Users\campo\OneDrive\Escritorio\Game\graphics\Player\player_walk_1.png").convert_alpha()
test_surface = pygame.Surface((100,200))
sky_surface = pygame.image.load(r"C:\Users\campo\OneDrive\Escritorio\Game\graphics\Sky.png").convert()
ground_surface = pygame.image.load(r"C:\Users\campo\OneDrive\Escritorio\Game\graphics\ground.png").convert()
text_surface = text_font.render("Snail Runner", False, "Black")
game_over_surface = text_font.render("Game Over", False, "Black") 
snail_surface = pygame.image.load(r"C:\Users\campo\OneDrive\Escritorio\Game\graphics\snail\snail1.png").convert_alpha()
test_surface.fill("White")

# Rectangulos
player_rect = player_surface.get_rect(midbottom = (80,300))
snail_rect = snail_surface.get_rect(bottomright = (700,300))

# Puntuacion
score = 0

# Gravedad
gravity = 0

# Game Over
game_over = False

while True: # Para que el juego se mantenga inicializado por siempre
    for event in pygame.event.get(): # Recoge eventos

        if event.type == pygame.QUIT: 
            pygame.quit() # Sale del juego
            exit()            

        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
            jump_sound = pygame.mixer.Sound(r"C:\Users\campo\OneDrive\Escritorio\Game\audio\jump.mp3")
            jump_sound.play()
            gravity = -24
            
    if game_over == False:
        screen.blit(test_surface,(0,0))
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(text_surface,(250,50))
        screen.blit(player_surface,player_rect)
        screen.blit(snail_surface,snail_rect)
        snail_rect.centerx -= 4
        
        # Fisicas del Caracol
        if snail_rect.right <= 0: snail_rect.left = 800
        
        # Puntuacion del Jugador
        if game_over == False:
            score += 1
            score_surface = text_font.render(f"Score: {score}", False, "Black")
            screen.blit(score_surface,(500,345))
        if game_over == True:
            score = score
            score_surface = text_font.render(f"Score: {score}", False, "Black")
            screen.blit(score_surface,(500,345))

        # Fisicas del Jugador
        gravity += 1
        player_rect.centery += gravity
        if player_rect.bottom > 300: player_rect.bottom = 300

        # Colision con el caracol
        if snail_rect.colliderect(player_rect):
            game_over = True
    else:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(score_surface,(550,345))
        screen.blit(game_over_surface,(200,150))

    pygame.display.update() # Actualiza los fotogramas 
    clock.tick(60) # Pone un limite de fotogramas 
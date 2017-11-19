import sys
import pygame
import subprocess

try:
    proc = subprocess.Popen('python Mqtt_OK.py',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
except:
    pass

datavr = "No data"
pygame.init()
screen = pygame.display.set_mode((1024, 200))
clock = pygame.time.Clock()
try:
    pygame.mixer.init(44100, -16,2,2048)
    pygame.mixer.music.load("thrown.mp3")
except (pygame.error):
    print"No audio device"
    pass

done = False

font = pygame.font.SysFont("comicsansms", 40)
text = font.render(datavr.encode('utf8'), True, (0, 128, 0))

while not done:
    output = proc.stdout.readline()
    datavr = output.rstrip()
    if output == "":
        print "datat ei tule"
    else:
        print "data tuleb"
        print datavr
        if datavr == "Alused otsas!!":
            try:
                pygame.mixer.music.play()
            except:
                pass

        text = font.render(datavr, True, (0, 128, 0))
        datavr = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
                done = True
                break


    screen.fill((255,255,255))
    screen.blit(text,(160 - text.get_width() // 2, 100 - text.get_height() // 2))
    pygame.display.flip()
    # change_varible()

    clock.tick(60)

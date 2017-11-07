import sys
import pygame
import subprocess

proc = subprocess.Popen('python Mqtt_OK.py',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
datavr = "No data"
pygame.init()
screen = pygame.display.set_mode((320, 200))
clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("comicsansms", 40)
text = font.render(datavr, True, (0, 128, 0))

while not done:
    output = proc.stdout.readline()
    datavr = output.rstrip()
    if output == "":
        print "datat ei tule"
    else:
        print "data tuleb"
        print output
        text = font.render(datavr, True, (0, 128, 0))
        datavr = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break


    screen.fill((255, 255, 255))
    screen.blit(text,(160 - text.get_width() // 2, 100 - text.get_height() // 2))
    pygame.display.flip()
    #change_varible()

    clock.tick(60)
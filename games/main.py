import pygame

       self.direction = 0
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
            self.direction = -1
        if keys[pygame.K_RIGHT]:
            self.direction = 1



clock = pygame.time.Clock()

projectiles = []

shooter = Shooter()

while running:

    ##

    dt = clock.tick(60)/1000

    shooter = Shooter()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            projectiles.append(Projectile(shooter.position.x, shooter.position.y))       
 
    def update(self, dt):
        self.directio = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
        if keys[pygame.K_RIGHT]:
            self.direction = 1
        self.position.xy = (self.position.x self.position.y - self.direction*5*60*dt)

    BulletY -= 5*60*dt
    Screen.fill(background)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(312,y,16,16))
    pygame.display.flip()

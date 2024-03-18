import pygame
from pygame.sprite import Sprite
import util
import random
import os 

class Zombie(Sprite):
    def __init__(self, contenedor):
        super().__init__()
        self.contenedor = contenedor
        self.imagenes = [
            util.cargar_imagen('imagenes/Z0.png'),
            util.cargar_imagen('imagenes/Z1.png'),
            util.cargar_imagen('imagenes/Z2.png'),
            util.cargar_imagen('imagenes/Z3.png'),
            util.cargar_imagen('imagenes/Z4.png'),
            util.cargar_imagen('imagenes/Z5.png'),
            util.cargar_imagen('imagenes/Z6.png'),
            util.cargar_imagen('imagenes/Z7.png')
        ]
        self.cont = 0
        self.sentido = 0
        self.image = self.imagenes[self.sentido]
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.x = random.randint(0, contenedor[0])
        self.rect.y = 320
        self.vel = 1.5
        self.velocidad_animacion = 8
        self.animacion_contador = 0 
        self.gruñido = pygame.mixer.Sound('sonido/gruñido.mp3')
        self.gruñido.set_volume(0.05)
        self.gruñido.play()
        self.cargar_fotos()  

    def cargar_fotos(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        imagenes_dir = os.path.join(base_dir, 'imagenes')
        imagen_muerto = [
            'Zmuerto0.png',
            'Zmuerto1.png',
            'Zmuerto2.png',
            'Zmuerto3.png'
        ]
        for imagen in imagen_muerto:
            self.imagenes.append(pygame.image.load(os.path.join(imagenes_dir, imagen)).convert_alpha())

    def morir(self):
        self.vel = 0
        self.image = self.imagenes[-1]

    def update(self):
        self.animacion_contador += 1
        if self.animacion_contador >= self.velocidad_animacion:
            self.animacion_contador = 0
            self.cont += 1
            if self.cont >= len(self.imagenes):
                self.cont = 0
        self.rect.x -= self.vel
        if self.rect.right <= 0:
            self.rect.x = self.contenedor[0]
        self.image = self.imagenes[self.cont]

def main():
    pygame.init()
    pygame.mixer.init()


if __name__ == "__main__":
    main()

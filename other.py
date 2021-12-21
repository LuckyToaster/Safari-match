import pygame as pg

class Dimmer:
    def __init__(self, keepalive=0):
        self.keepalive=keepalive
        if self.keepalive:
            self.buffer=pg.Surface(pg.display.get_surface().get_size())
        else:
            self.buffer=None
        
    def dim(self, darken_factor=64, color_filter=(0,0,0)):
        if not self.keepalive:
            self.buffer=pg.Surface(pg.display.get_surface().get_size())
        self.buffer.blit(pg.display.get_surface(),(0,0))
        if darken_factor>0:
            darken=pg.Surface(pg.display.get_surface().get_size())
            darken.fill(color_filter)
            darken.set_alpha(darken_factor)
            # safe old clipping rectangle...
            old_clip=pg.display.get_surface().get_clip()
            # ..blit over entire screen...
            pg.display.get_surface().blit(darken,(0,0))
            pg.display.flip()
            # ... and restore clipping
            pg.display.get_surface().set_clip(old_clip)

    def undim(self):
        if self.buffer:
            pg.display.get_surface().blit(self.buffer,(0,0))
            pg.display.flip()
            if not self.keepalive:
                self.buffer=None
            
class FPSCounter:
    def __init__(self, surface, font, clock, color, pos):
        self.surface = surface
        self.font = font
        self.clock = clock
        self.pos = pos
        self.color = color

        self.fps_text = self.font.render(str(int(self.clock.get_fps())) + "FPS", False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))
    
    def update(self):
        self.fps_text = self.font.render(str(self.clock.get_fps()) + "FPS", False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))

    def update(self):
        text = f"{self.clock.get_fps():2.0f} FPS"
        self.fps_text = self.font.render(text, False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1])) 
# Module pour contrôler l'écran (SH1107 OLED)
# -----------------------------------------------
# NOTE: L'écran utilise un système de 'pages'. Chaque page correspond à 8 lignes de la sortie...
# Écrit par LDA (prenant une pause pour https://git.planet-casio.com/lda/suiko, je hais le multiplier)
from smbus import SMBus as I2C
import numpy as np
WIDTH, HEIGHT = 128, 128

I2C_COMMAND                 = 0x80
I2C_DATA                    = 0x40

class Display:
    def __init__(self, i2c_bus: int = 1, i2c_address: int = 0x3C):
        self.i2c = I2C(i2c_bus)
        self.address = i2c_address

        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0xAE)
        self.enable()
        self.set_page(0)
        self.set_column(0)

        self.ibuf = [ 0 ] * WIDTH
        self.screen = []
        self.page_modifies = set()

        for y in range(HEIGHT):
            l = []
            self.screen.append(l)
            for x in range(WIDTH):
                l.append(0)

        for y in range(HEIGHT):
            l = self.modifie_ligne(y)
            for x in range(WIDTH):
                l[x] = 0
        self.push()

        for y in range(12, 23):
            l = self.modifie_ligne(y)
            for x in range(WIDTH):
                l[x] = 1
        self.push()

    def modifie_ligne(self, lidx):
        """ Retourne la nième ligne du framebuffer. Vous DEVEZ 
        utiliser cette fonction, sinon push() sera incapable 
        de savoir que la ligne a été modifiée. """
        self.page_modifies |= { lidx // 8 }
        return self.screen[lidx]

    def push(self):
        """ Écrit le contenu du _framebuffer_ (self.screen) à l'écran.
        TODO: c'est LEEEENT! """
        # Nous voulons incrémenter la colonne (donc écrire 0x20) au lieu 
        # de la page (écrire 0x21)
        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0x20)
        self.set_page(0)
        self.set_column(0)

        for page in self.page_modifies:
            self.set_page(page)
            idata = self.screen[ (page + 0) << 3 : (page + 1) << 3 ]
            for x in range(WIDTH):
                w = 0
                for uh in range(7, -1, -1):
                    w <<= 1
                    w |= idata[uh][x] # Would be handy if we could swap x and uh
                self.ibuf[x] = w
            self.blit_full_page(list(self.ibuf))
        self.page_modifies = set()

    def enable(self):
        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0xAF)
        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0xA6)
    def set_page(self, page: int):
        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0xB0 | page)
    def set_column(self, column: int):
        column_hi, column_lo = (column >> 4) & 0x7, (column >> 0) & 0xF
        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0x00 | column_lo)
        self.i2c.write_byte_data(self.address, I2C_COMMAND, 0x10 | column_hi)
    def blit_page(self, page: int):
        self.i2c.write_byte_data(self.address, I2C_DATA, page)
    def blit_full_page(self, page: int):
        for x in range(WIDTH // 32):
            self.i2c.write_i2c_block_data(self.address, I2C_DATA, page[32*x:32*x+32])


d = Display()

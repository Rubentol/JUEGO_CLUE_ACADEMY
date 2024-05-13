import pygame
import random
import sys


pygame.init()

GRIS = (200,200,200)
NEGRO = (0,0,0)
ROJO = (200,0,0)
AMARILLO = (200,200,0)
VERDE = (0,255,0)
BLANCO = (255,255,255)

ANCHO = 1100
ALTO = 650

# Definir dimensiones del TextArea
TEXTAREA_ANCHO = 525
TEXTAREA_ALTO = 350

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Clue")

# Cargar la imagen de fondo
fondo = pygame.image.load("Fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Cargar la imagen de los personajes
personajes = pygame.image.load("Personajes.jpg")
armas = pygame.image.load("Armas.jpg")
lugares = pygame.image.load("Lugares.jpg")

# Crear un objeto de fuente
titulo = pygame.font.Font(None, 50)

# Renderizar el texto
titulo = titulo.render("Juego Clue Academia de Ruben Dios <3", True, GRIS)

# Obtener el rectángulo del texto para centrarlo en la ventana
titulo_rect = titulo.get_rect(center=(ANCHO//2, ALTO//11))

# Crear el TextArea
textarea_rect = pygame.Rect((ANCHO - TEXTAREA_ANCHO) // 1.4, (ALTO - TEXTAREA_ALTO) // 3, TEXTAREA_ANCHO, TEXTAREA_ALTO)
textarea_surface = pygame.Surface((TEXTAREA_ANCHO, TEXTAREA_ALTO))
textarea_surface.fill(GRIS)

# Fuente y texto
font = pygame.font.SysFont("Arial", 20)
text = "                           Bienvenido al Juego Clue Academia \nEn este juego te sumergirás en un mundo de secretos, pistas ocultas\n y misterio por resolver."

# Crear el botón
boton_salir_rect = pygame.Rect(975, 100, 85, 45)
boton_jugar_rect = pygame.Rect(975, 200, 85, 45)   
boton_reiniciar_rect = pygame.Rect(975, 300, 85, 45) 
boton_siguiente_rect = pygame.Rect(975, 400, 85, 45)  

# Fuente y texto del botón
botones = pygame.font.Font(None, 24)
jugar = botones.render("Jugar", True, NEGRO)
texto_jugar_rect = jugar.get_rect(center=boton_jugar_rect.center)
salir = botones.render("Salir", True, NEGRO)
texto_salir_rect = salir.get_rect(center=boton_salir_rect.center)
reiniciar = botones.render("Reiniciar", True, NEGRO)
texto_reiniciar_rect = reiniciar.get_rect(center=boton_reiniciar_rect.center)
siguiente = botones.render("Siguiente", True, NEGRO)
texto_siguiente_rect = siguiente.get_rect(center=boton_siguiente_rect.center)

#Preguntas

Preg = pygame.font.Font(None, 32)
Preg1 = Preg.render("¿Quién es el asesino?", True, GRIS)
Preg2 = Preg.render("¿Qué arma se usó en el crimen?", True, GRIS)
Preg3 = Preg.render("¿Dónde tuvo lugar el asesinato?", True, GRIS)

Preg1_rect = Preg1.get_rect(center=(ANCHO//1.55, ALTO//1.38))
Preg2_rect = Preg2.get_rect(center=(ANCHO//1.55, ALTO//1.23))
Preg3_rect = Preg3.get_rect(center=(ANCHO//1.55, ALTO//1.11))

#Botones RadioButton (Respuestas)

class RadioButton1:
    all_buttons1 = []  # Lista para almacenar todas las instancias de RadioButton

    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, 20, 20)
        self.selected = False
        RadioButton1.all_buttons1.append(self)  # Agregar esta instancia a la lista de botones

    def draw(self, surface):
        pygame.draw.rect(surface, ROJO, self.rect, 2)
        if self.selected:
            pygame.draw.circle(surface, GRIS, (self.rect.x + 10, self.rect.y + 10), 7)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(self.text, True, GRIS)
        surface.blit(text_surface, (self.rect.x + 30, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Si este botón se selecciona, deselecciona todos los demás
                for button in RadioButton1.all_buttons1:
                    button.selected = False
                self.selected = True

Per1 = RadioButton1("#1 Luther", 400, 485)
Per2 = RadioButton1("#2 Diego", 520, 485)
Per3 = RadioButton1("#3 Allison", 640, 485)
Per4 = RadioButton1("#5 Five", 780, 485)
Per5 = RadioButton1("#7 Vayan", 900, 485)

class RadioButton2:
    all_buttons2 = []  # Lista para almacenar todas las instancias de RadioButton

    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, 20, 20)
        self.selected = False
        RadioButton2.all_buttons2.append(self)  # Agregar esta instancia a la lista de botones

    def draw(self, surface):
        pygame.draw.rect(surface, ROJO, self.rect, 2)
        if self.selected:
            pygame.draw.circle(surface, GRIS, (self.rect.x + 10, self.rect.y + 10), 7)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(self.text, True, GRIS)
        surface.blit(text_surface, (self.rect.x + 30, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Si este botón se selecciona, deselecciona todos los demás
                for button in RadioButton2.all_buttons2:
                    button.selected = False
                self.selected = True

Arm1 = RadioButton2("Paraguas", 400, 545)
Arm2 = RadioButton2("Acha", 520, 545)
Arm3 = RadioButton2("Chango", 640, 545)
Arm4 = RadioButton2("Sarten", 780, 545)
Arm5 = RadioButton2("Rifle", 900, 545)

class RadioButton3:
    all_buttons3 = []  # Lista para almacenar todas las instancias de RadioButton

    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, 20, 20)
        self.selected = False
        RadioButton3.all_buttons3.append(self)  # Agregar esta instancia a la lista de botones

    def draw(self, surface):
        pygame.draw.rect(surface, ROJO, self.rect, 2)
        if self.selected:
            pygame.draw.circle(surface, GRIS, (self.rect.x + 10, self.rect.y + 10), 7)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(self.text, True, GRIS)
        surface.blit(text_surface, (self.rect.x + 30, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Si este botón se selecciona, deselecciona todos los demás
                for button in RadioButton3.all_buttons3:
                    button.selected = False
                self.selected = True

Lug1 = RadioButton3("Sala", 400, 605)
Lug2 = RadioButton3("Bar", 520, 605)
Lug3 = RadioButton3("Oficina", 640, 605)
Lug4 = RadioButton3("Habitacion", 780, 605)
Lug5 = RadioButton3("Recibidor", 905, 605)

def obtener_seleccion(botones):
    for button in botones:
        if button.selected:
            return button
    return None


def abrir_ventana():
    global text

    while True: 

        #Ejecutar Ventana
        ventana.fill(GRIS)
        ventana.blit(fondo, (0, 0))
        #Imagenes
        ventana.blit(personajes, (400 // 2 - personajes.get_width() // 2, 110))
        ventana.blit(armas, (190 // 2 - armas.get_width() // 2, 435))
        ventana.blit(lugares, (560 // 2 - lugares.get_width() // 2, 400))
        #Textos
        ventana.blit(titulo, titulo_rect) 
        ventana.blit(Preg1, Preg1_rect)
        ventana.blit(Preg2, Preg2_rect)
        ventana.blit(Preg3, Preg3_rect)

        # Dibujar el área de texto
        pygame.draw.rect(ventana, GRIS, textarea_rect)
        pygame.draw.rect(ventana, NEGRO, textarea_rect, 2)

        # Renderizar y mostrar el texto en el área de texto
        lines = text.split('\n')
        y = textarea_rect.y + 5  # Comenzar a dibujar desde un poco abajo del borde superior del área de texto
        for line in lines:
            line_surface = font.render(line, True, NEGRO)
            ventana.blit(line_surface, (textarea_rect.x + 5, y))
            y += line_surface.get_height()

        # Dibujar el botón
        pygame.draw.rect(ventana, ROJO, boton_jugar_rect)
        pygame.draw.rect(ventana, NEGRO, boton_jugar_rect, 2)  # Borde del botón
        ventana.blit(jugar, texto_jugar_rect)
        pygame.draw.rect(ventana, AMARILLO, boton_salir_rect)
        pygame.draw.rect(ventana, NEGRO, boton_salir_rect, 2)
        ventana.blit(salir, texto_salir_rect)
        pygame.draw.rect(ventana, BLANCO, boton_reiniciar_rect)
        pygame.draw.rect(ventana, NEGRO, boton_reiniciar_rect, 2)
        ventana.blit(reiniciar, texto_reiniciar_rect)
        pygame.draw.rect(ventana, BLANCO, boton_siguiente_rect)
        pygame.draw.rect(ventana, NEGRO, boton_siguiente_rect, 2)
        ventana.blit(siguiente, texto_siguiente_rect)

        Per1.draw(ventana)
        Per2.draw(ventana)
        Per3.draw(ventana)
        Per4.draw(ventana)
        Per5.draw(ventana)

        Arm1.draw(ventana)
        Arm2.draw(ventana)
        Arm3.draw(ventana)
        Arm4.draw(ventana)
        Arm5.draw(ventana)

        Lug1.draw(ventana)
        Lug2.draw(ventana)
        Lug3.draw(ventana)
        Lug4.draw(ventana)
        Lug5.draw(ventana)

         
        for evento in pygame.event.get():

            Per1.handle_event(evento)
            Per2.handle_event(evento)
            Per3.handle_event(evento)
            Per4.handle_event(evento)
            Per5.handle_event(evento)

            Arm1.handle_event(evento)
            Arm2.handle_event(evento)
            Arm3.handle_event(evento)
            Arm4.handle_event(evento)
            Arm5.handle_event(evento)

            Lug1.handle_event(evento)
            Lug2.handle_event(evento)
            Lug3.handle_event(evento)
            Lug4.handle_event(evento)
            Lug5.handle_event(evento)

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en los botones
                if boton_jugar_rect.collidepoint(evento.pos):
                    print("Botón Jugar presionado")
                    # Procesar selecciones 
                    personaje_seleccionado = obtener_seleccion(RadioButton1.all_buttons1)
                    arma_seleccionada = obtener_seleccion(RadioButton2.all_buttons2)
                    lugar_seleccionado = obtener_seleccion(RadioButton3.all_buttons3)
                    print("Personaje seleccionado:", personaje_seleccionado.text)
                    print("Arma seleccionada:", arma_seleccionada.text)
                    print("Lugar seleccionado:", lugar_seleccionado.text)
                elif boton_salir_rect.collidepoint(evento.pos):
                    print("Botón Salir presionado")
                elif boton_reiniciar_rect.collidepoint(evento.pos):
                    print("Botón Reiniciar presionado")
                elif boton_siguiente_rect.collidepoint(evento.pos):
                    print("Botón Siguiente presionado")
        
        pygame.display.flip()

# Llamar a la función para abrir la ventana
abrir_ventana()
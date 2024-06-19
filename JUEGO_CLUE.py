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

# Definir dimensiones del TextArea-----------------------------------------------------------------------------------------------------------------------------------------------------
TEXTAREA_ANCHO = 525
TEXTAREA_ALTO = 350

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Clue")

# Cargar la imagen de fondo-----------------------------------------------------------------------------------------------------------------------------------------------------
fondo = pygame.image.load("Fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Cargar la imagen de los personajes-----------------------------------------------------------------------------------------------------------------------------------------------------
personajes = pygame.image.load("Personajes.jpg")
armas = pygame.image.load("Armas.jpg")
lugares = pygame.image.load("Lugares.jpg")

# Crear un objeto de fuente-----------------------------------------------------------------------------------------------------------------------------------------------------
titulo = pygame.font.Font(None, 50)

# Renderizar el texto-----------------------------------------------------------------------------------------------------------------------------------------------------
titulo = titulo.render("Juego Clue Academia de Ruben Dios <3", True, GRIS)

# Obtener el rectángulo del texto para centrarlo en la ventana-----------------------------------------------------------------------------------------------------------------------------------------------------
titulo_rect = titulo.get_rect(center=(ANCHO//2, ALTO//11))

# Crear el TextArea-----------------------------------------------------------------------------------------------------------------------------------------------------
textarea_rect = pygame.Rect((ANCHO - TEXTAREA_ANCHO) // 1.4, (ALTO - TEXTAREA_ALTO) // 3, TEXTAREA_ANCHO, TEXTAREA_ALTO)
textarea_surface = pygame.Surface((TEXTAREA_ANCHO, TEXTAREA_ALTO))
textarea_surface.fill(GRIS)

# Fuente y texto-----------------------------------------------------------------------------------------------------------------------------------------------------
font = pygame.font.SysFont("Arial", 19)

# Crear el botón-----------------------------------------------------------------------------------------------------------------------------------------------------
boton_salir_rect = pygame.Rect(975, 100, 85, 45)
boton_jugar_rect = pygame.Rect(975, 200, 85, 45)   
boton_reiniciar_rect = pygame.Rect(975, 300, 85, 45) 
boton_siguiente_rect = pygame.Rect(975, 400, 85, 45)  

# Fuente y texto del botón-----------------------------------------------------------------------------------------------------------------------------------------------------
botones = pygame.font.Font(None, 24)
jugar = botones.render("Jugar", True, NEGRO)
texto_jugar_rect = jugar.get_rect(center=boton_jugar_rect.center)
salir = botones.render("Salir", True, NEGRO)
texto_salir_rect = salir.get_rect(center=boton_salir_rect.center)
reiniciar = botones.render("Reiniciar", True, NEGRO)
texto_reiniciar_rect = reiniciar.get_rect(center=boton_reiniciar_rect.center)
siguiente = botones.render("Siguiente", True, NEGRO)
texto_siguiente_rect = siguiente.get_rect(center=boton_siguiente_rect.center)

#Preguntas-----------------------------------------------------------------------------------------------------------------------------------------------------

Preg = pygame.font.Font(None, 32)
Preg1 = Preg.render("¿Quién es el asesino?", True, GRIS)
Preg2 = Preg.render("¿Qué arma se usó en el crimen?", True, GRIS)
Preg3 = Preg.render("¿Dónde tuvo lugar el asesinato?", True, GRIS)

Preg1_rect = Preg1.get_rect(center=(ANCHO//1.55, ALTO//1.38))
Preg2_rect = Preg2.get_rect(center=(ANCHO//1.55, ALTO//1.23))
Preg3_rect = Preg3.get_rect(center=(ANCHO//1.55, ALTO//1.11))

#Botones RadioButton (Respuestas)-----------------------------------------------------------------------------------------------------------------------------------------------------

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
    def deselect(self):
        self.selected = False

Per1 = RadioButton1("#1 Luther", 400, 485)
Per2 = RadioButton1("#2 Diego", 520, 485)
Per3 = RadioButton1("#3 Allison", 640, 485)
Per4 = RadioButton1("#5 Five", 780, 485)
Per5 = RadioButton1("#7 Vanya", 900, 485)

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

    def deselect(self):
        self.selected = False

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
    
    def deselect(self):
        self.selected = False

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

#Scroll TextArea-----------------------------------------------------------------------------------------------------------------------------------------------------
def draw_scrollbar(surface, scroll_y, textarea_rect, text_lines, font):
    total_content_height = len(text_lines) * font.get_linesize()
    visible_area_height = textarea_rect.height
    scrollbar_height = min(1, visible_area_height / total_content_height) * visible_area_height
    scrollbar_y = (scroll_y / total_content_height) * (visible_area_height - scrollbar_height)
    pygame.draw.rect(surface, (100, 100, 100), (textarea_rect.right + 5, textarea_rect.top, 10, textarea_rect.height))
    pygame.draw.rect(surface, (150, 150, 150), (textarea_rect.right + 5, textarea_rect.top + scrollbar_y, 10, scrollbar_height))

#Respuestas Aleatorias-----------------------------------------------------------------------------------------------------------------------------------------------------
def Asesino():
    asesino = ['#1 Luther', '#2 Diego', '#3 Allison', '#5 Five', '#7 Vanya'][random.randrange(5)]
    return asesino 

def Arma():
    arma = ['Paraguas', 'Hacha', 'Chango', 'Sarten', 'Rifle'][random.randrange(5)]
    return arma

def Lugar():
    lugar = ['Sala', 'Bar', 'Oficina', 'Habitacion', 'Recibidor'][random.randrange(5)]
    return lugar

#Funcion Principal de Ventana-----------------------------------------------------------------------------------------------------------------------------------------------------
def abrir_ventana():

    global text
    asesino = Asesino() 
    arma = Arma()   
    lugar = Lugar()     
    text = "                           Bienvenido al Juego Clue Academia\n En este juego te sumergirás en un mundo de secretos, pistas ocultas\n y misterio de un crimen que resolver, donde matan a #4 Klaus.\n Tenemos 5 sospechosos, 5 armas y 5 lugares el cual solo uno de ellos\n fue quien lo asesino, un arma involucrada y un lugar donde\n sucedieron los hechos.\n\n Los sospechosos:            Las Armas:                 Los Lugares:\n -#1 Luther                           -Paraguas                   -Sala\n -#2 Diego                            -Hacha                         -Bar\n -#3 Allison                           -Chango                      -Oficina\n -#5 Five                               -Sartén                        -Habitación\n -#7 Vanya                           -Rifle                            -Recibidor\n\n                             PRESIONA JUGAR PARA COMENSAR!!" 
    
    Pista1 = False
    Pista2 = False
    Pista3 = False

    scroll_y = 0
    scroll_speed = 10
    while True: 

        #Ejecutar Ventana-----------------------------------------------------------------------------------------------------------------------------------------------------
        ventana.fill(GRIS)
        ventana.blit(fondo, (0, 0))
        #Imagenes-----------------------------------------------------------------------------------------------------------------------------------------------------
        ventana.blit(personajes, (400 // 2 - personajes.get_width() // 2, 110))
        ventana.blit(armas, (190 // 2 - armas.get_width() // 2, 435))
        ventana.blit(lugares, (560 // 2 - lugares.get_width() // 2, 400))
        #Textos-----------------------------------------------------------------------------------------------------------------------------------------------------
        ventana.blit(titulo, titulo_rect) 
        ventana.blit(Preg1, Preg1_rect)
        ventana.blit(Preg2, Preg2_rect)
        ventana.blit(Preg3, Preg3_rect)

        # Dibujar el área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana, GRIS, textarea_rect)
        pygame.draw.rect(ventana, NEGRO, textarea_rect, 2)

        # Renderizar y mostrar el texto en el área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
        lines = text.split('\n')
        total_content_height = len(lines) * font.get_linesize()
        max_scroll_y = -(total_content_height - TEXTAREA_ALTO)

        # Dibujar el botón-----------------------------------------------------------------------------------------------------------------------------------------------------
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
#___________________________________________________________________________________________________________________________________________________________________________________ 
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
#___________________________________________________________________________________________________________________________________________________________________________________ 
            if evento.type == pygame.QUIT:                  #CERRAR VENTANA
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:              #SCROLL
                if evento.key == pygame.K_UP:
                    scroll_y += scroll_speed
                elif evento.key == pygame.K_DOWN:             
                    scroll_y -= scroll_speed
            elif evento.type == pygame.MOUSEBUTTONDOWN:       #MOUSEBUTTONDOWN
                if boton_salir_rect.collidepoint(evento.pos): #BOTON SALIR
                    pygame.quit()
                    sys.exit()
                elif boton_jugar_rect.collidepoint(evento.pos) and not Pista1:#Pista 1
                    if asesino == '#1 Luther':
                        text = "                           Pista 1: Sospechosos\n Los sospechosos Mencionan sus cuartadas mientras pasaba\n el crimen.\n- #1 Luther:\n            Se encontraba solo en el sótano.\n- #2 Diego:\n-          Estaba con su novia en el parque.\n- #3 Allison:\n             Se encontraba con Vanya en el jardín.\n- #5 Five:\n          Estaba disfrutando de un helado con mamá.\n- #7 Vanya:\n           Se encontraba con Allison practicando.\n\n                                                      SIGUIENTE!"
                        Pista1 = True
                    elif asesino == '#2 Diego':
                        text = "                           Pista 1: Sospechosos\n Los sospechosos Mencionan sus cuartadas mientras pasaba\n el crimen.\n- #1 Luther:\n            Se encontraba con Allison besándose.\n- #2 Diego:\n-          Practicaba su ansiedad.\n- #3 Allison:\n             Se encontraba con Luther en el jardín.\n- #5 Five:\n          Estaba meditando sobre el futuro.\n- #7 Vanya:\n           Estaba practicando con su violín.\n\n                                                      SIGUIENTE!"
                        Pista1 = True
                    elif asesino == '#3 Allison':
                        text =  "                           Pista 1: Sospechosos\n Los sospechosos Mencionan sus cuartadas mientras pasaba\n el crimen.\n- #1 Luther:\n            Estaba con Five en el centro comercial.\n- #2 Diego:\n-          Estaba espiando a Papa.\n- #3 Allison:\n             Estaba recuperándose en el sótano.\n- #5 Five:\n          Estaba con Luther.\n- #7 Vanya:\n           Estaba en unas clases de violín.\n\n                                                      SIGUIENTE!"
                        Pista1 = True
                    elif asesino == '#5 Five':
                        text = "                           Pista 1: Sospechosos\n Los sospechosos Mencionan sus cuartadas mientras pasaba\n el crimen.\n- #1 Luther:\n            Se estaba rasurando.\n- #2 Diego:\n-          Estaba comiendo con vanya.\n- #3 Allison:\n             Se estaba bañando.\n- #5 Five:\n          Estaba Ayudando a Klaus.\n- #7 Vanya:\n           Estaba en la cocina. \n\n                                                      SIGUIENTE!"
                        Pista1 = True
                    elif asesino == '#7 Vanya':
                        text =  "                           Pista 1: Sospechosos\n Los sospechosos Mencionan sus cuartadas mientras pasaba\n el crimen.\n- #1 Luther:\n            Estaba en la luna.\n- #2 Diego:\n-          Estaba buscando a su novia.\n- #3 Allison:\n             Estaba en una entrevista.\n- #5 Five:\n          Estaba practicando sus viajes del futuro.\n- #7 Vanya:\n           No recuerda que estaba haciendo.\n\n                                                      SIGUIENTE!"
                        Pista1 = True
                elif boton_reiniciar_rect.collidepoint(evento.pos):
                    asesino = Asesino()
                    arma = Arma()   
                    lugar = Lugar()  
                    Pista1 = False  
                    Pista2 = False 
                    Pista3 = False        
                    text = "                           Bienvenido al Juego Clue Academia\n En este juego te sumergirás en un mundo de secretos, pistas ocultas\n y misterio de un crimen que resolver, donde matan a #4 Klaus.\n Tenemos 5 sospechosos, 5 armas y 5 lugares el cual solo uno de ellos\n fue quien lo asesino, un arma involucrada y un lugar donde\n sucedieron los hechos.\n\n Los sospechosos:            Las Armas:                 Los Lugares:\n -#1 Luther                           -Paraguas                   -Sala\n -#2 Diego                            -Hacha                         -Bar\n -#3 Allison                           -Chango                      -Oficina\n -#5 Five                               -Sartén                        -Habitación\n -#7 Vanya                           -Rifle                            -Recibidor\n\n                             PRESIONA JUGAR PARA COMENSAR!!" 
                    for button in RadioButton1.all_buttons1:
                        button.deselect()
                    for button in RadioButton2.all_buttons2:
                        button.deselect()
                    for button in RadioButton3.all_buttons3:
                        button.deselect()

                elif boton_siguiente_rect.collidepoint(evento.pos) and Pista1:
                    if arma == 'Paraguas':
                        Pista1 = False
                        Pista2 = True
                        text = "                           Pista 2: Arma de asesinato\n Se buscaron las armas que estaban más a la mano al momento del\n crimen.\n- Paraguas:\n           Se encontró en el cuarto de #4 Klaus\n- Hacha:\n-      Estaba guardada en su lugar.\n- Chango:\n         Estaba haciendo el aseo.\n- Sartén:\n         La estaba usando mamá para cocinar.\n- Rifle:\n        Papá de estaba dando mantenimiento.\n\n                                                      SIGUIENTE!"
                    elif arma == 'Hacha':
                        Pista1 = False
                        Pista2 = True
                        text = "                           Pista 2: Arma de asesinato\n Se buscaron las armas que estaban más a la mano al momento del\n crimen.\n- Paraguas:\n           Se encontró colgado en su Lugar\n- Hacha:\n-      Se encontró cerca del cuerpo de #4 Klaus.\n- Chango:\n         Estaba Comiendo con Papa.\n- Sartén:\n         Se encontró en la estufa.\n- Rifle:\n        Papá se lo llevo de cacería.\n\n                                                      SIGUIENTE!"
                    elif arma == 'Chango':
                        Pista1 = False
                        Pista2 = True
                        text = "                           Pista 2: Arma de asesinato\n Se buscaron las armas que estaban más a la mano al momento del\n crimen.\n- Paraguas:\n           Mamá lo estaba usando en el jardín.\n- Hacha:\n-      Se encontró en el jardín ya que cortaron un árbol\n        un día anterior.\n- Chango:\n         No se encontró.\n- Sartén:\n         Estaba  sucia en el lavavajillas con huevo del desayuno.\n- Rifle:\n        Se encontró en su estuche.\n\n                                                      SIGUIENTE!"
                    elif arma == 'Sarten':
                        Pista1 = False
                        Pista2 = True
                        text = "                           Pista 2: Arma de asesinato\n Se buscaron las armas que estaban más a la mano al momento del\n crimen.\n- Paraguas:\n           Papá se lo llevo al trabajo.\n- Hacha:\n-      Mamá la está usando para cortar el\n        árbol de la calle.\n- Chango:\n         Se fue con Papá al trabajo.\n- Sartén:\n         Se encontró sucia pero fuera del\n          lavavajillas.\n- Rifle:\n        Papá de estaba dando mantenimiento.\n\n                                                      SIGUIENTE!"
                    elif arma == 'Rifle':
                        Pista1 = False
                        Pista2 = True
                        text = "                           Pista 2: Arma de asesinato\n Se buscaron las armas que estaban más a la mano al momento del\n crimen.\n- Paraguas:\n           Estaba colgado en su lugar.\n- Hacha:\n-      Estaba en la coche de papá.\n- Chango:\n         Estaba comiendo.\n- Sartén:\n         Estaba en su lugar.\n- Rifle:\n        No se encontró.\n\n                                                      SIGUIENTE!"
                elif boton_siguiente_rect.collidepoint(evento.pos) and Pista3:
                    # Procesar selecciones 
                    per_sel = obtener_seleccion(RadioButton1.all_buttons1)
                    arm_sel = obtener_seleccion(RadioButton2.all_buttons2)
                    lug_sel = obtener_seleccion(RadioButton3.all_buttons3)
                    print(per_sel)
                    print(arm_sel)
                    print(lug_sel)
                    if per_sel.text == asesino and arm_sel.text == arma and lugar == lug_sel.text:
                        text = "\n                                                  FELICIDADES!! \n\n                          Has resuelto el Crimen Detective CETIANO\n                   Espero te hayas Divertido con este Juego Didáctico\n\n\n\n\n\n\n\n\n\n                           Preciona Reiniciar para jugar nuevamente!!"
                    else: 
                        text =  "\n                          ERROR, TU RESPUESTA FUE INCORRECTA!!\n\n Las respuestas correctas son:\n- "+asesino+"\n- "+arma+"\n- "+lugar+"\n\n                              Intenta Nuevamente Precionando Reiniciar"


                elif boton_siguiente_rect.collidepoint(evento.pos) and Pista2:
                    if lugar == 'Sala':
                        Pista2 = False
                        Pista3 = True
                        text = "                           Pista 3: Lugar de crimen\n Después de la muerte de Klaus se busco donde fue asesinado.\n- Sala:\n       había sangre en la alfombra.\n- Bar:\n-     Papa estaba ahí todo el día.\n- Oficina:\n          Papá la cerro con llave desde días antes.\n- Habitación:\n             Mama estaba limpiando.\n- Recibidor:\n            La cámara no grabo nada.    \n\n   NOTA:\n       Después de contestas las preguntas de abajo presiona\n SIGUIENTE para verificar tus respuestas con la base de datos."
                    elif lugar == 'Bar':
                        Pista2 = False
                        Pista3 = True
                        text = "                           Pista 3: Lugar de crimen\n Después de la muerte de Klaus se buscó donde fue asesinado. \n- Sala:\n       La novia de #2 Diego estaba ahí.\n- Bar:\n-     Todo estaba fuera de su lugar.\n- Oficina:\n          Papá estuvo trabajando todo el día ahí.\n- Habitación: \n             Estaba Cerrada la puerta con llave.\n- Recibidor:\n            La cámara no grabo nada. \n\n   NOTA:\n       Después de contestas las preguntas de abajo presiona\n SIGUIENTE para verificar tus respuestas con la base de datos."
                    elif lugar == 'Oficina':
                        Pista2 = False
                        Pista3 = True
                        text = "                           Pista 3: Lugar de crimen\n Después de la muerte de Klaus se buscó donde fue asesinado. \n- Sala:\n       Estaba todo en orden.\n- Bar:\n-     El que despacha las botellas estaba ahí\n- Oficina:\n          Estaba abierta la puerta.\n- Habitación: \n             Estaba cerrada con llave.\n- Recibidor:\n            La abogada estaba ahí esperando a papá. \n\n   NOTA:\n       Después de contestas las preguntas de abajo presiona\n SIGUIENTE para verificar tus respuestas con la base de datos."
                    elif lugar == 'Habitacion':
                        Pista2 = False
                        Pista3 = True
                        text = "                           Pista 3: Lugar de crimen\n Después de la muerte de Klaus se buscó donde fue asesinado.\n- Sala:\n       Mamá la estaba limpiando ya que iba a ver una fiesta.\n- Bar:\n-     Mamá la estaba limpiando ya que iba a ver una fiesta.\n- Oficina:\n          Papá la cerro con llave desde días antes.\n- Habitación:\n             Todo estaba desordenado.\n- Recibidor:\n            La cámara no grabo nada.\n\n   NOTA:\n       Después de contestas las preguntas de abajo presiona\n SIGUIENTE para verificar tus respuestas con la base de datos."
                    elif lugar == 'Recibidor':
                        Pista2 = False
                        Pista3 = True
                        text = "                           Pista 3: Lugar de crimen\n Después de la muerte de Klaus se buscó donde fue asesinado. \n- Sala:\n       Five del futuro estaba ahí.\n- Bar:\n-     Se encontró todo en orden.\n- Oficina:\n          Papá trabajo todo el día ahí.\n- Habitación: \n             Mamá estaba limpiando.\n- Recibidor:\n            Se encontró el arma ahí.\n\n   NOTA:\n       Después de contestas las preguntas de abajo presiona\n SIGUIENTE para verificar tus respuestas con la base de datos."                                                                                

        max_lines = TEXTAREA_ALTO // font.get_linesize()
        start_line = max(0, min(-scroll_y // font.get_linesize(), len(lines) - max_lines))
        end_line = min(len(lines), start_line + max_lines)

        for i in range(start_line, end_line):
            line_surface = font.render(lines[i], True, NEGRO)
            ventana.blit(line_surface, (textarea_rect.x + 5, textarea_rect.y + 5 + (i - start_line) * font.get_linesize()))

        # Draw scrollbar
        draw_scrollbar(ventana, scroll_y, textarea_rect, lines, font)

        
        pygame.display.flip()

# Llamar a la función para abrir la ventana
abrir_ventana()
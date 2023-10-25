# RETO 33: TETRIS
# https://retosdeprogramacion.com/semanales2023
# https://www.youtube.com/watch?v=3UCZltG8iCY

# CONTINUAR AQUÍ: https://youtu.be/3UCZltG8iCY?t=2834

'''
 Crea un programa capaz de gestionar una pieza de Tetris.
 - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
   🔳
   🔳🔳🔳
 - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla de juego.
 - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 - Debes tener en cuenta los límites de la pantalla de juego.
'''

# Importaciones:
from enum import Enum

# ------------------------------------------------------------- 
# Clase "Movement" para definir los 4 movimientos. 
class Movement(Enum):
  DOWN = 1
  RIGHT = 2
  LEFT = 3
  ROTATE = 4
  
# ------------------------------------------------------------- 
# Función principal:
def tetris():
  
  screen = [["🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"]]
  
  print_screen(screen)
  
  # Inicializamos el estado de rotacion:
  rotation = 0
  
  # Movimientos de test:
  # screen = move_piece(screen, Movement.DOWN, rotation)
  # screen = move_piece(screen, Movement.DOWN, rotation)
  # screen = move_piece(screen, Movement.DOWN, rotation)
  # screen = move_piece(screen, Movement.RIGHT, rotation)
  (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)
  # ------------------------------------------------------------- 

def move_piece (screen:list,  movement:Movement, rotation:int) -> (list, int):
  
  # Partimos de una pantalla en blanco:
  new_screen = [["🔲"] * 10 for _ in range(10)]
  #print_screen(white_screen)
  
  
  # Variables para la rotación:
  rotation_item = 0 # Valor inicial.
  # Patrones de rotacion (horaria) para cada una de las 4 piezas negras.
  # Partimos de la posición inicial y calculamos cuánto se tendría que mover cada pieza:
  rotations = [[(0,0), (0,0), (0,0), (0,0)],  # Posición inicial.
               [(0,1), (-1,0), (0,-1), (1,-2)], # 90° derecha.
               [(0,2), (1,1), (-1,1), (-2,0)], # 180°.
               [(0,1), (-1,0), (0,-1), (1,-2)]] # 270°.
  
  new_rotation = rotation
  if movement is Movement.ROTATE:
    new_rotation = 0 if rotation == 3 else rotation + 1            
  
  
  
  for row_index, row in enumerate(screen): # Recorremos los índices de la matriz.
    for column_index, item in enumerate(row): # Recorremos los indices de la fila.
      if item == "🔳":
        # Valores iniciales de nuevas coordenadas:
        new_row_index = 0
        new_col_index = 0
        # Hacemos un "switch" de los 4 tipos de movimiento:
        match movement:
          case Movement.DOWN:
            new_row_index = row_index + 1
            new_col_index = column_index
          case Movement.RIGHT:
            new_row_index = row_index
            new_col_index = column_index + 1
          case Movement.LEFT:
            new_row_index = row_index
            new_col_index = column_index - 1
          case Movement.ROTATE:
            new_row_index = row_index + rotations[new_rotation][rotation_item][0]
            new_col_index = column_index + rotations[rotation_item][1]
            rotation_item += 1
                
        # Pintamos de negro las nuevas coordenadas en la pantalla blanca:
        # Teniendo en cuenta los límites:
        if new_row_index > 9 or new_col_index > 9 or new_col_index < 0:
          print("\Movimiento inválido\n")
          return (screen, rotation)
        else:
          new_screen[new_row_index][new_col_index] = "🔳"
  
  # Pintamos y devolvemos la nueva pantalla:
  print_screen(new_screen)
  return (new_screen, new_rotation)
  
# -------------------------------------------------------------
# Pinta en pantalla un screen de 10 x 10 cuadritos:
def print_screen (screen:list):
  print("\nPANTALLA TETRIS\n")
  for row in screen:
    print ("".join(row))
# -------------------------------------------------------------
    
# Lanzamos el programa:
tetris()
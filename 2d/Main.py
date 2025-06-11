import copy

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)

class Rectangle:
    def __init__(self, width: float, height: float, position: Point = Point(0, 0)):
        self.width = width
        self.height = height
        self.position = position  # Coin inférieur gauche
    
    def top_left(self) -> Point:
        """Retourne la position du coin supérieur droit du rectangle."""
        return Point(self.x, self.y + self.height)
    def top_right(self) -> Point:
        """Retourne la position du coin supérieur droit du rectangle."""
        return Point(self.x + self.width, self.y + self.height)

    def bottom_right(self) -> Point:
        """Retourne la position du coin inférieur droit du rectangle."""
        return Point(self.x + self.width, self.y)
    
    # obtenir les 3 coordonnees x et y du rectangle, (on ne prend pas en compte le cote bas et gauche alors)
    # en partant d'une coordonnee x et y du coin bas gauche
    def get_coordinates(self) -> list[Point]:
        """Retourne les 3 coordonnées du rectangle (coin supérieur droit, coin supérieur gauche, coin inférieur droit)."""
        return [
            self.top_left(),
            self.top_right(),  # Coin supérieur droit
            self.bottom_right()  # Coin inférieur droit
        ]
        
    @property
    def x(self):
        return self.position.x
    
    @property
    def y(self):
        return self.position.y
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, position={self.position})"

class Bin(Rectangle):
    def __init__(self, width: float, height: float):
        super().__init__(width, height)
        self.rectangles = []
        self.slots = []  # Liste des emplacements disponibles
        self.slots.append(Point(0, 0))  # Ajouter l'origine comme premier emplacement
    
    def add_rectangle(self, rectangle: Rectangle):
        # Verifier d'abord si le rectangle peut etre place, ensuite choisi la position la plus optimale
        # Le rectangle doit occuper un emplacement valide dans le bin
        # Pour l'instant, on prend la premiere place disponible
        rectanglePlace = False
        for slot in self.slots:
            if self.can_place_rectangle(rectangle, slot):
                rectangle.position = slot
                self.slots.remove(slot)
                # on ajoute les nouveaux emplacements disponibles avec les 3 autres coins du rectangle qu'on vient de placer
                self.rectangles.append(rectangle)
                self.add_new_slots(rectangle)
                rectanglePlace = True
                break
        if rectanglePlace: print("rectangle ajouté à la position:", rectangle.position)
        else: print("rectangle non ajouté, pas de place disponible")
        
    # Retourne des copies de ce bin en ajoutant un rectangle au nombre de place dispo
    def add_rectangle_get_copies(self, rectangle: Rectangle):
        result = []
        for slot in self.slots:
            if self.can_place_rectangle(rectangle, slot):
                bin = copy.deepcopy(self)
                newRect = copy.deepcopy(rectangle)
                newRect.position = copy.deepcopy(slot)
                # on ajoute les nouveaux emplacements disponibles avec les 3 autres coins du rectangle qu'on vient de placer
                bin.rectangles.append(newRect)
                bin.add_new_slots(newRect)
                result.append(bin)
        return result
    
    # on ajoute les nouveaux emplacements disponibles avec les 3 autres coins du rectangle qu'on vient de placer
    def add_new_slots(self, rectangle: Rectangle):
        if rectangle not in self.rectangles:
            return
        self.slots.append(rectangle.top_left())  # Coin inférieur droit
        self.slots.append(rectangle.bottom_right())  # Coin inférieur droit
        self.slots.append(rectangle.top_right())  # Coin inférieur droit
        
    # verifier si pour une position donnee, le rectangle peut etre place dans le bin
    def can_place_rectangle(self, rectangle: Rectangle, position: Point) -> bool:
        """Vérifie si le rectangle peut être placé à la position donnée."""
        if not self.is_within_bin(rectangle, position):
            return False
        return self.is_valid_placement(rectangle, position)
    
    # Verifie si le rectangle est dans les limites du bin
    def is_within_bin(self, rect: Rectangle, position: Point) -> bool:
        return ( 0 <= position.x and 0 <= position.y and position.x + rect.width <= self.width and position.y + rect.height <= self.height )       
         
    # verifier si le rectangle ne collide pas avec les autres rectangles deja places
    def is_valid_placement(self, rect: Rectangle, position: Point) -> bool:
        """Vérifie si le placement est valide (pas de collisions)"""
        test_rect = Rectangle(rect.width, rect.height, position)
        
        for existing_rect in self.rectangles:
            if self.check_collision(test_rect, existing_rect):
                return False
        return self.is_within_bin(rect, position)
    
    @staticmethod
    def check_collision(rect1: Rectangle, rect2: Rectangle) -> bool:
        """Vérifie si deux rectangles se chevauchent"""
        return not (
            rect1.x + rect1.width <= rect2.x or
            rect2.x + rect2.width <= rect1.x or
            rect1.y + rect1.height <= rect2.y or
            rect2.y + rect2.height <= rect1.y
        )
    
    @property
    def getSlots(self):
        return self.slots   
    
    def __str__(self):
        rects_str = '\n'.join(str(r) for r in self.rectangles)
        return f"Bin(size={self.width}x{self.height}):\n{rects_str}"

# Ajouter une liste de rectangles dans un seul bin
# Juste pour illustrer
def pack_rectangles(bin : Bin, rectangles: list[Rectangle]):
    result = []
    result.append(bin)
    for i in range(len(rectangles)):
        # Pour chaque bin, ajouter le prochain rectangle avec l'index i
        length = len(result)
        for j in range(length):
            binChild = result[0].add_rectangle_get_copies(rectangles[i])
            result.extend(binChild)  
            result.pop(0)
    return result

# Ajouter un rectangle a un bin, et retourner toutes les possibilites
def pack_rectangle(bin : Bin, rectangle: Rectangle):
    result = result[0].add_rectangle_get_copies(rectangle)
    return result

bin = Bin(5, 5)
listRect = []
rect1 = Rectangle(2, 2)
rect2 = Rectangle(2, 3)
rect3 = Rectangle(3, 3)
rect4 = Rectangle(3, 1)
listRect.append(rect1)
listRect.append(rect2)
listRect.append(rect3)
listRect.append(rect4)

result = pack_rectangles(bin, listRect)
print("result = ")
for r in result:
    print("\nBIN")
    print(r.__str__())
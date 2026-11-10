import copy

# Paso 1. Creamos la clase con método clone:
class PromoBanner:
    def __init__(self, title, text, discount):
        self.title = title
        self.text = text
        self.discount = discount

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"[{self.title}] {self.text} ({self.discount}% off)"


# Paso 2. Creamos un “prototipo” y lo clonamos:
base_promo = PromoBanner(
    title="Promo de la semana",
    text="Café + croissant",
    discount=20
)

# Clonamos y personalizamos para el lunes
promo_lunes = base_promo.clone()
promo_lunes.title = "Lunes de energía"

# Clonamos y personalizamos para el viernes
promo_viernes = base_promo.clone()
promo_viernes.discount = 30

# Mostramos los resultados
print(base_promo)
print(promo_lunes)
print(promo_viernes)

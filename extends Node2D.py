extends Node2D

# Cargamos las imágenes de los corazones
var heart_full = preload("res://heart_full.png")
var heart_empty = preload("res://heart_empty.png")

# Configuración de la vida
var max_health = 5
var current_health = 3

func _ready():
    actualizar_barra_vida()

func actualizar_barra_vida():
    var contenedor = $HBoxContainer
    contenedor.clear()  # Limpiamos corazones anteriores

    for i in range(max_health):
        var corazon = TextureRect.new()
        corazon.texture = i < current_health ? heart_full : heart_empty
        corazon.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
        contenedor.add_child(corazon)

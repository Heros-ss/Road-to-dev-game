extends TextureProgressBar
var maxValor:int 
func _ready():
	maxValor=150
func disminuirVida(damage):
	value-=damage
	if value <=0:
		get_tree().get_nodes_in_group("jugador")[0].muerte()

extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_popup_menu_index_pressed(index: int) -> void:
	print("Pop Up Menu - My Menu, ", str(index))


func _on_popup_menu_2_index_pressed(index: int) -> void:
	print("Pop Up Menu - Project, ", str(index))


func _on_button_1_pressed() -> void:
	var Box = $VBoxContainer2/ColorRect
	Box.color = Color(1,2,3)


func _on_button_2_pressed() -> void:
	var Box = $VBoxContainer2/ColorRect
	Box.color = Color(3.0, 0.558, 0.468, 1.0)


func _on_button_3_pressed() -> void:
	var Box = $VBoxContainer2/ColorRect
	Box.color = Color(1.133, 0.552, 0.0, 1.0)


func _on_button_4_pressed() -> void:
	var Box = $VBoxContainer2/ColorRect
	Box.color = Color(0.974, 0.331, 0.0, 1.0)


func _on_button_5_pressed() -> void:
	var Box = $VBoxContainer2/ColorRect
	Box.color = Color(0.807, 0.117, 0.0, 1.0)

func _on_button_6_pressed() -> void:
	var Box = $VBoxContainer2/ColorRect
	Box.color = Color(0.0, 0.0, 0.0, 1.0)

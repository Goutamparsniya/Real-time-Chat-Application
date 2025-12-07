def get_guitar_model(guitar_type, guitar_color):
    guitar_models = {
        "acoustic": {
            "black": "ACO1001",
            "brown": "ACO2002",
            "natural": "ACO3003"
        },
        "electric": {
            "red": "ELE1004",
            "blue": "ELE2005",
            "black": "ELE3006"
        },
        "bass": {
            "sunburst": "BAS1007",
            "white": "BAS2008",
            "black": "BAS3009"
        }
    }
    guitar_type = guitar_type.lower()
    guitar_color = guitar_color.lower()
    model_number = guitar_models.get(guitar_type, {}).get(guitar_color, None)
    return model_number
guitar_type = input("Enter the type of guitar (acoustic/electric/bass): ")
guitar_color = input("Enter the color of the guitar: ")
model_number = get_guitar_model(guitar_type, guitar_color)
if model_number is not None:
    print(f"The model number for the {guitar_color} {guitar_type} guitar is {model_number}.")
else:
    print("Invalid guitar type or color.")

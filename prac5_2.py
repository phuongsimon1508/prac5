Colour_Code = {"AliceBlue": "#f0f8ff", "blue1": "#0000ff", "AntiqueWhite4": "#8b8378", "black": "#000000",
               "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc"}
# print(STATE_NAMES)

color = input("Enter name of the colour : ").upper()
while color != "":
    if color in Colour_Code:
        print(color, "is", Colour_Code[color])
    else:
        print("Invalid short colour")
    color = input("Enter name of the colour : ")
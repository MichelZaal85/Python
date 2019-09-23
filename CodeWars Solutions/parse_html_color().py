# Write a function which takes a color as a string and returns the parsed color as a map (see Examples).

# The input string represents one of the following:

# 6-digit hexadecimal - "#RRGGBB"
# e.g. "#012345", "#789abc", "#FFA077"
# Each pair of digits represents a value of the channel in hexadecimal: 00 to FF

# 3-digit hexadecimal - "#RGB"
# e.g. "#012", "#aaa", "#F5A"
# Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.

# Preset color name
# e.g. "red", "BLUE", "LimeGreen"
# You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby)
# The keys are the names of preset colors in lower-case and the values are the 
# corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").


# Examples:
# parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
# parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
# parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }


def parse_html_color(color):
	PRESET_COLORS = {'lemonchiffon': '#fffacd', 'mediumorchid': '#ba55d3', 'indigo': '#4b0082', 'linen': '#faf0e6', 'plum': '#dda0dd', 'darkorange': '#ff8c00', 'turquoise': '#40e0d0', 'darksalmon': '#e9967a', 'purple': '#800080', 'gray': '#808080', 'grey': '#808080', 'lightpink': '#ffb6c1', 'lightgrey': '#d3d3d3', 'ghostwhite': '#f8f8ff', 'saddlebrown': '#8b4513', 'crimson': '#dc143c', 'mediumvioletred': '#c71585', 'mediumspringgreen': '#00fa9a', 'slategrey': '#708090', 'dimgrey': '#696969', 'orangered': '#ff4500', 'slategray': '#708090', 'snow': '#fffafa', 'lightblue': '#add8e6', 'lightgreen': '#90ee90', 'bisque': '#ffe4c4', 'gold': '#ffd700', 'darkgrey': '#a9a9a9', 'paleturquoise': '#afeeee', 'whitesmoke': '#f5f5f5', 'dodgerblue': '#1e90ff', 'darkolivegreen': '#556b2f', 'blueviolet': '#8a2be2', 'tomato': '#ff6347', 'rebeccapurple': '#663399', 'mintcream': '#f5fffa', 'darkblue': '#00008b', 'darkslateblue': '#483d8b', 'darkmagenta': '#8b008b', 'lightgray': '#d3d3d3', 'lightseagreen': '#20b2aa', 'lightskyblue': '#87cefa', 'peachpuff': '#ffdab9', 'silver': '#c0c0c0', 'sandybrown': '#f4a460', 'floralwhite': '#fffaf0', 'aliceblue': '#f0f8ff', 'antiquewhite': '#faebd7', 'indianred': '#cd5c5c', 'beige': '#f5f5dc', 'powderblue': '#b0e0e6', 'darkorchid': '#9932cc', 'darkgreen': '#006400', 'darkseagreen': '#8fbc8f', 'brown': '#a52a2a', 'chocolate': '#d2691e', 'dimgray': '#696969', 'peru': '#cd853f', 'darkslategray': '#2f4f4f', 'lightgoldenrodyellow': '#fafad2', 'lightsalmon': '#ffa07a', 'aqua': '#00ffff', 'gainsboro': '#dcdcdc', 'darkgray': '#a9a9a9', 'seashell': '#fff5ee', 'hotpink': '#ff69b4', 'skyblue': '#87ceeb', 'wheat': '#f5deb3', 'salmon': '#fa8072', 'lawngreen': '#7cfc00', 'springgreen': '#00ff7f', 'papayawhip': '#ffefd5', 'navajowhite': '#ffdead', 'lime': '#00ff00', 'slateblue': '#6a5acd', 'mistyrose': '#ffe4e1', 'lightsteelblue': '#b0c4de', 'mediumslateblue': '#7b68ee', 'darkred': '#8b0000', 'cyan': '#00ffff', 'steelblue': '#4682b4', 'cornsilk': '#fff8dc', 'palegreen': '#98fb98', 'ivory': '#fffff0', 'magenta': '#ff00ff', 'orange': '#ffa500', 'azure': '#f0ffff', 'blanchedalmond': '#ffebcd', 'midnightblue': '#191970', 'darkcyan': '#008b8b', 'greenyellow': '#adff2f', 'goldenrod': '#daa520', 'limegreen': '#32cd32', 'seagreen': '#2e8b57', 'olivedrab': '#6b8e23', 'green': '#008000', 'lightcoral': '#f08080', 'pink': '#ffc0cb', 'mediumturquoise': '#48d1cc', 'blue': '#0000ff', 'firebrick': '#b22222', 'mediumblue': '#0000cd', 'mediumaquamarine': '#66cdaa', 'honeydew': '#f0fff0', 'forestgreen': '#228b22', 'fuchsia': '#ff00ff', 'mediumpurple': '#9370db', 'lightyellow': '#ffffe0', 'oldlace': '#fdf5e6', 'red': '#ff0000', 'lightslategray': '#778899', 'coral': '#ff7f50', 'navy': '#000080', 'cornflowerblue': '#6495ed', 'olive': '#808000', 'palevioletred': '#db7093', 'aquamarine': '#7fffd4', 'deeppink': '#ff1493', 'yellowgreen': '#9acd32', 'lightcyan': '#e0ffff', 'darkslategrey': '#2f4f4f', 'maroon': '#800000', 'khaki': '#f0e68c', 'cadetblue': '#5f9ea0', 'lavender': '#e6e6fa', 'palegoldenrod': '#eee8aa', 'black': '#000000', 'rosybrown': '#bc8f8f', 'thistle': '#d8bfd8', 'teal': '#008080', 'darkturquoise': '#00ced1', 'sienna': '#a0522d', 'tan': '#d2b48c', 'darkviolet': '#9400d3', 'deepskyblue': '#00bfff', 'white': '#ffffff', 'orchid': '#da70d6', 'lavenderblush': '#fff0f5', 'lightslategrey': '#778899', 'darkkhaki': '#bdb76b', 'violet': '#ee82ee', 'darkgoldenrod': '#b8860b', 'yellow': '#ffff00', 'mediumseagreen': '#3cb371', 'burlywood': '#deb887', 'royalblue': '#4169e1', 'moccasin': '#ffe4b5', 'chartreuse': '#7fff00'}

	if color[0] != '#':
		return parse_into_dict(PRESET_COLORS[color.lower()])
	if len(color) > 3:
		pass

def parse_into_dict(hexa):
	number = [hexa[i:i+2] for i in range(1, len(hexa), 2)]
	return {'r': number[0], 'g': number[1], 'b': number[2]}


print(parse_html_color('limegreen'))
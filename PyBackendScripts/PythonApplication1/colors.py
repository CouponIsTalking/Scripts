if 1:
	colors = {}
	
	colors["AntiqueWhite"] = 1
	colors["Aqua"] = 1
	colors["Aquamarine"] = 1
	colors["Azure"] = 1
	colors["Beige"] = 1
	colors["Bisque"] = 1
	colors["Black"] = 1
	colors["BlanchedAlmond"] = 1
	colors["Blue"] = 1
	colors["BlueViolet"] = 1
	colors["Brown"] = 1
	colors["BurlyWood"] = 1
	colors["CadetBlue"] = 1
	colors["Chartreuse"] = 1
	colors["Chocolate"] = 1
	colors["Coral"] = 1
	colors["CornflowerBlue"] = 1
	colors["Cornsilk"] = 1
	colors["Crimson"] = 1
	colors["Cyan"] = 1
	colors["DarkBlue"] = 1
	colors["DarkCyan"] = 1
	colors["DarkGoldenrod"] = 1
	colors["DarkGray"] = 1
	colors["DarkGreen"] = 1
	colors["DarkKhaki"] = 1
	colors["DarkMagenta"] = 1
	colors["DarkOliveGreen"] = 1
	colors["DarkOrange"] = 1
	colors["DarkOrchid"] = 1
	colors["DarkRed"] = 1
	colors["DarkSalmon"] = 1
	colors["DarkSeaGreen"] = 1
	colors["DarkSlateBlue"] = 1
	colors["DarkSlateGray"] = 1
	colors["DarkTurquoise"] = 1
	colors["DarkViolet"] = 1
	colors["DeepPink"] = 1
	colors["DeepSkyBlue"] = 1
	colors["DimGray"] = 1
	colors["DodgerBlue"] = 1
	colors["FireBrick"] = 1
	colors["FloralWhite"] = 1
	colors["ForestGreen"] = 1
	colors["Fuchsia"] = 1
	colors["Gainsboro"] = 1
	colors["GhostWhite"] = 1
	colors["Gold"] = 1
	colors["Goldenrod"] = 1
	colors["Gray"] = 1
	colors["Green"] = 1
	colors["GreenYellow"] = 1
	colors["Honeydew"] = 1
	colors["HotPink"] = 1
	colors["IndianRed"] = 1
	colors["Indigo"] = 1
	colors["Ivory"] = 1
	colors["Khaki"] = 1
	colors["Lavender"] = 1
	colors["LavenderBlush"] = 1
	colors["LawnGreen"] = 1
	colors["LemonChiffon"] = 1
	colors["LightBlue"] = 1
	colors["LightCoral"] = 1
	colors["LightCyan"] = 1
	colors["LightGoldenrodYellow"] = 1
	colors["LightGreen"] = 1
	colors["LightGrey"] = 1
	colors["LightPink"] = 1
	colors["LightSalmon"] = 1
	colors["LightSeaGreen"] = 1
	colors["LightSkyBlue"] = 1
	colors["LightSlateGray"] = 1
	colors["LightSteelBlue"] = 1
	colors["LightYellow"] = 1
	colors["Lime"] = 1
	colors["LimeGreen"] = 1
	colors["Linen"] = 1
	colors["Magenta"] = 1
	colors["Maroon"] = 1
	colors["MediumAquamarine"] = 1
	colors["MediumBlue"] = 1
	colors["MediumOrchid"] = 1
	colors["MediumPurple"] = 1
	colors["MediumSeaGreen"] = 1
	colors["MediumSlateBlue"] = 1
	colors["MediumSpringGreen"] = 1
	colors["MediumTurquoise"] = 1
	colors["MediumVioletRed"] = 1
	colors["MidnightBlue"] = 1
	colors["MintCream"] = 1
	colors["MistyRose"] = 1
	colors["Moccasin"] = 1
	colors["NavajoWhite"] = 1
	colors["Navy"] = 1
	colors["OldLace"] = 1
	colors["Olive"] = 1
	colors["OliveDrab"] = 1
	colors["Orange"] = 1
	colors["OrangeRed"] = 1
	colors["Orchid"] = 1
	colors["PaleGoldenrod"] = 1
	colors["PaleGreen"] = 1
	colors["PaleTurquoise"] = 1
	colors["PaleVioletRed"] = 1
	colors["PapayaWhip"] = 1
	colors["PeachPuff"] = 1
	colors["Peru"] = 1
	colors["Pink"] = 1
	colors["Plum"] = 1
	colors["PowderBlue"] = 1
	colors["Purple"] = 1
	colors["Red"] = 1
	colors["RosyBrown"] = 1
	colors["RoyalBlue"] = 1
	colors["SaddleBrown"] = 1
	colors["Salmon"] = 1
	colors["SandyBrown"] = 1
	colors["SeaGreen"] = 1
	colors["Seashell"] = 1
	colors["Sienna"] = 1
	colors["Silver"] = 1
	colors["SkyBlue"] = 1
	colors["SlateBlue"] = 1
	colors["SlateGray"] = 1
	colors["Snow"] = 1
	colors["SpringGreen"] = 1
	colors["SteelBlue"] = 1
	colors["Tan"] = 1
	colors["Teal"] = 1
	colors["Thistle"] = 1
	colors["Tomato"] = 1
	colors["Turquoise"] = 1
	colors["Violet"] = 1
	colors["Wheat"] = 1
	colors["White"] = 1
	colors["WhiteSmoke"] = 1
	colors["Yellow"] = 1
	colors["YellowGreen"] = 1
	
	pcolors = {}
	for s in colors:
		i = 1
		c = s
		while i < len(s):
			#print str(i)
			if s[i] >= 'A' and s[i] <= 'Z':
				c = s[:i] + " "+ s[i:]
			i = i+1
		pcolors[c.lower()] = 1
		
	for x in pcolors:
		print "colors[\""+x+"\"] = 1"
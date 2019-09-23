# (['body','head','tail'])
def fix_the_meerkat(arr):
	chk = {'head':0,'body':1,'tail':2}
	fixed = []
	try:
		for i in arr:
			if chk[i]:
				fixed.insert(chk[i],i)
	except:
		return False
	return fixed


print(fix_the_meerkat(["tail", "body", "head"])) 				# ["head", "body", "tail"]

print(fix_the_meerkat(["tails", "body", "heads"])) 				# ["heads", "body", "tails"]
print(fix_the_meerkat(["bottom", "middle", "top"]))				# ["top", "middle", "bottom"]
print(fix_the_meerkat(["lower legs", "torso", "upper legs"])) 	# ["upper legs", "torso", "lower legs"]
print(fix_the_meerkat(["ground", "rainbow", "sky"])) 			# ["sky", "rainbow", "ground"]
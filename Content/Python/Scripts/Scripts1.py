import unreal

#NOTE:Ensure you use Scripts1.FUNCTIONNAME when calling functions from this script

def FindAndReplace(StartString:str, FindText:str,ReplaceText:str):
	"""Finds and replace text within a string, not case sensitive

	Args:
		StartString (str): Unmodified string
		FindText (str): Text to find in StartString
		ReplaceText (str): Text to replace once found

	Returns:
		OutText (str): Modified Text
	"""

	OutText = unreal.StringLibrary().replace(StartString, FindText, ReplaceText)

	return OutText
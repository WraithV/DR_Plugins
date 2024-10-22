import unreal

from Scripts import Scripts1

def GetSelectedUAssets():
	"""Returns list of selected content browser objects

	Returns:
		SelectedAssets (List[Unreal.Object]): Selected Content browser assets
	"""
	SelectedAssets:list[unreal.Object] = []


	SelectedAssets += unreal.EditorUtilityLibrary.get_selected_assets()

	if len(SelectedAssets) < 0:
		print(f"No Content Browser Assets selected")

	return SelectedAssets


def RenameAssets (FindText:str, ReplaceText:str):
	"""Renames selected content browser assets using find and replace, not case sensitive

	Args:
		FindText (str): Text to find
		ReplaceText (str): Text to replace
	"""
	SelectedAssets = GetSelectedUAssets()

	NumModified: int = 0
	NumSkipped: int = 0

	total_frames = 1000
	text_label = "Renaming Assets"
	with unreal.ScopedSlowTask(total_frames, text_label) as slow_task: #with statement automatically initialises before and cleans up after the function
		slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already
		for asset in SelectedAssets:
			if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
				break
			slow_task.enter_progress_frame(1)     # Advance progress by one frame.
													# You can also update the dialog text in this call, if you want.
			AssetPath = unreal.Paths.get_path(asset.get_path_name())
			OldName = unreal.Paths.get_base_filename(asset.get_path_name())

			NewName = Scripts1.FindAndReplace(OldName, FindText, ReplaceText)

			if NewName == OldName:
				print(f"Unable to update {asset.get_name()}, {FindText} not found. Skipping")
				NumSkipped += 1
				continue

			OldAssetPath = AssetPath + "/" + OldName
			NewAssetPath = AssetPath + "/" + NewName

			unreal.EditorAssetLibrary.rename_asset(OldAssetPath ,NewAssetPath)

			NumModified += 1

		print(f"Find and Replace Complete: Modified {NumModified} assets, {NumSkipped} assets skipped")
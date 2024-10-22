import unreal

from Scripts import Scripts1

def GetSelectedActors():
	"""Returns list of selected world Actors

	Returns:
		SelectedActors (List[Unreal.Actor]): Selected Actors
	"""
	SelectedActors:list[unreal.Actor] = []


	SelectedActors += unreal.EditorActorSubsystem.get_selected_level_actors(unreal.EditorActorSubsystem())

	if len(SelectedActors) < 0:
		print(f"No Actors selected")

	return SelectedActors

def FindAndReplaceActorLabels(FindText:str, ReplaceText:str):
	"""Renames actors using find and replace, use * to batch rename actors

	Args:
		FindText (str): Text to find in Actor Label, not case sensitive
		ReplaceText (str): New text for Actor Label
	"""

	SelectedActors:list[unreal.Actor] = GetSelectedActors()

	NumModified: int = 0
	NumSkipped: int = 0

	total_frames = 1000
	text_label = "Renaming Actors"
	with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
		slow_task.make_dialog(True)					# Makes the dialog visible, if it isn't already

		for actor in SelectedActors:
			if slow_task.should_cancel():			# True if the user has pressed Cancel in the UI
				break
			slow_task.enter_progress_frame(1)		# Advance progress by one frame.
													# You can also update the dialog text in this call, if you want.

			OldName:str = actor.get_actor_label()
			NewName:str = ""

			if FindText == "*":
				NewName = ReplaceText + "_" + str(NumModified + 1)
			else:
				NewName = Scripts1.FindAndReplace(OldName, FindText, ReplaceText)

			if NewName == OldName:
				print(f"Unable to update {OldName}, {FindText} not found. Skipping")
				NumSkipped += 1
				continue

			actor.set_actor_label(NewName)

			NumModified += 1

		print(f"Find and Replace Complete: Modified {NumModified} actors, {NumSkipped} actors skipped")
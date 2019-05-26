def confirm():
	yes = {'yes','y', 'ye', ''}
	no = {'no','n'}
	choice = input("Do you want to Download? [Yes/No]: ").lower()
	if choice in yes:
		print(">>> Starting Download!")
		return True
	elif choice in no:
		print("<<< Download Cancelled!")
		return False
	else:
		print("Please respond with 'yes' or 'no'")
		confirm()
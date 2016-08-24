on run argv
	set message to item 1 of argv
	tell application "System Events"
		set frontAppName to name of first application process whose frontmost is true
	end tell
	if frontAppName is not "Python" then
		display notification message with title "Connect" sound name "Glass"
	end if
	#return frontAppName
end run

## PsychoPy keypress exercises
1. Please see 
2. Moving 'event.clearEvents' would have a major effect on the outcome. If you were to put it lower in the script, such as under 'keys' it would just clear the keys you just collected. If you were to remove an indent from the 'if keys:' section, it would run through the 2 seconds getting keys the whole time, only after that will it execute the 'if keys:' statement. That is incorrect, it needs to count each time a key is added, not just the one time a key gets added at the end of two seconds 
##

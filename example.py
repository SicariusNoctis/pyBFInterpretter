import BFInterpretter

# Example 1

output_text = BFInterpretter.execute("""
	++++++++			loop 8 times
	[
		>+++++++++		increment by 9
		<-
	]
	>.					print H = 8 * 9
	,.					print i
	,.					print !
""", "i!")

print(output_text)

# Example 2

output_text = BFInterpretter.execute("""
	+++					loop 3 times
	[
		>++++			loop 4 times
		[
			>++++++		increment by 6
			<-
		]
		<-
	]
	>>.					print H = 3 * 4 * 6
	+.					print I = 3 * 4 * 6 + 1
	,.					print !
	,.					print space
	,.					print :
	,.					print )
""", "! :)")

print(output_text)

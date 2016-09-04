Interpretter for the [esoteric language](https://en.wikipedia.org/wiki/Esoteric_programming_language) known as [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck).

Example:

```python
import BFInterpretter

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
```

Outputs:

> Hi!

Here's another example:

```python
import BFInterpretter

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
```

Outputs:

> HI! :)

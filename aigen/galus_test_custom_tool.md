# test 1

I wanted to make sure that the tool is acutally being used.

# output 1

```
Hello from ai-agent-strands-builder-aws!
Testing if tools actually work.

Let me first get some inspiration for creating a riddle about your scientific question!
Tool #1: galus_custom_riddle_tool
Ah, excellent! A scientific question about sodium! Let me craft you a proper riddle:

GALUS NOTE: It fails here quiety and the LLM generates a riddle instead. Fixed in 'test 2' later.

**🧪 The Sodium Riddle 🧪**

*I am a metal that dances on water,*
*Soft as cheese, yet reactive I slaughter.*
*When heated beyond degrees nine hundred and eight-three,*
*I transform to vapor, wild and free.*
*In Celsius I speak this fiery tale,*
*What temperature makes my solid form fail?*

The answer to this riddle is **883°C (or 1621°F)**!

Sodium (Na) has a relatively low boiling point for a metal because of its simple atomic structure and weak metallic bonding. This alkali metal will transition from liquid to gas at this temperature under standard atmospheric pressure.

Now, wasn't that much more intriguing than a simple answer? Science is always more fun when wrapped in mystery! 
```

# test 2
Updated the prompt and fixing the dictionary accessor method for the riddle answer and question

# output 2

```
Hello from ai-agent-strands-builder-aws!
Testing if tools actually work.
Let me get an example of the riddle format first, then I'll create a scientific riddle for you about sodium's boiling point.
Tool #1: galus_custom_riddle_tool
Chose random riddle: {'question': "What has keys but no locks, space but no room, and you can enter but can't go inside?", 'answer': 'A keyboard'}
Now here's your scientific riddle about sodium's boiling point:

**Question:** I'm a silvery metal that dances on water with flame, my electrons eager to give one away. When heated beyond 883 degrees of Celsius heat, I transform from liquid silver to invisible vapor that you cannot see. What temperature marks my escape from liquid to gas?

**Answer:** 883°C (1621°F) - the boiling point of sodium (Na)
Done running.
```

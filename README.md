# 🧠 ReAgent — A Reasoning Agent with Dynamic Tool Use

**ReAgent** is a reasoning-first chatbot that uses the ReAct pattern to talk, think, and use tools (like a calculator, search, or Wikipedia) to help you intelligently.

## ✨ Features

- Chat like a normal AI
- Automatically uses tools _when needed_
- Built using the **ReAct** pattern (Thought → Action → Observation → Answer)
- Uses a **Router Agent** to intelligently delegate between specialized agents (Math or Research)
- Plug in your own tools easily

## 💡 Example

> You: "What's 42 squared minus the number of moons on Mars?"

> 🤖 ReAgent:
>
> ```
> Thought: I need to calculate 42 squared, then subtract the number of Mars moons.
> Action: Calculator(42^2)
> Observation: 1764
> Action: Wikipedia("moons of Mars")
> Observation: Mars has 2 moons.
> Thought: 1764 - 2 = 1762
> Final Answer: 1762
> ```

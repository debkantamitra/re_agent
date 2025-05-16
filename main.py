from agent.router_agent import create_router_agent

def run_chat():
    print("🤖 ReAgent (Multi-Agent Mode) is ready. Type 'exit' to quit.")
    router = create_router_agent()

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        
        response = router(user_input)
        print(f"\n🧠 ReAgent: {response}")

if __name__ == "__main__":
    run_chat()

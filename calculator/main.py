import os
from dotenv import load_dotenv 
from calculator.calculation import Calculation
from calculator.command_loader import CommandLoader

load_dotenv()

def repl():
    commands = CommandLoader.load_commands()
    print("Calculator REPL. Type 'menu' for options, 'exit' to quit.")
    
    while True:
        user_input = input("> ").strip()
        
        if user_input == "exit":
            break
        elif user_input == "menu":
            print(f"Available commands: {', '.join(commands.keys())}")
        elif user_input == "history":
            print(Calculation.get_history())
        else:
            parts = user_input.split()
            command_name = parts[0]
            arguments = map(float, parts[1:])
            
            if command_name in commands:
                command = commands[command_name]
                result = command.execute(*arguments)
                Calculation.add_to_history(command_name, tuple(arguments), result)
                print(f"Result: {result}")
            else:
                print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    repl()

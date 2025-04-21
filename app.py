import os
from rich.console import Console
from rich.panel import Panel
from rich.box import HEAVY

console = Console()

def file_exists(filepath):
    """Check if the file exists."""
    return os.path.isfile(filepath)

def search_text_file(filepath, keyword):
    """Search for the keyword in the text file and print matching paragraphs."""
    found = False
    context_lines = []

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        paragraph = []
        for line in file:
            if line.strip() == "":
                if paragraph:
                    if any(keyword.lower() in l.lower() for l in paragraph):
                        found = True
                        context_lines.append("\n".join(paragraph))
                    paragraph = []
            else:
                paragraph.append(line.strip())

        if paragraph:
            if any(keyword.lower() in l.lower() for l in paragraph):
                found = True
                context_lines.append("\n".join(paragraph))

    if found:
        for context in context_lines:
            console.print(Panel(context, title=f"📖 {os.path.basename(filepath)} — Answer", style="bold green", box=HEAVY))
    else:
        console.print(Panel(f"[bold red]No information found in {os.path.basename(filepath)} about '{keyword}'[/bold red]", title="Not Found", box=HEAVY))

def text_chatbot():
    """Chatbot function for interacting with the user and searching text files."""
    console.print(Panel("[bold cyan]Welcome! I'm your Text Data Chatbot 📚[/bold cyan]", title="TextBot", box=HEAVY))

    # List of file paths to search
    file_paths = [
       r"C:\Users\Ic\Desktop\Buzz Chatbot\most important chatbot 100gb answer\Albert_Einstein.txt",
       r"C:\Users\Ic\Desktop\Buzz Chatbot\most important chatbot 100gb answer\Portable_media_player.txt",
       r"C:\Users\Ic\Desktop\Buzz Chatbot\most important chatbot 100gb answer\Biology.txt",
       r"C:\Users\Ic\Desktop\Buzz Chatbot\most important chatbot 100gb answer\Brain.txt",
       r"C:\Users\Ic\Desktop\Buzz Chatbot\most important chatbot 100gb answer\bio12.txt"

    ]

    # Check if files exist
    existing_files = []
    for path in file_paths:
        if file_exists(path):
            existing_files.append(path)
            console.print(Panel(f"[bold green]{os.path.basename(path)} found and ready.[/bold green]", box=HEAVY))
        else:
            console.print(Panel(f"[bold red]{os.path.basename(path)} not found.[/bold red]", box=HEAVY))

    if not existing_files:
        console.print(Panel("[bold red]No valid files found. Exiting...[/bold red]", box=HEAVY))
        return

    while True:
        question = console.input("[bold magenta]🧑 You:[/bold magenta] ").strip()

        if question.lower() == 'exit':
            console.print(Panel("[bold cyan]Goodbye![/bold cyan] 👋", box=HEAVY))
            break
        elif question.lower() in ["developer", "who is your developer?", "what is your developer name?"]:
            console.print(Panel("[bold cyan]My developer is Rao Zain.[/bold cyan]", box=HEAVY))
        elif question:
            for file_path in existing_files:
                search_text_file(file_path, question)
        else:
            console.print(Panel("[bold red]❌ Please type a question.[/bold red]", box=HEAVY))

if __name__ == "__main__":
    text_chatbot()

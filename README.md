# $upershell
$upershell is a simple interactive shell for executing custom commands using a lightweight scripting language. It allows users to define variables, display messages, introduce delays, create and read from .ssh files, and clear console output.

# Features
Variable Definition: Use varconst to define variables in the format varconst=variable>value.

Text Output: Display messages with ctext('Your message here'), including variable substitutions.

Delay Execution: Introduce pauses using time.add('number_of_seconds') before executing subsequent commands.

File Management: Create new .ssh files with newfile filename.ssh and execute commands from existing files using openfile filename.ssh.

Clear Console: Use cclear to clear the console output.

Exit Shell: Type exit to close the shell.

# Example Usage
# Variables:
varconst=name>World

# Text:
ctext('Hello, $name$!')

# Time (in seconds)
time.add('5')'

# New file
newfile intro.ssh

#Open a file
openfile intro.ssh

# Everything:
varconst=greeting>Hello, User!

ctext('$greeting$')

time.add('3')

ctext('This message appears after a 3-second delay.')

# Thanks for checking
Clone the repository and run $upershell to start using this interactive shell for custom scripting and command execution.

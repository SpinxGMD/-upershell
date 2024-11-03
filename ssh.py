import re
import time  # Import time for delay functionality

def simple_python_shell():
    variables = {}  # Dictionary to store variables

    print("Welcome to the $upershell console! Type 'exit' to quit.")
    while True:
        user_input = input(">>> ")

        # Exit the shell
        if user_input.lower() == "exit":
            print("Exiting the shell.")
            break
        # Create a new file "main.ssh"
        elif user_input.lower() == "newfile":
            with open("main.ssh", "w") as f:
                f.write("# This is the main.ssh file\n")
            print("File 'main.ssh' created.")
        # Open and interpret "main.ssh"
        elif user_input.lower() == "openfile":
            try:
                with open("main.ssh", "r") as f:
                    for line in f:
                        line = line.strip()

                        # Check if there's a time delay
                        if line.startswith("time.add("):
                            match = re.match(r"time\.add\('(\d+)'\)", line)
                            if match:
                                delay_time = int(match.group(1))  # Set delay time in seconds
                                time.sleep(delay_time)  # Apply the delay

                        # Match varconst pattern: varconst=variable>value
                        elif line.startswith("varconst="):
                            match = re.match(r"varconst=(\w+)>(.+)", line)
                            if match:
                                variable_name = match.group(1)
                                variable_value = match.group(2)
                                variables[variable_name] = variable_value

                        # Match ctext pattern: ctext('Hello World')
                        elif line.startswith("ctext("):
                            match = re.match(r"ctext\('(.+?)'\)", line)
                            if match:
                                text = match.group(1)
                                # Replace any variables in the format $variable$
                                text = re.sub(r"\$(\w+)\$", lambda m: variables.get(m.group(1), ""), text)
                                print(text)
            except FileNotFoundError:
                print("File 'main.ssh' not found.")
        else:
            # Execute user-entered Python commands
            try:
                result = eval(user_input)
                if result is not None:
                    print(result)
            except SyntaxError:
                try:
                    exec(user_input)
                except Exception as e:
                    print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

# Run the shell
simple_python_shell()




#Welcome the code is split across various blocks from easy to challenging

"""import math

def calculate():
    history = []
    
    while True:
        print("\nScientific Calculator")
        print("1. Basic Operations (+, -, *, /)")
        print("2. Advanced Operations (^, %, sqrt)")
        print("3. Show History")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            print("Goodbye!")
            break
            
        if choice == '3':
            print("\nCalculation History:")
            for i, calc in enumerate(history, 1):
                print(f"{i}. {calc}")
            continue
            
        try:
            if choice in ('1', '2'):
                num1 = float(input('Enter first number: '))
                op = input('Enter operator: ')
                
                if op != 'sqrt':
                    num2 = float(input('Enter second number: '))
                
                if choice == '1':
                    if op == '+':
                        result = num1 + num2
                    elif op == '-':
                        result = num1 - num2
                    elif op == '*':
                        result = num1 * num2
                    elif op == '/':
                        result = num1 / num2 if num2 != 0 else "Undefined"
                    else:
                        print("Invalid operator for basic operations!")
                        continue
                else:  # choice == '2'
                    if op == '^':
                        result = num1 ** num2
                    elif op == '%':
                        result = num1 % num2
                    elif op == 'sqrt':
                        result = math.sqrt(num1)
                    else:
                        print("Invalid operator for advanced operations!")
                        continue
                
                expression = f"{num1} {op} {num2 if op != 'sqrt' else ''} = {result}"
                history.append(expression)
                print(f"Result: {result}")
                
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

calculate()"""



"""from tkinter import *
import math

memory = 0

def calculate():
    try:
        num1 = float(entry_num1.get())
        op = entry_op.get()
        
        if op not in ('sqrt', 'sin', 'cos', 'tan', 'log'):
            num2 = float(entry_num2.get())
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': result = num1 / num2 if num2 != 0 else "Undefined"
        elif op == '^': result = num1 ** num2
        elif op == '%': result = num1 % num2
        elif op == 'sqrt': result = math.sqrt(num1)
        elif op == 'log': result = math.log(num1, 10)
        elif op == 'sin': result = math.sin(math.radians(num1))
        elif op == 'cos': result = math.cos(math.radians(num1))
        elif op == 'tan': result = math.tan(math.radians(num1))
        else: result = "Invalid operator!"
        
        label_result.config(text=f"Result: {result}")
    except:
        label_result.config(text="Error: Invalid input!")

def memory_add():
    global memory
    memory += float(entry_num1.get())
    label_memory.config(text=f"Memory: {memory}")

def memory_recall():
    entry_num1.delete(0, END)
    entry_num1.insert(0, str(memory))

# GUI Setup
root = Tk()
root.title("Scientific Calculator")

Label(root, text="First Number:").grid(row=0, column=0)
entry_num1 = Entry(root)
entry_num1.grid(row=0, column=1)

Label(root, text="Operator:").grid(row=1, column=0)
entry_op = Entry(root)
entry_op.grid(row=1, column=1)

Label(root, text="Second Number:").grid(row=2, column=0)
entry_num2 = Entry(root)
entry_num2.grid(row=2, column=1)

Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

label_result = Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2)

Button(root, text="M+", command=memory_add).grid(row=5, column=0)
Button(root, text="MR", command=memory_recall).grid(row=5, column=1)

label_memory = Label(root, text="Memory: 0")
label_memory.grid(row=6, column=0, columnspan=2)

root.mainloop()"""


"""import math

memory = 0  # Global variable to store memory value

def calculate():
    history = []
    
    def show_memory():
        print(f"\nMemory: {memory}")
    
    while True:
        print("\nScientific Calculator")
        print("1. Basic Operations (+, -, *, /)")
        print("2. Advanced Operations (^, %, sqrt, log, sin, cos, tan)")
        print("3. Memory Functions (M+, M-, MR, MC)")
        print("4. Unit Converter (Celsius ↔ Fahrenheit)")
        print("5. Show History")
        print("6. Save History to File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
            
        if choice == '5':
            print("\nCalculation History:")
            for i, calc in enumerate(history, 1):
                print(f"{i}. {calc}")
            continue
            
        if choice == '6':
            with open("calculator_history.txt", "a") as f:
                for calc in history:
                    f.write(calc + "\n")
            print("History saved to 'calculator_history.txt'!")
            continue
            
        if choice == '4':
            temp = float(input("Enter temperature: "))
            unit = input("Convert to (C/F): ").upper()
            if unit == 'C':
                result = (temp - 32) * 5/9
                print(f"{temp}°F = {result:.2f}°C")
            elif unit == 'F':
                result = (temp * 9/5) + 32
                print(f"{temp}°C = {result:.2f}°F")
            else:
                print("Invalid unit! Use 'C' or 'F'.")
            continue
            
        if choice == '3':
            # Memory Functions
            print("\nMemory Functions:")
            print("1. M+ (Add to Memory)")
            print("2. M- (Subtract from Memory)")
            print("3. MR (Recall Memory)")
            print("4. MC (Clear Memory)")
            mem_choice = input("Choose memory operation (1-4): ")
            
            if mem_choice == '1':
                value = float(input("Enter value to add to memory: "))
                global memory
                memory += value
                show_memory()
            elif mem_choice == '2':
                value = float(input("Enter value to subtract from memory: "))
                memory -= value
                show_memory()
            elif mem_choice == '3':
                show_memory()
            elif mem_choice == '4':
                memory = 0
                print("Memory cleared!")
            else:
                print("Invalid choice!")
            continue
            
        try:
            num1 = float(input('Enter first number (or "MR" for Memory Recall): '))
            if num1 == "MR":
                num1 = memory
            op = input('Enter operator: ')
            
            if op not in ('sqrt', 'sin', 'cos', 'tan', 'log'):
                num2 = float(input('Enter second number: '))
            
            if choice == '1':
                if op == '+': result = num1 + num2
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': result = num1 / num2 if num2 != 0 else "Undefined"
                else: print("Invalid operator!"); continue
            else:
                if op == '^': result = num1 ** num2
                elif op == '%': result = num1 % num2
                elif op == 'sqrt': result = math.sqrt(num1)
                elif op == 'log': result = math.log(num1, 10)
                elif op == 'sin': result = math.sin(math.radians(num1))
                elif op == 'cos': result = math.cos(math.radians(num1))
                elif op == 'tan': result = math.tan(math.radians(num1))
                else: print("Invalid operator!"); continue
            
            expression = f"{num1} {op} {num2 if op not in ('sqrt', 'sin', 'cos', 'tan', 'log') else ''} = {result}"
            history.append(expression)
            print(f"Result: {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

calculate()"""



"""import math

memory = 0  # Global variable to store memory value

def calculate():
    history = []
    
    def show_memory():
        print(f"\nMemory: {memory}")
    
    while True:
        print("\nScientific Calculator")
        print("1. Basic Operations (+, -, *, /)")
        print("2. Advanced Operations (^, %, sqrt, log, sin, cos, tan)")
        print("3. Memory Functions (M+, M-, MR, MC)")
        print("4. Unit Converter (Celsius ↔ Fahrenheit)")
        print("5. Show History")
        print("6. Save History to File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
            
        if choice == '5':
            print("\nCalculation History:")
            for i, calc in enumerate(history, 1):
                print(f"{i}. {calc}")
            continue
            
        if choice == '6':
            with open("calculator_history.txt", "a") as f:
                for calc in history:
                    f.write(calc + "\n")
            print("History saved to 'calculator_history.txt'!")
            continue
            
        if choice == '4':
            temp = float(input("Enter temperature: "))
            unit = input("Convert to (C/F): ").upper()
            if unit == 'C':
                result = (temp - 32) * 5/9
                print(f"{temp}°F = {result:.2f}°C")
            elif unit == 'F':
                result = (temp * 9/5) + 32
                print(f"{temp}°C = {result:.2f}°F")
            else:
                print("Invalid unit! Use 'C' or 'F'.")
            continue
            
        if choice == '3':
            # Memory Functions
            print("\nMemory Functions:")
            print("1. M+ (Add to Memory)")
            print("2. M- (Subtract from Memory)")
            print("3. MR (Recall Memory)")
            print("4. MC (Clear Memory)")
            mem_choice = input("Choose memory operation (1-4): ")
            
            if mem_choice == '1':
                value = float(input("Enter value to add to memory: "))
                global memory
                memory += value
                show_memory()
            elif mem_choice == '2':
                value = float(input("Enter value to subtract from memory: "))
                memory -= value
                show_memory()
            elif mem_choice == '3':
                show_memory()
            elif mem_choice == '4':
                memory = 0
                print("Memory cleared!")
            else:
                print("Invalid choice!")
            continue
            
        try:
            num1 = float(input('Enter first number (or "MR" for Memory Recall): '))
            if num1 == "MR":
                num1 = memory
            op = input('Enter operator: ')
            
            if op not in ('sqrt', 'sin', 'cos', 'tan', 'log'):
                num2 = float(input('Enter second number: '))
            
            if choice == '1':
                if op == '+': result = num1 + num2
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': result = num1 / num2 if num2 != 0 else "Undefined"
                else: print("Invalid operator!"); continue
            else:
                if op == '^': result = num1 ** num2
                elif op == '%': result = num1 % num2
                elif op == 'sqrt': result = math.sqrt(num1)
                elif op == 'log': result = math.log(num1, 10)
                elif op == 'sin': result = math.sin(math.radians(num1))
                elif op == 'cos': result = math.cos(math.radians(num1))
                elif op == 'tan': result = math.tan(math.radians(num1))
                else: print("Invalid operator!"); continue
            
            expression = f"{num1} {op} {num2 if op not in ('sqrt', 'sin', 'cos', 'tan', 'log') else ''} = {result}"
            history.append(expression)
            print(f"Result: {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

calculate()"""
"""from tkinter import *
import math

memory = 0

def calculate():
    try:
        num1 = float(entry_num1.get())
        op = entry_op.get()
        
        if op not in ('sqrt', 'sin', 'cos', 'tan', 'log'):
            num2 = float(entry_num2.get())
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': result = num1 / num2 if num2 != 0 else "Undefined"
        elif op == '^': result = num1 ** num2
        elif op == '%': result = num1 % num2
        elif op == 'sqrt': result = math.sqrt(num1)
        elif op == 'log': result = math.log(num1, 10)
        elif op == 'sin': result = math.sin(math.radians(num1))
        elif op == 'cos': result = math.cos(math.radians(num1))
        elif op == 'tan': result = math.tan(math.radians(num1))
        else: result = "Invalid operator!"
        
        label_result.config(text=f"Result: {result}")
    except:
        label_result.config(text="Error: Invalid input!")

def memory_add():
    global memory
    memory += float(entry_num1.get())
    label_memory.config(text=f"Memory: {memory}")

def memory_recall():
    entry_num1.delete(0, END)
    entry_num1.insert(0, str(memory))

# GUI Setup
root = Tk()
root.title("Scientific Calculator")

Label(root, text="First Number:").grid(row=0, column=0)
entry_num1 = Entry(root)
entry_num1.grid(row=0, column=1)

Label(root, text="Operator:").grid(row=1, column=0)
entry_op = Entry(root)
entry_op.grid(row=1, column=1)

Label(root, text="Second Number:").grid(row=2, column=0)
entry_num2 = Entry(root)
entry_num2.grid(row=2, column=1)

Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

label_result = Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2)

Button(root, text="M+", command=memory_add).grid(row=5, column=0)
Button(root, text="MR", command=memory_recall).grid(row=5, column=1)

label_memory = Label(root, text="Memory: 0")
label_memory.grid(row=6, column=0, columnspan=2)

root.mainloop()"""
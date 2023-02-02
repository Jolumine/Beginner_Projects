import sys 
import os

class Creater: 
    def __init__(self):
        self.create(sys.argv)

    def create(self, arguments):
        if len(arguments) > 1: 
            if arguments[1] == "python":
                os.mkdir("./src")
                os.mkdir("./doc")

                with open("./run.py", "w") as f: 
                    f.write('from src import main\n\n\nif __name__ == "__main__":\n\tmain()\n')
                    f.close()

                with open("./src/__init__.py", "w") as f: 
                    f.write("def main():\n\tpass")  
                    f.close()

                with open("./src/const.py", "w") as f:   
                    f.close()

                with open("./README.md", "w") as f: 
                    project_name = input("Project Name:")
                    f.write(f"# {project_name}")
                    f.close()

                os.system("python -m venv .venv")
                os.system(".\.venv\Scripts\pip.exe freeze | powershell tee requirements.txt")

            elif arguments[1] == "cpp": 
                os.mkdir("./src")
                os.mkdir("./doc")

                with open("./main.cpp", "w") as f: 
                    f.write('#include <iostream>\n\nint main(){\n\tstd::cout << "Hello World!" << std::endl;\n\treturn 0;\n}')
                    f.close()

                with open("./README.md", "w") as f: 
                    project_name = input("Project Name:")
                    f.write(f"# {project_name}")
                    f.close()
            else: 
                print("Language not found.")
        else: 
            print("[!] Error [!]")




def main() -> Creater:
    return Creater() 


if __name__ == "__main__":
    main()

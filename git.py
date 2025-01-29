import os
from datetime import datetime

# Función para automatizar el proceso de git en la rama main con la fecha y hora actuales como mensaje de commit
def automate_git_process(repo_path):
    # Cambiar el directorio de trabajo actual a la ruta del repositorio
    os.chdir(repo_path)
    
    # Paso 1: Agregar todos los cambios
    os.system("git add .")
    
    # Paso 2: Hacer commit de los cambios con la fecha y hora actuales como mensaje
    commit_message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'git commit -m "{commit_message}"')
    
    # Paso 3: Subir los cambios a la rama main
    os.system("git push origin main")

# Ejemplo de uso
repo_path = "C:\Users\j.canadas\Documents\proyectos\proyectohtml\curso-html2"
automate_git_process(repo_path)

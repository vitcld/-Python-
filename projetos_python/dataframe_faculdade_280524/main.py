import pandas as pd

# Dados dos cursos
cursos_data = {
    'Código': ['CPP101', 'MAT201', 'PHY301', 'ENG401'],
    'Nome': ['Introdução à Computação', 'Cálculo Avançado', 'Física Moderna', 'Engenharia de Software'],
    'Créditos': [3, 4, 3, 3]
}

# Dados dos departamentos
departamentos_data = {
    'Código': ['CPP', 'MAT', 'PHY', 'ENG'],
    'Nome': ['Ciência da Computação', 'Matemática', 'Física', 'Engenharia']
}

# Dados dos professores
professores_data = {
    'ID': [101, 201, 301, 401],
    'Nome': ['Dr. João', 'Dra. Maria', 'Dr. Carlos', 'Dra. Ana'],
    'Departamento': ['CPP', 'MAT', 'PHY', 'ENG']
}

# Dados dos alunos
alunos_data = {
    'ID': [1, 2, 3, 4, 5],
    'Nome': ['José', 'Maria', 'Carlos', 'Ana', 'Joana'],
    'Curso': ['CPP101', 'MAT201', 'PHY301', 'ENG401', 'MAT201']
}

# Criando dataframes
df_cursos = pd.DataFrame(cursos_data)
df_departamentos = pd.DataFrame(departamentos_data)
df_professores = pd.DataFrame(professores_data)
df_alunos = pd.DataFrame(alunos_data)

# Exibindo dataframes
print("Cursos:")
print(df_cursos)
print("\nDepartamentos:")
print(df_departamentos)
print("\nProfessores:")
print(df_professores)
print("\nAlunos:")
print(df_alunos)

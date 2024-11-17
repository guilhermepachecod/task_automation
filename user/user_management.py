# task_automation/user/user_management.py

import os
import subprocess

# Função para listar usuários
def list_users():
    try:
        with open('/etc/passwd', 'r') as f:
            users = [line.split(':')[0] for line in f.readlines()]
        
        if users:
            print("Usuários cadastrados:")
            for user in users:
                print(f"- {user}")
        else:
            print("Nenhum usuário cadastrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para adicionar um usuário
def add_user(username):
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        print(f"Usuário '{username}' adicionado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao adicionar o usuário '{username}'.")

# Função para remover um usuário
def remove_user(username):
    try:
        subprocess.run(['sudo', 'userdel', username], check=True)
        print(f"Usuário '{username}' removido com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao remover o usuário '{username}'.")

# Função para alterar a senha de um usuário
def change_password(username, new_password):
    try:
        subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{new_password}", text=True, check=True)
        print(f"Senha do usuário '{username}' alterada com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao alterar a senha do usuário '{username}'.")

# Função para listar grupos
def list_groups():
    try:
        with open('/etc/group', 'r') as f:
            groups = [line.split(':')[0] for line in f.readlines()]
        
        if groups:
            print("Grupos cadastrados:")
            for group in groups:
                print(f"- {group}")
        else:
            print("Nenhum grupo cadastrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para adicionar um grupo
def add_group(groupname):
    try:
        subprocess.run(['sudo', 'groupadd', groupname], check=True)
        print(f"Grupo '{groupname}' adicionado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao adicionar o grupo '{groupname}'.")

# Função para remover um grupo
def remove_group(groupname):
    try:
        subprocess.run(['sudo', 'groupdel', groupname], check=True)
        print(f"Grupo '{groupname}' removido com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao remover o grupo '{groupname}'.")



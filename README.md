# 🔒 EncDes - Herramienta de Encriptación/Desencriptación de Archivos

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Kivy](https://img.shields.io/badge/Kivy-2.3.1-1F72B6?logo=kivy&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-44.0.0-000000)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

Aplicación GUI moderna para encriptar y desencriptar archivos usando **AES-256 (CBC Mode)** con interfaz intuitiva.

## 🚀 Características Principales
- 🔐 Encriptación AES-256 con modo CBC
- 📂 Selección múltiple de archivos
- 🗝️ Clave predefinida para demostración
- 🎨 Interfaz gráfica moderna con Kivy
- 🌍 Multiplataforma (Windows, Linux, macOS)
- 📦 Empaquetado como ejecutable independiente

## 📥 Instalación

### Requisitos Previos
- Python 3.10+
- Gestor de paquetes pip

### Pasos de Instalación
```bash
# 1. Clonar repositorio
git clone https://github.com/tuusuario/encdes.git
cd encdes

## 2. Crear entorno virtual (Windows)
python -m venv venv
.\venv\Scripts\activate

## 2. Crear entorno virtual (Linux/Mac)
python3 -m venv venv
source venv/bin/activate

## 3. Instalar dependencias
pip install -r requirements.txt

## 4. Ejecutar la aplicación
python main.py
🖥️ Uso Básico
Seleccionar archivo(s) usando el explorador integrado

## Elegir operación:

🛡️ Encriptar: Genera archivo .enc

🔓 Desencriptar: Elimina extensión .enc

## Ejemplo de flujo:

plaintext
Copy
documento.txt ➔ Encriptar ➔ documento.txt.enc
documento.txt.enc ➔ Desencriptar ➔ documento.txt
## 🧠 Detalles Técnicos
🔧 Especificaciones de Encriptación
Parámetro	Valor
🧬 Algoritmo	AES-256
🎛️ Modo	CBC
🧩 Padding	PKCS7
🔑 Longitud clave	32 bytes (256 bits)
🎲 IV	16 bytes aleatorios
## 📂 Estructura del Proyecto
bash
Copy
.
├── 📄 main.py            # Lógica principal
├── 🎨 my.kv              # Diseño de interfaz
├── 📦 requirements.txt   # Dependencias
└── 📖 README.md          # Documentación
## 📚 Dependencias
Librería	Versión	Propósito	Badge
Kivy	2.3.1	Interfaz gráfica	Kivy
Cryptography	44.0.0	Implementación AES	Cryptography
PyInstaller	6.11.1	Generación ejecutables	PyInstaller
## 📦 Compilación a Ejecutable
bash
Copy
pyinstaller --onefile --windowed \
--name "EncDes" \
--add-data "my.kv:." \
--icon=assets/icon.ico \
main.py
## 🤝 Contribución
### 🍴 Haz fork del proyecto

### 🌿 Crea tu rama:

bash
Copy
git checkout -b feature/nueva-funcion
## 💾 Commit cambios:

bash
Copy
git commit -m 'Añade nueva función'
## ⬆️ Push a la rama:

bash
Copy
git push origin feature/nueva-funcion
## 📤 Abre un Pull Request

## ⚖️ Licencia
### Distribuido bajo licencia MIT.

## ⚠️ Importante de Seguridad
### Warning
Este proyecto usa una clave fija para demostración.
No utilizar con datos sensibles sin implementar:

Sistema seguro de gestión de claves

Rotación de IVs

Validación de integridad

## 🚧 Futuras Mejoras
Prioridad	Función	Estado
🔴 Alta	Gestión de claves seguras	🚧 En desarrollo
🟡 Media	Soporte multi-algoritmo	📅 Planeado
🟢 Baja	Sistema de logging	💡 Propuesto

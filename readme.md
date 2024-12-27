# Proyecto Modbus TCP en Python

Este proyecto permite conectarse a un dispositivo Modbus TCP, leer registros y mostrar la información en la consola. La documentación incluye cómo configurar el entorno para correr el proyecto y cómo ajustar los parámetros principales del código.

---

## **Configuración del entorno**

### 1. Requisitos previos
- Tener instalado **Python 3.7** o superior.
- Tener acceso a un dispositivo Modbus TCP o un simulador.
- Para la prueba se debe correr el servidor en un PC y el cliente en otro PC

---

### 2. Configurar un entorno virtual

Es altamente recomendado usar un entorno virtual para evitar conflictos con otras bibliotecas instaladas globalmente en tu sistema.

1. **Crear el entorno virtual**:
   ```bash
   python -m venv env
   ```

2. **Activar el entorno virtual**:
   - En **Linux/macOS**:
     ```bash
     source env/bin/activate
     ```
   - En **Windows**:
     ```bash
     env\Scripts\activate
     ```

   Después de activar el entorno virtual, verás algo como `(env)` al inicio de la línea de comandos.

3. **Instalar las dependencias**:
   Todas las dependencias necesarias están en el archivo `requirements.txt`. Instálalas con:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Ejecutar el proyecto**

1. Asegúrate de haber configurado y activado el entorno virtual.
2. Ejecuta el programa principal cliente:
   ```bash
   python modbus_client.py
   ```
3. Ejecuta el programa principal servidor:
   ```bash
   python modbus_server.py
   ```
---

## **Configuración del código**

La parte del código donde se configuran los parámetros de conexión y lectura es crucial para que el programa funcione correctamente.

```python
HOST = "127.0.0.1"  # Dirección IP del dispositivo Modbus
PORT = 502          # Puerto TCP del dispositivo Modbus
START_ADDRESS = 0   # Dirección inicial de lectura
MAX_REGISTERS = 10  # Cantidad máxima de registros a leer
INTERVAL = 2        # Intervalo en segundos entre lecturas
```

### Parámetros explicados:
1. **`HOST`**:
   - La IP solo se cambia en el cliente, el servidor debe correr en
   - Define la dirección IP del servidor Modbus.
   - Cambia este valor según la configuración de tu dispositivo o simulador.
   - Ejemplo:
     - Para usar una IP local: `"127.0.0.1"`
     - Para usar un dispositivo en tu red: `"192.168.0.100"`

2. **`PORT`**:
   - Puerto donde el servidor Modbus está escuchando.
   - Por defecto, el protocolo Modbus usa el puerto `502`.

3. **`START_ADDRESS`**:
   - Dirección inicial de los registros que deseas leer.
   - Por ejemplo, si el servidor tiene datos en las direcciones `0` a `100`, puedes establecer aquí la dirección de inicio.

4. **`MAX_REGISTERS`**:
   - Cantidad de registros a leer desde `START_ADDRESS`.
   - Por ejemplo, si quieres leer 10 registros comenzando desde `0`, establece `MAX_REGISTERS = 10`.

5. **`INTERVAL`**:
   - Intervalo en segundos entre cada intento de lectura.
   - Puedes ajustar este valor según la frecuencia de actualización requerida.

---

## **Notas importantes**

- Si el servidor Modbus no está activo, el programa intentará reconectarse automáticamente.
- Verifica que la dirección IP y el puerto sean correctos antes de ejecutar el programa.
- Si usas un simulador Modbus, asegúrate de que esté configurado con los mismos parámetros que el código.

---

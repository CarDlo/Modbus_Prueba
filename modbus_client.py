import logging
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import time

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_modbus_registers(client, start_address=0, max_registers=10):
    """
    Lee un rango de registros Modbus desde un dispositivo Modbus TCP.

    :param client: Instancia del cliente ModbusTcpClient.
    :param start_address: Dirección inicial de los registros a leer.
    :param max_registers: Cantidad máxima de registros a leer.
    """
    try:
        # Leer los registros
        logging.info(f"Leyendo registros desde la dirección {start_address} con un máximo de {max_registers} registros...")
        result = client.read_holding_registers(address=start_address, count=max_registers)

        # Verificar si la lectura fue exitosa
        if result.isError():
            logging.error(f"Error al leer registros: {result}")
        else:
            # Mostrar los registros leídos
            logging.info(f"Registros leídos correctamente:")
            for i, value in enumerate(result.registers):
                address = start_address + i
                logging.info(f"Dirección: {address}, Valor: {value}")

    except ModbusException as e:
        logging.error(f"Excepción de Modbus: {e}")

    except Exception as e:
        logging.error(f"Error inesperado: {e}")

def connect_with_retries(host, port, max_retries=5, retry_interval=5):
    """
    Intenta conectarse al dispositivo Modbus con varios reintentos.

    :param host: Dirección IP del dispositivo Modbus.
    :param port: Puerto TCP del dispositivo Modbus.
    :param max_retries: Número máximo de reintentos antes de abortar.
    :param retry_interval: Intervalo en segundos entre reintentos.
    :return: Cliente ModbusTcpClient conectado o None si no se pudo conectar.
    """
    retries = 0
    while retries < max_retries or max_retries == 0:
        client = ModbusTcpClient(host=host, port=port)
        if client.connect():
            logging.info(f"Conexión exitosa a {host}:{port}")
            return client
        else:
            logging.warning(f"No se pudo conectar al servidor Modbus en {host}:{port}. Reintentando en {retry_interval} segundos...")
            client.close()
            time.sleep(retry_interval)
            retries += 1

    logging.error(f"No se pudo conectar al servidor después de {retries} intentos.")
    return None

def main_loop(host, port=502, start_address=0, max_registers=10, interval=5):
    """
    Mantiene la conexión al dispositivo Modbus y lee datos de manera continua.

    :param host: Dirección IP del dispositivo Modbus.
    :param port: Puerto TCP del dispositivo Modbus.
    :param start_address: Dirección inicial de lectura.
    :param max_registers: Cantidad máxima de registros a leer.
    :param interval: Intervalo en segundos entre lecturas consecutivas.
    """
    while True:
        client = connect_with_retries(host, port, max_retries=0)  # Reintenta indefinidamente
        if not client:
            logging.error("No se pudo establecer conexión con el servidor. Terminando programa.")
            break

        try:
            while client.connect():
                read_modbus_registers(client, start_address, max_registers)
                logging.info(f"Esperando {interval} segundos para la próxima lectura...")
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Bucle detenido por el usuario.")
            break
        except Exception as e:
            logging.error(f"Error inesperado: {e}. Intentando reconectar...")
        finally:
            logging.info("Cerrando conexión...")
            client.close()

if __name__ == "__main__":
    # Configuración personalizable
    HOST = "127.0.0.1"  # Dirección IP del dispositivo Modbus
    PORT = 502          # Puerto TCP del dispositivo Modbus
    START_ADDRESS = 0   # Dirección inicial de lectura
    MAX_REGISTERS = 10  # Cantidad máxima de registros a leer
    INTERVAL = 2        # Intervalo en segundos entre lecturas

    # Llamar a la función principal
    main_loop(HOST, PORT, START_ADDRESS, MAX_REGISTERS, INTERVAL)

from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_modbus_server(host="127.0.0.1", port=502):
    """
    Inicia un servidor Modbus TCP que actúa como un dispositivo esclavo.

    :param host: Dirección IP del servidor Modbus.
    :param port: Puerto TCP del servidor Modbus (predeterminado: 502).
    """
    try:
        # Crear un bloque de datos para los registros de holding
        # Inicializamos los registros con valores predefinidos (por ejemplo, 100, 200, 300, ...)
        holding_registers = ModbusSequentialDataBlock(0, [i * 100 for i in range(100)])

        # Crear un contexto de esclavo
        slave_context = ModbusSlaveContext(hr=holding_registers)

        # Crear un contexto de servidor
        server_context = ModbusServerContext(slaves=slave_context, single=True)

        # Iniciar el servidor Modbus TCP
        logging.info(f"Iniciando servidor Modbus TCP en {host}:{port}...")
        StartTcpServer(context=server_context, address=(host, port))

    except Exception as e:
        logging.error(f"Error al iniciar el servidor Modbus TCP: {e}")

if __name__ == "__main__":
    # Configuración personalizable
    HOST = "127.0.0.1"  # Dirección IP del servidor Modbus
    PORT = 502          # Puerto TCP del servidor Modbus

    # Llamar a la función para iniciar el servidor
    run_modbus_server(HOST, PORT)
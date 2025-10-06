from pymodbus.client import ModbusTcpClient, ModbusSerialClient
import pandas as pd

# ---------------------- KONFIGURACJA ----------------------
# Wybierz typ połączenia: 'tcp' lub 'rtu'
CONNECTION_TYPE = 'tcp'

# Dla TCP
TCP_IP = '192.168.1.100'
TCP_PORT = 502

# Dla RTU
RTU_PORT = '/dev/ttyUSB0'   # np. COM3 w Windows
BAUDRATE = 9600
PARITY = 'N'
STOPBITS = 1
BYTESIZE = 8
TIMEOUT = 1

UNIT_ID = 1           # adres Modbus (slave)
MAX_ADDRESS = 1000    # maksymalny adres do sprawdzenia
STEP = 10             # odczyt blokami po STEP rejestrów
OUTPUT_CSV = 'modbus_scan_results.csv'
# -----------------------------------------------------------

# Tworzenie klienta
if CONNECTION_TYPE == 'tcp':
    client = ModbusTcpClient(TCP_IP, port=TCP_PORT)
elif CONNECTION_TYPE == 'rtu':
    client = ModbusSerialClient(
        method='rtu',
        port=RTU_PORT,
        baudrate=BAUDRATE,
        parity=PARITY,
        stopbits=STOPBITS,
        bytesize=BYTESIZE,
        timeout=TIMEOUT
    )
else:
    raise ValueError("Nieznany typ połączenia. Wybierz 'tcp' lub 'rtu'.")

if not client.connect():
    print("Nie udało się połączyć z urządzeniem")
    exit()

found_registers = []

for start in range(0, MAX_ADDRESS, STEP):
    try:
        result = client.read_holding_registers(address=start, count=STEP, unit=UNIT_ID)
        if not result.isError():
            for i, val in enumerate(result.registers):
                found_registers.append({"Adres": start + i, "Wartość": val})
    except Exception as e:
        print(f"Błąd przy adresach {start}-{start+STEP-1}: {e}")

client.close()

if found_registers:
    df = pd.DataFrame(found_registers)
    print(df)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Wyniki zapisane do {OUTPUT_CSV}")
else:
    print("Nie znaleziono żadnych działających holding registers.")

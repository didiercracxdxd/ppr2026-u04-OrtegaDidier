import ipaddress
from pathlib import Path

dispositivos=[
    {
        "nombre": "Router01",
        "interfaz": "G0/0",
        "ip": "192.168.1.1",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "Router02",
        "interfaz": "G0/0",
        "ip": "192.168.2.1",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "SwitchCore",
        "interfaz": "VLAN10",
        "ip": "192.168.10.2",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "FirewallEdge",
        "interfaz": "G0/1",
        "ip": "10.0.0.256",
        "mascara": "255.0.0.0"
    },
    {
        "nombre": "ServidorDNS",
        "interfaz": "Eth0",
        "ip": "192.168.2.1",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "AccessPoint01",
        "interfaz": "BVI1",
        "ip": "172.16.5.10",
        "mascara": "255.255.0.0"
    },
    {
        "nombre": "RouterBranch",
        "interfaz": "S0/0/0",
        "ip": "192.168.100.999",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "ServidorSQL",
        "interfaz": "Eth1",
        "ip": "192.168.20.15",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "SwitchAccess",
        "interfaz": "VLAN1",
        "ip": "192.168.1.254",
        "mascara": "255.255.255.0"
    },
    {
        "nombre": "GatewayVoz",
        "interfaz": "G0/2",
        "ip": "172.16.1.1",
        "mascara": "255.255.255.128"
    }
]

# crear la carpeta con los archivos de configuración
carpeta=Path("configuraciones")
carpeta.mkdir(exist_ok=True)

ips_registradas=[]

# validar y generar solo las válidas
for dispositivo in dispositivos:
    ip = dispositivo["ip"]
    nombre = dispositivo["nombre"]

    try:
        ipaddress.ip_address(ip)

        if ip in ips_registradas:
            print(nombre, "_", ip, "DIRECCION IP DUPLICADA - NO SE GENERA")
            continue

        ips_registradas.append(ip)

        configuracion=f'''
hostname {nombre}

interface {dispositivo["interfaz"]}
ip address {ip} {dispositivo["mascara"]}
no shutdown

end
'''
        archivo=carpeta / f'{nombre}.txt'
        archivo.write_text(configuracion, encoding="utf-8")
        print(nombre, "_", ip, "DIRECCION IP VALIDA - ARCHIVO GENERADO")

    except ValueError:
        print(nombre, "_", ip, "DIRECCION IP NO VALIDA - NO SE GENERA")
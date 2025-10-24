import os
import random
from faker import Faker


def generate_file(carpeta, archivo):
    fake = Faker()

    os.makedirs(carpeta, exist_ok=True)

    errors = ["INFO", "WARNING", "ERROR"]
    dates = [
        "2021-07-12",
        "2023-02-05",
        "2024-11-19",
        "2020-09-30",
        "2022-05-17",
        "2025-01-01",
        "2023-08-22",
        "2021-11-10",
        "2024-03-05",
        "2022-07-28",
        "2020-12-15",
        "2025-06-30",
        "2021-03-18",
        "2023-09-09",
        "2024-12-25",
    ]
    IPs = [
        "192.45.23.11",
        "8.234.56.78",
        "123.45.67.89",
        "210.10.5.67",
        "34.56.78.90",
        "11.22.33.44",
        "200.100.50.25",
        "172.16.0.1",
        "45.67.89.12",
        "98.76.54.32",
        "167.89.23.45",
        "10.0.0.5",
        "250.100.50.25",
        "123.123.123.123",
        "8.8.8.8",
    ]

    with open(archivo, "w") as file:
        for _ in range(random.randint(1000, 2000)):
            linea = (
                random.choice(dates)
                + ";"
                + random.choice(errors)
                + ";"
                + random.choice(IPs)
                + ";"
                + fake.sentence()
                + "\n"
            )
            file.write(linea)


def generate_result(carpeta, archivo, resultados, texto):

    os.makedirs(carpeta, exist_ok=True)

    with open(archivo, "w") as file:
        if texto:
            file.write(texto + "\n")
            for clave, valor in resultados.items():
                linea = str(clave) + " : " + str(valor) + "\n"
                file.write(linea)


def overwrite_result(carpeta, archivo, resultados, texto):

    os.makedirs(carpeta, exist_ok=True)

    with open(archivo, "a") as file:
        if texto:
            file.write(texto + "\n")
            for clave, valor in resultados.items():
                linea = str(clave) + " : " + str(valor) + "\n"
                file.write(linea)

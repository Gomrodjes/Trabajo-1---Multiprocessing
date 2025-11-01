import os
import multiprocessing

import generate_file_function
import aux_functions

carpeta = "../Trabajo-1---Multiprocessing/files"
archivo_principal = os.path.join(carpeta, "logs.txt")
archivo_resultados = os.path.join(carpeta, "resultados.txt")


def main():

    generate_file_function.generate_file(carpeta, archivo_principal)

    bloques = list(aux_functions.dividir_por_bloques(archivo_principal, 200))

    cola1 = multiprocessing.Queue()
    cola2 = multiprocessing.Queue()
    cola3 = multiprocessing.Queue()
    cola4 = multiprocessing.Queue()

    resultados1 = multiprocessing.Process(
        target=aux_functions.contar_lineas, args=(bloques, cola1)
    )

    resultados2 = multiprocessing.Process(
        target=aux_functions.contar_errores, args=(bloques, cola2)
    )

    resultados3 = multiprocessing.Process(
        target=aux_functions.contar_ips_mas_usadas, args=(bloques, cola3)
    )

    resultados4 = multiprocessing.Process(
        target=aux_functions.contar_error_por_dia, args=(bloques, cola4)
    )

    resultados1.start()
    resultados2.start()
    resultados3.start()
    resultados4.start()

    resultados1.join()
    resultados2.join()
    resultados3.join()
    resultados4.join()

    resultados1 = cola1.get()
    resultados2 = cola2.get()
    resultados3 = cola3.get()
    resultados4 = cola4.get()

    generate_file_function.generate_result(
        carpeta, archivo_resultados, resultados1, "**** LINEAS TOTALES ****"
    )
    generate_file_function.overwrite_result(
        carpeta, archivo_resultados, resultados2, "**** TODOS LOS ERRORES EXISTENTES ****"
    )
    generate_file_function.overwrite_result(
        carpeta, archivo_resultados, resultados3, "**** LAS 10 IPS MAS USADAS ****"
    )
    generate_file_function.overwrite_result(
        carpeta, archivo_resultados, resultados4, "**** LOS DIAS CON ERRORES ****"
    )


if __name__ == "__main__":
    main()

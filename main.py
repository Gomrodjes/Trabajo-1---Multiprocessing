import os
import multiprocessing

import generate_file_function
import aux_functions

carpeta = "../Trabajo-1---Multiprocessing/files"
archivo_principal = os.path.join(carpeta, "logs.txt")
archivo_resultados = os.path.join(carpeta, "resultados.txt")


def main():

    print("🧩 Generando archivo de logs inicial...")
    generate_file_function.generate_file(carpeta, archivo_principal)

    print("📂 Dividiendo el archivo en bloques...")
    bloques = list(aux_functions.dividir_por_bloques(archivo_principal, 200))
    print(f"✅ Se han creado {len(bloques)} bloques de texto.")

    # Crear colas
    cola_lineas = multiprocessing.Queue()
    cola_errores = multiprocessing.Queue()
    cola_ips = multiprocessing.Queue()
    cola_dias = multiprocessing.Queue()

    # Crear procesos
    print("🚀 Iniciando procesos de análisis...")
    proceso_lineas = multiprocessing.Process(
        target=aux_functions.contar_lineas, args=(bloques, cola_lineas)
    )

    proceso_errores = multiprocessing.Process(
        target=aux_functions.contar_errores, args=(bloques, cola_errores)
    )

    proceso_ips = multiprocessing.Process(
        target=aux_functions.contar_ips_mas_usadas, args=(bloques, cola_ips)
    )

    proceso_dias = multiprocessing.Process(
        target=aux_functions.contar_error_por_dia, args=(bloques, cola_dias)
    )

     # Iniciar y Finalizar procesos
    for p in [proceso_lineas, proceso_errores, proceso_ips, proceso_dias]:
        print(f"🔹 Ejecutando proceso {p.name}...")
        p.start()

    for p in [proceso_lineas, proceso_errores, proceso_ips, proceso_dias]:
        p.join()
        print(f"✅ Proceso {p.name} finalizado.")

    # Recuperar resultados
    print("📊 Obteniendo resultados desde las colas...")
    resultados_lineas = cola_lineas.get()
    resultados_errores = cola_errores.get()
    resultados_ips = cola_ips.get()
    resultados_dias = cola_dias.get()

    print("💾 Guardando resultados en archivo...")
    generate_file_function.generate_result(
        carpeta, archivo_resultados, resultados_lineas, "LINEAS->TOTAL"
    )
    generate_file_function.overwrite_result(
        carpeta, archivo_resultados, resultados_errores, "TIPO->VALOR"
    )
    generate_file_function.overwrite_result(
        carpeta, archivo_resultados, resultados_ips, "IP->FRECUENCIA"
    )
    generate_file_function.overwrite_result(
        carpeta, archivo_resultados, resultados_dias, "DIAS->FRECUENCIAERRORES"
    )

    print("🏁 Análisis completado correctamente.")


if __name__ == "__main__":
    try:
        main()
        print("✅ Ejecución completada correctamente.")
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

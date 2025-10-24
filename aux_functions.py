def dividir_por_bloques(nombre_archivo, tamaño_bloque):
    with open(nombre_archivo, "r") as f:
        while True:
            bloque = []
            for _ in range(tamaño_bloque):
                linea = f.readline()
                if not linea:
                    break
                bloque.append(linea)
            if not bloque:
                break
            yield bloque


def contar_errores(bloques, cola):
    resultado = {}
    for bloque in bloques:
        for linea in bloque:
            partes = linea.strip().split(";")
            if len(partes) == 4:
                clave = partes[1]
                if clave not in resultado:
                    resultado[clave] = 1
                else:
                    resultado[clave] += 1
    resultados_ordenados = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    cola.put(dict(resultados_ordenados))


def contar_lineas(bloques, cola):
    cont = 0
    for bloque in bloques:
        cont += len(bloque)
    cola.put({"lineas": cont})


def contar_ips_mas_usadas(bloques, cola):
    resultado = {}
    for bloque in bloques:
        for linea in bloque:
            partes = linea.strip().split(";")
            if len(partes) == 4:
                clave = partes[2]
                if clave not in resultado:
                    resultado[clave] = 1
                else:
                    resultado[clave] += 1
    resultados_ordenados = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    resultado_Top10 = resultados_ordenados[:10]
    cola.put(dict(resultado_Top10))


def contar_error_por_dia(bloques, cola):
    resultado = {}
    for bloque in bloques:
        for linea in bloque:
            partes = linea.strip().split(";")
            if len(partes) == 4:
                clave = partes[1]
                claveDate = partes[0]
                if clave == "ERROR":
                    if claveDate not in resultado:
                        resultado[claveDate] = 1
                    else:
                        resultado[claveDate] += 1
    resultados_ordenados = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    cola.put(dict(resultados_ordenados))

import subprocess
import re

def run_tests():
    # Ejecuta pytest como un proceso externo y captura la salida
    result = subprocess.run(
        ["pytest", "-v", "--tb=short"],
        text=True,  # Para obtener la salida como texto en lugar de bytes
        capture_output=True  # Captura la salida estándar y de error
    )
    output = result.stdout
    return result.returncode, output

def parse_test_results(output):
    # Define los nombres de los ejercicios para identificarlos en la salida
    exercises = {
        "Ejercicio 1": "test_sumar_numeros",  # Nombre de la función de prueba para el Ejercicio 1 # Nombre de la función de prueba para el Ejercicio 2
        "Ejercicio 2": "test_contar_palabras"  # Nombre de la función de prueba para el Ejercicio 2
    }
    
    results = {}
    for exercise, test_name in exercises.items():
        # Busca si el test correspondiente pasó o falló
        if re.search(rf'{test_name}.*?FAILED', output):
            results[exercise] = "falló🤔🤞"
        elif re.search(rf'{test_name}.*?PASSED', output):
            results[exercise] = "pasó🦾🙌"
        else:
            results[exercise] = "no encontrado🔥"

    return results

if __name__ == '__main__':
    # Ejecuta las pruebas y captura el resultado y la salida
    result_code, output = run_tests()

    # Analiza los resultados
    results = parse_test_results(output)

    # Imprime la salida de pytest
    print(output)

    # Imprime el informe detallado de resultados
    for exercise, status in results.items():
        print(f"{exercise}: {status}")

    # Imprime el mensaje basado en el resultado total
    if all(status == "pasó" for status in results.values()):
        print("Todos los ejercicios pasaron exitosamente ✔")
    else:
        print("Algunos ejercicios fallaron ❌")

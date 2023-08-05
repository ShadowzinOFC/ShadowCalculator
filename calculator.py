def find_closest_solution(target_sum):
    closest_diff = float('inf')
    closest_solution = None

    for x in range(1, target_sum):
        for y in range(1, target_sum):
            for z in range(1, target_sum):
                current_sum = x**3 + y**3 + z**3
                current_diff = abs(target_sum - current_sum)

                if current_diff < closest_diff:
                    closest_diff = current_diff
                    closest_solution = (x, y, z)

    return closest_solution

def read_results_file(filename):
    results = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                k, solution = int(parts[0]), eval(parts[1])
                results[k] = solution
    except FileNotFoundError:
        pass
    return results

def save_result_to_file(filename, k, solution):
    with open(filename, "a") as file:
        file.write(f"{k}:{solution}\n")

def is_close(value1, value2, tolerance=1e-5):
    return abs(value1 - value2) < tolerance

try:
    target_sum = int(input("Digite o valor de k: "))
except ValueError:
    print("Por favor, insira um valor numérico válido.")
    exit()

results = read_results_file("resultados.txt")

if target_sum in results:
    if is_close(sum(num**3 for num in results[target_sum]), target_sum):
        print(f"Solução exata encontrada para k = {target_sum}: {results[target_sum]}")
    else:
        print(f"Solução aproximada encontrada para k = {target_sum}: {results[target_sum]}")
else:
    closest_solution = find_closest_solution(target_sum)
    
    if closest_solution:
        closest_value = sum(num**3 for num in closest_solution)
        if is_close(closest_value, target_sum):
            print("A solução mais próxima é:", closest_solution)
            print("O valor da solução mais próxima é:", closest_value)
            save_result_to_file("resultados.txt", target_sum, closest_solution)
        else:
            print("Solução aproximada encontrada:", closest_solution)
            print("O valor da solução aproximada é:", closest_value)
    else:
        print("Não foram encontradas soluções dentro dos limites considerados.")

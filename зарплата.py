from pathlib import *

def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  
                try:
                    salary = int(parts[1])
                    salaries.append(salary)
                except ValueError:
                    continue  
            if not salaries:
                return (0, 0)
            
            total = sum(salaries)
            average = total / len(salaries)
            
            return (total, average)
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

test_path = Path("salary_file.txt")
with open(test_path, "w", encoding="utf-8") as file:
    file.write("Alex Korp,3000\n")
    file.write("Nikita Borisenko,2000\n")
    file.write("Sitarama Raju,1000\n")


total, average = total_salary(test_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# капец
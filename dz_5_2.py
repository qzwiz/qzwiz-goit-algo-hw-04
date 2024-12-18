


def get_cats_info(path):
    cats_info = []
    try:
        with open(path , 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat = {
                        "id": parts[0],    
                        "name": parts[1],     
                        "age": int(parts[2])
                    }
                cats_info.append(cat)

    
    
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None
    return cats_info


cats = get_cats_info('text.txt')

if cats:
    for i in cats:
        print(i)
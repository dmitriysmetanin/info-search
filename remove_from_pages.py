import re

def remove_html_tags(filename):
    """
    Читает HTML файл и удаляет теги <img>, <link>, <style>, <script>
    """
    try:
        # 1) Читаем файл
        with open(f"./pages/page_{page_index}.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 2) Удаляем теги
        # Удаляем <img> теги и их содержимое (самозакрывающиеся)
        content = re.sub(r'<img[^>]*>', '', content, flags=re.IGNORECASE | re.DOTALL)

        # Удаляем <img> теги и их содержимое (самозакрывающиеся)
        content = re.sub(r'<meta[^>]*>', '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Удаляем <link> теги
        content = re.sub(r'<link[^>]*>', '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Удаляем <style> теги и всё содержимое между ними
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Удаляем <script> теги и всё содержимое между ними
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Записываем результат обратно в файл (или можно вернуть строку)
        with open(f"./pages_removed/page_{page_index}.txt", 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Файл {filename} успешно обработан!")
        return content
        
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Использование
for page_index in range(1, 100):
    # filename = f'./pages/page_{page_index}.txt'  # укажите путь к вашему файлу
    result = remove_html_tags(page_index)
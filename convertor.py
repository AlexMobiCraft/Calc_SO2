import base64

def image_to_base64(path):
    try:
        with open(path, 'rb') as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        return f"Ошибка: Файл не найден: {path}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

logo_jpg_b64 = image_to_base64(r'C:\Users\38670\DEV_WEB\Calc_SO2\logo.jpg')
logo_negativ_png_b64 = image_to_base64(r'C:\Users\38670\DEV_WEB\Calc_SO2\logo_negativ.png')

print('start_logo_light')
print(logo_jpg_b64)
print('end_logo_light')

print('start_logo_dark')
print(logo_negativ_png_b64)
print('end_logo_dark')
import requests
import os

# Configuração da API
endpoint = "https://mycognitiveservices.cognitiveservices.azure.com/vision/v3.2/ocr"
api_key = "**************************63"
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/octet-stream"
}

# Função para reconhecer texto em uma imagem
def recognize_text(image_path):
    with open(image_path, "rb") as image_file:
        response = requests.post(endpoint, headers=headers, data=image_file)
    response.raise_for_status()
    return response.json()

# Diretórios de entrada e saída
input_dir = "inputs"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# Processar cada imagem na pasta de entrada
for image_file in os.listdir(input_dir):
    if image_file.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(input_dir, image_file)
        result = recognize_text(image_path)
        output_path = os.path.join(output_dir, f"{os.path.splitext(image_file)[0]}.txt")
        with open(output_path, "w") as output_file:
            output_file.write(str(result))

print("Processamento concluído.")

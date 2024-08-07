import requests
import json
import os

# Endpoint e chave de API
endpoint = "https://mycognitiveservices.cognitiveservices.azure.com/vision/v3.2/ocr"
api_key = "9065ef9e61eb4c3ebeba3493c1a7ee63"

def recognize_text(image_path):
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'language': 'unk',
        'detectOrientation': 'true'
    }

    with open(image_path, 'rb') as image_file:
        response = requests.post(endpoint, headers=headers, params=params, data=image_file)
        response.raise_for_status()
        analysis = response.json()

    return analysis

def extract_text(analysis):
    lines = []
    for region in analysis['regions']:
        for line in region['lines']:
            line_text = ' '.join([word['text'] for word in line['words']])
            lines.append(line_text)
    return '\n'.join(lines)

def save_text(image_path, text):
    output_path = os.path.join('outputs', os.path.basename(image_path) + '.txt')
    with open(output_path, 'w') as output_file:
        output_file.write(text)

def process_images():
    input_folder = 'inputs'
    for image_file in os.listdir(input_folder):
        if image_file.lower().endswith(('png', 'jpg', 'jpeg')):
            image_path = os.path.join(input_folder, image_file)
            print(f"Processing {image_path}")
            analysis = recognize_text(image_path)
            text = extract_text(analysis)
            save_text(image_path, text)
            print(f"Text saved to {os.path.join('outputs', image_file + '.txt')}")

if __name__ == '__main__':
    process_images()

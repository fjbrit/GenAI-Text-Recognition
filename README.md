# GenAI Text Recognition

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Azure Cognitive Services](https://img.shields.io/badge/Azure%20Cognitive%20Services-OCR-brightgreen)

## Descrição

Este projeto utiliza o serviço OCR (Optical Character Recognition) do Azure Cognitive Services para reconhecer e extrair texto de imagens. Foi desenvolvido como parte de um projeto educacional para a DIO, demonstrando uma abordagem prática de reconhecimento de texto em imagens.

## Ferramentas Utilizadas

- **Linguagem de Programação**: Python 3.8+
- **Serviços de OCR**: Azure Cognitive Services OCR
- **Ambiente Virtual**: venv
- **Bibliotecas**:
  - `requests` para integração com o Azure

## Passo a Passo

### 1. Clonar o Repositório

 ```bash
git clone https://github.com/fjbrit/GenAI-Text-Recognition.git
cd GenAI-Text-Recognition

2. Configurar o Ambiente Virtual

bash
python -m venv venv
source venv/Scripts/activate  # No Windows
# ou
source venv/bin/activate  # No macOS/Linux
3. Instalar Dependências

bash
pip install -r requirements.txt
4. Configurar as Chaves de API
Adicione a chave da API e o endpoint corretos no arquivo recognize_text.py:

python
endpoint = "https://<seu-serviço>.cognitiveservices.azure.com/vision/v3.1/ocr"
api_key = "YOUR_AZURE_API_KEY"
5. Executar o Script
Certifique-se de ter as imagens na pasta inputs e execute:


python recognize_text.py
6. Resultados
Os resultados do reconhecimento de texto serão salvos na pasta outputs em arquivos .txt correspondentes às imagens processadas.

Possibilidades e Insights
Durante o desenvolvimento deste projeto, aprendi sobre as capacidades e limitações do serviço OCR da Azure. A integração foi direta e a precisão do reconhecimento de texto foi satisfatória para diversas aplicações.

Contato
GitHub: fjbrit
LinkedIn: Fábio Brito



# GenAI Text Recognition

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Azure Cognitive Services](https://img.shields.io/badge/Azure%20Cognitive%20Services-OCR-brightgreen)


[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc) 

## Contato
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/fabiojbrito)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fjbrit)


## Descrição

Este projeto utiliza o serviço OCR (Optical Character Recognition) do Azure Cognitive Services para reconhecer e extrair texto de imagens. Foi desenvolvido como parte de um projeto educacional para a [DIO](https://www.dio.me/), demonstrando uma abordagem prática de reconhecimento de texto em imagens.

---

## Ferramentas Utilizadas

- **Linguagem de Programação**: Python 3.8+
- **Serviços de OCR**: Azure Cognitive Services OCR
- **Ambiente Virtual**: venv
- **Bibliotecas**:
  - `requests` para integração com o Azure


## Passo a Passo

### **1. Clonar o Repositório**

```bash
git clone https://github.com/fjbrit/GenAI-Text-Recognition.git
cd GenAI-Text-Recognition

2. Configurar o Ambiente Virtual

bash
python -m venv venv
source venv/Scripts/activate  # No Windows

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
Durante o desenvolvimento deste projeto, aprendi sobre as capacidades e limitações do serviço OCR da Azure.
A integração foi direta e a precisão do reconhecimento de texto foi satisfatória para diversas aplicações.


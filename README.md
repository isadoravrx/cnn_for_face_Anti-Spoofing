# CNN for Face Anti-Spoofing

## 📋 Passo a passo para reproduzir o código

### 1. Criar e ativar um ambiente virtual

Recomenda-se utilizar `venv` ou `conda`:

#### Usando venv
```bash
python -m venv venv
source venv/bin/activate 
```

### 2. Instalar as dependências

Instale os pacotes necessários com:

```bash
pip install -r requirements.txt
```

### 3. Baixar o dataset

Acesse o link abaixo para baixar o dataset:

[🔗 Real vs. Fake Face CNN Model - Kaggle](https://www.kaggle.com/code/abdalrhmanmorsi/real-vs-fake-face-cnn-model?select=real_vs_fake)

Após o download, extraia a pasta real_vs_fake e coloque dentro do diretório data/ na raiz do projeto:

```bash
/cnn_for_face_Anti-Spoofing
└── data/
    └── real_vs_fake/
```

### 4. Executar o notebook

Com tudo pronto, execute o notebook principal:

```bash
jupyter notebook experiment.ipynb
```

### Estrutura esperada do projeto

```bash
cnn_for_face_Anti-Spoofing/
├── experiment.ipynb              # Notebook principal com o experimento
├── load_real_fake_dataset.py     # Script para carregar o dataset
├── CDCNs.py                      # Implementação do modelo CNN
├── model/
│   └── cdcn_read_fake.pth        # Pesos treinados do modelo
├── data/
│   └── real_vs_fake/             # Dataset baixado do Kaggle
├── requirements.txt              # Dependências do projeto
├── .gitignore                    # Arquivos e pastas ignoradas pelo Git
└── README.md                     # Este arquivo
```


Referencias: https://github.com/ZitongYu/CDCN?tab=readme-ov-file
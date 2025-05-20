# CNN for Face Anti-Spoofing

## 📋 Passo a passo para reproduzir o código

### 1. Criar e ativar um ambiente virtual

Recomenda-se utilizar `venv` ou `conda`:

#### Usando venv
```bash
python -m venv myenv
source myenv/bin/activate 
```

### 2. Instalar as dependências

Instale os pacotes necessários com:

```bash
pip install -r requirements.txt
```

### 3. Baixar o dataset

Acesse o link abaixo para baixar o dataset:

[ 🔗 Dataset reduzido](https://universidadecatolica-my.sharepoint.com/:f:/g/personal/isadora_00000844511_unicap_br/EhtSKCrkC_lBlCH7qDSSqskBhbLPl6JKEYuKWUEYA4jMaw?e=sSHCnR)

Após o download, extraia a pasta real_vs_fake e coloque dentro do diretório data/ na raiz do projeto (Crie a pasta se ela não existir):

```bash
/data
├── real-vs-fake/
│   ├── train/
│   │   ├── fake/   ← imagens falsas usadas no treinamento
│   │   └── real/   ← imagens reais usadas no treinamento
│   │
│   └── test/
│       ├── fake/   ← imagens falsas usadas para teste
│       └── real/   ← imagens reais usadas para teste
```

### 4. Executar o notebook

Com tudo pronto, execute as células do notebook:

experiment.ipynb



### Estrutura do projeto

```bash
cnn_for_face_Anti-Spoofing/
├── experiment.ipynb              # Notebook principal com o experimento
├── load_real_fake_dataset.py     # Script para carregar o dataset
├── CDCNs.py                      # Implementação do modelo CNN
├── model/
│   └── cdcn_read_fake.pth        # Pesos treinados do modelo
├── data/
│   └── real_vs_fake/             # Dataset baixado do link compartilhado
├── requirements.txt              # Dependências do projeto
├── .gitignore                    # Arquivos e pastas ignoradas pelo Git
└── README.md                     # Este arquivo
```


Referencias: 
  - [🔗 Github do artigo](https://github.com/ZitongYu/CDCN?tab=readme-ov-file)
  - [🔗 Dataset reduzido](https://universidadecatolica-my.sharepoint.com/:f:/g/personal/isadora_00000844511_unicap_br/EhtSKCrkC_lBlCH7qDSSqskBhbLPl6JKEYuKWUEYA4jMaw?e=sSHCnR)
  - [🔗 Dataset Original](https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces)
  - [🔗 Artigo](https://arxiv.org/pdf/2003.04092)

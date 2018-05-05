# Quebra por força bruta da cifra playfair

## Autores:
 - Guilherme Bastos de Oliveira
 - Gabriel de Souza Barreto

## Compilação:
    crystal build quebra-pf.cr --release

## Execução:
    ./quebra-pf -d <arquivo-dicionario> -t <arquivo-texto-cifrado>

- **arquivo-dicionario:** arquivo que contem as chaves a serem testadas
- **arquivo-texto-cifrado:** arquivo que contem o texto a ser quebrado

## Arquivos:
### keys (diretório):
 - *keys3*: chaves de 3 caracteres
 - *keys4*: chaves de 4 caracteres
 - *keys5*: chaves de 5 caracteres
 - *keys345*: chaves de 3, 4 ou 5 caracteres
 - *keysX*: chaves para testes
 - *keysDict*: palavras entre 3 a 6 letras

### python-version (diretório):
 - primeira versão do código, foi muito lento, por isso refeito em Crystal

### textos (diretório):
 - *cifrado*: texto padrão a ser decifrado
 - *claro*: texto claro padrão

### utils (diretório):
 - *cifrador.py*: código em Python para cifrar textos
 - *clean_dict*: lista de palavras pt_BR sem caracteres especiais
 - *generators.py*: códigos para limpar dicionário e gerar listas de chaves

### *quebra-pf.cr*:
 - código principal

## Recursos Utilizados:
 -  [Python](https://www.python.org/)
 - [Crystal](https://crystal-lang.org/)
 - dict pt_BR (*/usr/share/dict/brazilian*)
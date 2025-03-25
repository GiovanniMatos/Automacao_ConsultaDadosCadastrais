# Automacao_ConsultaDadosCadastrais
Com o objetivo de otimizar o trabalho de um colaborador, desenvolvi este código que automatiza a extração e consulta de dados em um sistema do Governo. Onde através de uma vulnerabilidade, o captcha não se altera se o ID for válido.

<b>Foram usadas as bibliotecas Pyautogui, Pandas e Time</b><br>
```bash
pip install pandas pyautogui
```
Foi fornecida uma planilha com a respectiva coluna, que após executar o "tabela.py" foi extraida para um arquivo de texto "extraido.txt" que servirá de wordlist.

![image](https://github.com/GiovanniMatos/Automacao_ConsultaDadosCadastrais/assets/99231397/f2c17c55-a41b-4167-b485-fee9773aa195) <br>
O arquivo "coordenadas.py" teve a utilidade de pegar as coordenadas da tela para que pudessem receber os cliques necessarios usando Pyautogui, a biblioteca Time serviu para estabelecer um tempo até que as coordenadas de onde o cursor do mouse estava fossem capturadas.<br>

Executando o "main.py" com o site desejado aberto, coloque primeiramente o texto do Captcha, logo após ele começará a consultar cada matrícula do "extraido.txt" utilizando um único Captcha.
É importante que após executar, não encoste no mouse, pois a automação estará em andamento.

#### Caso as matrículas forem válidas, o captcha não atualiza, ou seja, o script de automação pode ser executado livremente
![Sem título](https://github.com/GiovanniMatos/Automacao_ConsultaDadosCadastrais/assets/99231397/4cc586e0-4b74-4dad-b672-b1c3a9ff3502)



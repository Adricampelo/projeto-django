from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import mysql.connector

# ✅ Função para buscar produtos com estoque abaixo do mínimo
def buscar_estoque_baixo():
    try:
        # Conectar ao MySQL
        conexao = mysql.connector.connect(
            host="localhost",    # Ajuste conforme necessário
            user="root",
            password="",
            database="whatstock"
        )

        # Verifica se a conexão foi estabelecida corretamente
        if conexao.is_connected():
            print("✅ Conexão com o banco de dados estabelecida com sucesso!")

        cursor = conexao.cursor(dictionary=True)

        # Consulta SQL: busca produtos com estoque abaixo do mínimo
        query = """
        SELECT nome, estoque, estoque_minimo 
        FROM produtos_produto 
        WHERE estoque < estoque_minimo
        """
        cursor.execute(query)
        produtos_alerta = cursor.fetchall()

        cursor.close()
        conexao.close()
        print("✅ Conexão encerrada com sucesso!")

        # Criar a mensagem de alerta
        if produtos_alerta:
            mensagem = "⚠️ ALERTA DE ESTOQUE BAIXO ⚠️\n"
            for produto in produtos_alerta:
                mensagem += f"{produto['nome']}: {produto['estoque']} em estoque (Mínimo: {produto['estoque_minimo']})\n"
        else:
            mensagem = "✅ Todos os produtos estão com estoque suficiente."

    except mysql.connector.Error as e:
        mensagem = f"❌ Erro ao conectar ao banco de dados: {e}"
        print(mensagem)

    return mensagem



# ✅ Inicializa o navegador
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

# ✅ Aguarda o carregamento do WhatsApp Web
print("Aguardando o carregamento do WhatsApp Web...")
while len(navegador.find_elements(By.ID, 'side')) < 1:
    sleep(1)
print("WhatsApp Web carregado com sucesso!")

# ✅ Dicionários para armazenar o estado da conversa
ultima_saudacao = {}  # Tempo da última saudação enviada por contato
ultima_mensagem = {}   # Última mensagem recebida de cada contato

# ✅ Função para capturar a última mensagem recebida e o nome do contato
def capturar_ultima_mensagem():
    try:
        mensagens = navegador.find_elements(By.XPATH, '//div[contains(@class,"message-in")]')

        if mensagens:
            ultima_mensagem_elemento = mensagens[-1]
            nova_msg = ultima_mensagem_elemento.find_element(By.XPATH, './/span[contains(@class,"selectable-text")]').text.strip()

            contato = navegador.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/div/span').text.strip()

            return contato, nova_msg
    except Exception as e:
        print(f"Erro ao capturar mensagem: {e}")
    return None, None

# ✅ Loop principal do chatbot
while True:
    try:
        # Verifica notificações no painel lateral
        notificacoes = navegador.find_elements(By.XPATH, '//*[@id="pane-side"]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span')

        if notificacoes:
            print(f"Nova mensagem detectada! Total: {len(notificacoes)}")
            notificacoes[0].click()  # Abre a conversa com notificação
            print("Entrou na conversa.")
            sleep(2)

        # Captura a última mensagem recebida
        contato, nova_msg = capturar_ultima_mensagem()

        if nova_msg and contato:
            # Se for a mesma mensagem já processada, ignora para evitar loops
            if ultima_mensagem.get(contato) == nova_msg:
                print(f"Mensagem já processada de {contato}: '{nova_msg}', ignorando...")
                continue  # Pula para a próxima iteração

            print(f"Nova mensagem de {contato}: '{nova_msg}'")
            ultima_mensagem[contato] = nova_msg  # Atualiza o histórico de mensagens

            input_msg = navegador.find_element(By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')

            tempo_atual = time()
            tempo_ultima_saudacao = ultima_saudacao.get(contato, 0)

            # ✅ Se for a primeira mensagem ou já se passaram 5 minutos, envia a saudação
            if contato not in ultima_saudacao or (tempo_atual - tempo_ultima_saudacao) > 300:
                input_msg.send_keys("Olá! Eu sou o chatbot! Escolha uma opção:\n1 - Adicionar produto\n2 - Visualizar alertas de estoque")
                input_msg.send_keys(Keys.RETURN)
                print("Mensagem de boas-vindas enviada.")
                ultima_saudacao[contato] = tempo_atual  # Atualiza o tempo da última saudação

            # ✅ Se o usuário já recebeu a saudação e enviou uma opção válida
            elif nova_msg == "1":
                input_msg.send_keys("Vou listar seu produto!")
                input_msg.send_keys(Keys.RETURN)
                print("Resposta enviada: listar produto")

            elif nova_msg == "2":
                mensagem_alerta = buscar_estoque_baixo()  # Busca estoque baixo no banco
                input_msg.send_keys(mensagem_alerta)
                input_msg.send_keys(Keys.RETURN)
                print("Resposta enviada: Estoque baixo")

            # ✅ Mensagem inválida
            elif nova_msg.lower() not in ["1", "2"]:
                input_msg.send_keys("Desculpe, não entendi. Tente novamente.")
                input_msg.send_keys(Keys.RETURN)
                print("Resposta enviada: Opção inválida.")

        else:
            print("Sem novas mensagens.")

        sleep(5)

    except Exception as e:
        print(f"Erro detectado: {e}")
        break


# ✅ Encerra o navegador ao finalizar
navegador.quit()

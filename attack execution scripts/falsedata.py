import time
import random
import paho.mqtt.publish as publish
import json

# Configurações
broker_ip = "10.42.0.1"
taxa_mensagens = 100 
duracao_envio = 30   
intervalo = 1.0 / taxa_mensagens

while True:
    print("Iniciando envio de mensagens por 20s...")
    inicio = time.time()

    while time.time() - inicio < duracao_envio:
        
        velocidade = random.randint(0, 100)
        angulo = random.randint(-111, 0)
        vbat = random.randint(0, 809)

        
        payload_velocidade = json.dumps({"velocidade": velocidade, "angulo": angulo})
        payload_bateria = json.dumps({"vbat": vbat})

        
        publish.single("robo/comandos", payload=payload_velocidade, hostname=broker_ip)
        print(f"→ robo/comandos: {payload_velocidade}")

        publish.single("robo/bateria", payload=payload_bateria, hostname=broker_ip)
        print(f"→ robo/bateria: {payload_bateria}")

        time.sleep(intervalo)

    print("Envio concluído.")
    break

import subprocess
import time
import paho.mqtt.publish as publish

# Configurações
broker_ip = "10.42.0.1"
topic_mqtt = "ataque/tipo"


'''========================================================================='''
'''DOS ATTACK'''

publish.single(topic_mqtt, payload=f"START:DoS", hostname=broker_ip)
print(f" -> START:DoS")

subprocess.run([
"wsl",
"bash", "-c",
"cd /mnt/c/Users/mathe/OneDrive/Documentos/GitHub/mqttsa && python3 mqttsa.py -fc 100 10.42.0.1"
])
time.sleep(1)

# End message to mark attack
publish.single(topic_mqtt, payload=f"END:DoS", hostname=broker_ip)
print(f" -> END:DoS")

# intervall between attacks
time.sleep(10)


'''====================================================================='''
'''MALFORMED ATTACK'''

publish.single(topic_mqtt, payload=f"START:Malformed", hostname=broker_ip)
print(f" -> START:Malformed")

subprocess.run([
"wsl",
"bash", "-c",
"cd /mnt/c/Users/mathe/OneDrive/Documentos/GitHub/mqttsa && python3 mqttsa.py --md 10.42.0.1"
])

time.sleep(1)

publish.single(topic_mqtt, payload=f"END:Malformed", hostname=broker_ip)
print(f" -> END:Malformed")

time.sleep(10)

'''====================================================================='''
'''FALSE-DATA-INJECTION ATTACK'''

publish.single(topic_mqtt, payload=f"START:Falsedata", hostname=broker_ip)
print(f" -> START:Falsedata")

subprocess.run([
"wsl",
"bash", "-c",
"python3 false_data.py"
])

time.sleep(1)

publish.single(topic_mqtt, payload=f"END:Falsedata", hostname=broker_ip)
print(f" -> END:Falsedata")

time.sleep(10)
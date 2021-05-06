# Recon/Reconhecimento
os testes da semana seram feitos no lab fornecido pela CrowSec Segurança Ofensiva.
- Cenário:
    > A empresa chamada CS Hosting nos contratou para que nós realizassemos um pentest (achar, explorar e identificar as vulnerabilidades) dentro de sua estrutura.

- Dados:
    > Aparenta ser uma empresa de hospedagem com serivdores dedicados;
    
    > Dominio: cshosting.crowsec.com.br

    > Aparenta ter três categorias de servidores disponíveis:
        >> servidor compartilhado;
        >> servidor dedicado;
        >> cloud vps.
    
    > O cloud load balancing aparenta ser da aws pelo fato de no descritivo mencionar as siglas ALB/ELB;

    > Aparenta que para realizar qualquer operação no site primeiro é preciso que o cliente esteja logado, é feito um redirecionamento para a página /login e dps a própria página do /login redireciona para a página /login/public ao clicar em abrir ticket ou área do cliente, por exemplo.

    > 

- Repos:
    > Repositorio com listas para fazer fuzzing e entre outras coisas https://github.com/danielmiessler/SecLists

    > Automatizador de analise de aplicações laravel https://github.com/carlosevieira/larasploit

---

## Comandos
```bash
# mapeando as portas disponiveis no host
$ nmap cshosting.crowsec.com.br -vvv # -vvv habilita o modo verbose do nmap para ver o log de output

$ nmap -Pn -sV -A cshosting.crowsec.com.br -oA scan-output -vvv # -Pn não envia icmp para que o firewall não bloqueie o scan; -sV enumera as versões dos serviços rodando; -A inicializa e roda os scripts do nmap dentro de cada porta que for possivel a conexão; -oA exporta todo o output do nmap pra dentro de um arquivo 

# tentando acessar um ftp
$ ftp 54.166.65.130 # pacote que realiza conexão ftp com um ip informado 

# tentando conectar no ssh
$ ssh 54.166.65.130 # pacore que realiza a conexão via ssh com o servidor informado

# tentando resolver um dns apartir do ip
$ dig @54.166.65.130 cshosting.com.br # dig faz parte do pacote dnsutils

# realizando webfuzzing (busca por diretorios, rotas e arquivos com base numa lista de palavras chaves)
$ wfuzz -t 100 -Z -c -z file,lista.txt --hc 404 https://cshosting.crowsec.com.br/FUZZ # -t especifica a quantidade de threads que vão ser usadas; -Z indica que será rodado em modo scan o pacote do wfuzz para que sejam ignorados os erros durante os testes ; -c colore o output; -z especifica a lista que vai ser utilizada; --hc especifica qual o status code que vai ser escondido; o FUZZ é onde o pacote vai pegar o valor da linha e trocar e construir a url

```

> Link do notion do Kadu: https://www.notion.so/SWH-Recon-dd4176f908cd47f08472c05a877ae2b1
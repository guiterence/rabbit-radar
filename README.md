# RABBIT RADAR

## Descrição
O RABBIT RADAR é um sistema de visão computacional para detectar objetos perigosos (como armas e facas) em ambientes públicos, utilizando a rede neural YOLO. Ao identificar objetos, o sistema alerta a equipe de segurança e armazena as informações para análise futura.

## Estrutura de Diretórios
- **core/api**: API Flask para gerenciar as detecções e notificações.
- **core/detection**: Serviço responsável por processar imagens e identificar objetos utilizando YOLO.
- **core/notifications**: Serviço que lida com o envio de alertas e notificações.
- **core/README.md**: Documentação geral do projeto.

## Instruções de Instalação

### Construir e Rodar a API
```bash
cd core/api
docker build -t rabbit-radar-api .
docker run -it --rm -p 8000:8000 rabbit-radar-api

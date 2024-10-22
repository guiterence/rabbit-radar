# RABBIT RADAR

## Descrição
O RABBIT RADAR é um sistema de visão computacional para detectar objetos perigosos (como armas e facas) em ambientes públicos, utilizando a rede neural YOLO. Ao identificar objetos, o sistema alerta a equipe de segurança e armazena as informações para análise futura.

## Estrutura de Diretórios
- **core/api**: API Flask para gerenciar as detecções e notificações.
- **core/yolo-database**: Serviço responsável por processar imagens e identificar objetos utilizando YOLO.
- **core/notifications**: Serviço que lida com o envio de alertas e notificações.
- **core/camera-service**: Serviço que lida com o processamento de imagens.
- **README.md**: Overview do projeto.
- **Documentação oficial**: https://docs.google.com/document/d/1DZLOp_9J9l8P6gXI-vfxZS-2CkWUhs2Nuj99PEx1u6o/edit?usp=sharing
- **Arquitetura oficial**: https://drive.google.com/file/d/1YVkCtLEH1OL6KO6LBundrApkS_raI70s/view?usp=sharing

## Instruções de Instalação

### Construir e Rodar a API
docker-compose up --build

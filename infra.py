import pulumi
import pulumi_docker as docker

config = pulumi.Config()

porta_backend = config.get_int("backend_port") or 8001
porta_frontend = config.get_int("frontend_port") or 8042

network = docker.Network("escola-network")

def criar_container(nome, imagem, porta_interna, porta_externa):
    return docker.Container(
        nome,
        image=imagem,
        ports=[
            {
                "internal": porta_interna,
                "external": porta_externa,
            }
        ],
        networks_advanced=[{
            "name": network.name, 
        }]
    )

backend = criar_container("api-container", "gabiribeiro/api-escola:latest", 8000, porta_backend)
frontend = criar_container("web-container", "gabiribeiro/web-escola:latest", 80, porta_frontend)

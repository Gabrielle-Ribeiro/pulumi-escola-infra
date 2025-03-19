import pulumi
import pytest
from pulumi.runtime import set_mocks
import infra

class PulumiMocks:
    def new_resource(self, args):
        return {
            "id": args.name,
            "urn": f"urn:pulumi:stack::project::{args.type}::{args.name}",
            **args.inputs,
        }

    def call(self, args):
        return {}

@pytest.fixture(scope="module", autouse=True)
def setup_pulumi():
    set_mocks(PulumiMocks())


def test_verifica_rede():
    assert infra.network._name == "escola-network"

def test_verifica_criacao_container_backend():
    def check_backend(image):
        assert image == "gabiribeiro/api-escola:latest"

    infra.backend.image.apply(check_backend) 

def test_verifica_criacao_container_frontend():
    def check_frontend(image):
        assert image == "gabiribeiro/web-escola:latest"

    infra.frontend.image.apply(check_frontend)    
from typing import List
import pytest
from tests.factories import product_data
from fastapi import status

# Testes para a API de produtos

async def test_create_product_should_return_success(client, products_url):
    """
    Testa a criação de um novo produto.
    """
    response = await client.post(products_url, json=product_data())
    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_get_product_should_return_success(client, products_url, product_inserted):
    """
    Testa a obtenção dos detalhes de um produto pelo ID.
    """
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_get_product_should_return_not_found(client, products_url):
    """
    Testa a obtenção de um produto inexistente.
    """
    response = await client.get(f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }

# ... (outros testes)

async def test_delete_product_should_return_not_found(client, products_url):
    """
    Testa a exclusão de um produto inexistente.
    """
    response = await client.delete(f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }

import asyncio
from uuid import UUID
import pytest
from store.db.mongo import db_client
from store.schemas.product import ProductIn
from tests.schemas.factories import product_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mongo_client():
    return db_client.get()

@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_name= await mongo_client.get_database().list_collection_names()
    for collection_name in collections_name:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})

@pytest.fixture
def product_id():
    return UUID("fce6cc37-10b9-4a8c-a8b2-977df327001a")

@pytest.fixture
def product_in():
    return ProductIn(**product_data(),id=product_id)
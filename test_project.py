from project import get_id, get_team, search_player
import pytest_asyncio
import pytest

async def main():
    test_get_id()
    test_get_team()
    test_search_player

@pytest.mark.asyncio
async def test_get_id():
    assert await get_id("Mount") == 142
@pytest.mark.asyncio
async def test_get_team():
    assert await get_team(1) == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 313, 607]

@pytest.mark.asyncio
async def test_search_player():
    assert await get_id("Test") == None

def get_choice():
    pass

def search_team():
    pass

def search_position():
    pass

def create_table():
    pass

if __name__ == "__main__":
    main()
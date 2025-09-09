from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()

# Fake database of items
fake_items_db = [{"item_name": "Zoo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    Fetch a list of items with pagination.
    - skip: number of items to skip (for pagination)
    - limit: max number of items to return
    """
    # Return a slice of the fake_items_db based on skip and limit
    return fake_items_db[skip : skip + limit]

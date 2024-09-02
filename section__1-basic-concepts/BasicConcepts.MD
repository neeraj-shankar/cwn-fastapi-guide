# FastAPI Python

## Pydantic Model
- Pydantic models are used to define data schemas that are validated and parsed automatically.
- These models are typically used for defining request bodies, query parameters, and response data structures. 
- Pydantic models provide data validation, type checking, and conversion, making it easier to ensure that the data your application processes is accurate and consistent.

### Basic Usage of Pydantic Models in FastAPI

#### Defining a Pydantic Model
```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
```
- **name:** A required string field.
- **description:** An optional string field (None is the default value).
- **price:** A required float field.
- **tax:** An optional float field.

#### Using the Model in FastAPI Endpoints
- FastAPI will automatically validate the incoming data against the Pydantic model.
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```
In this example, when a POST request is made to `/items/` with a JSON body, FastAPI will validate the JSON against the Item model. If the validation passes, the item parameter in the `create_item` function will be an instance of the Item model.

#### Response Models
Pydantic models can also be used as response models to ensure that the data returned by the API is correctly structured.
```python
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
```

#### Model Validation and Serialization
Pydantic models provide powerful validation features:

- **Automatic Conversion:** Pydantic can automatically convert compatible types. For example, if a field expects an int but receives a string that can be converted to an int, Pydantic will do the conversion.
- **Data Validation:** Pydantic validates data types, ensuring that the data conforms to the specified type.

#### Nested Models
```python
class User(BaseModel):
    username: str
    email: str

class Item(BaseModel):
    name: str
    price: float
    owner: User
```
In this example, the `Item` model has an owner attribute, which is itself a `User` model.

#### Default Values and Field Validation
You can provide default values and custom validation for fields.
```python
from pydantic import Field

class Item(BaseModel):
    name: str = Field(..., title="Name of the item")
    price: float = Field(..., gt=0, description="The price must be greater than zero")
```
- **Field:** Provides metadata and validation for individual fields.
- **gt=0:** Ensures that the price is greater than zero.



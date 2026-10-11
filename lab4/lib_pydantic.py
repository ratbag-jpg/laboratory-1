from pydantic import BaseModel
def use_pydantic():
    class User(BaseModel):
        name: str
        id: int
    u = User(name="Admin", id=1)
    print(f"pydantic: Валідовано користувача -> {u}")
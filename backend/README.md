###### Некоторые ручки
**Создание пользователя**:
POST: api/auth/users/
```json
{
    "username": "Обязательное поле.",
    "password": "Обязательное поле."
}

```

**Получение JWT-токена:**
POST: api/auth/jwt/create/
```json
{
    "username": "Обязательное поле.",
    "password": "Обязательное поле."
}

```

**Получение списка категорий с подкатегориями:**
GET: api/v1/categories/?limit=1&offset=0
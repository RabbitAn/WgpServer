from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "role" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255),
    "password" VARCHAR(255) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "phone" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "roles" (
    "id" UUID NOT NULL PRIMARY KEY,
    "role_name" VARCHAR(50) NOT NULL UNIQUE,
    "description" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "user_roles" (
    "id" UUID NOT NULL PRIMARY KEY,
    "assigned_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "role_id" UUID NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmf1P4jAYx/8Vsp808YwieOZyuYQ3T06BC447ozFL2cpo3FrcOpEY/vdry17Lho5ghH"
    "O/EHj6PKz9tH2eb7sXxSYGtNzDgQsd5VvpRcHAhuxLwn5QUsBkElm5gYKhJRw95iEsYOhS"
    "B+iUGUfAciEzGdDVHTShiGBmxZ5lcSPRmSPCZmTyMHr0oEaJCelYdOTunpkRNuAzdIOfkw"
    "dthKBlJPqJDP5sYdfobCJsg0G7eS48+eOGmk4sz8aR92RGxwSH7p6HjEMew9tMiKEDKDRi"
    "w+C99IcbmBY9ZgbqeDDsqhEZDDgCnsVhKN9HHtY5g5J4Ev+o/FBy4NEJ5mgRppzFy3wxqm"
    "jMwqrwRzUuav29k9N9MUriUtMRjYKIMheBgIJFqOAageTzKL4v4WyMgZOOMx4jQWUdfh+c"
    "Aab12Ck2eNYsiE06Zj/L1eoKmH9qfcGTeQmghK3uxZrv+k3lRRsHG4F0iJULYuC/GYCBIS"
    "IYbcadQQhtgKw8DMOAtSD6a+z/YjgBrjslTkp6zMYYjymWY1RjXI3VNfSUsq3rhO1egDOq"
    "TTxO4jlkge8FNMyZmy4v9V7vinfadt1HSxjaqsRx0Km3+nvHAi9zQlSY211VYqo7kI9aA3"
    "QZapO1UGTDdKrJSAmr4YceBl+2dNGyMRg9bM382VrBXG13WtdqrfM7Ab5ZU1u8pSysM8m6"
    "dyot7/BPSn/b6kWJ/yzd9rotWSeEfuqtwvsEPEo0TKYaMGLFOLAGYJJ5h01HrvoXBnzu3M"
    "0V7ughJs24YQj0hylwDC3RkhRtGhcQbkpq8mPPL/vQAmKUy5BjMr/v65Dt2y3zYMkE1mDX"
    "cESkTLKgLTfZZVu2AAxM0Wv+bP4kH4nAkXIiCjBln4jC+ShORDt9IuLzqOU9EiWCdvFMVD"
    "16Qz6rHmWmM96ULPXxbi2RVOEzTScphe1IdVhVyVs3aqKIB9D2OrWb/UQhv+p1fwbuMciN"
    "q1690FGfQ0d5E2PNiU1GFhP7oRMb6pTc2k5UkvB2tdB2G9R2IZKMG+/XNV5SeBdCb6eFHn"
    "BdZOK1cq0UWiTbLauiIonm2yixkE3ulg+Vnq9uDulKIR+xWMhnIbZU0ZMAl+mdEweyTHEJ"
    "Z4Jhm/UDYD3tlCi9ed1aakslm5kdMA0LVXxZsOGxQcHFZXCjdt2oNVvKG96a5aa2e0JHph"
    "ZLP+nUsrXje0qmGnSQPk4TTH7LSrkEIp+tkUptnHHxkJrJ+IRJ68qfvQ+9ujH5U76Ujytf"
    "K2cnp5Uz5iJ6Elq+rshxwVuZbGX0xE4fqdc22RdgsZDiFWIkMdnWyAHRd99NgMdHb7lCZF"
    "6ZAEWbdM9FMIU4RZ//uu51My64ohAJ5ACzAd4ZSKcHJQu59H47sa6gyEe9+i5RvjaUdAz/"
    "g3q+106bLy/zf5TAY1s="
)

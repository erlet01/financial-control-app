from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum

class TransactionTypeEnum(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

# User Schemas
class UserRegister(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

# Account Schemas
class AccountCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    account_type: str
    initial_balance: float = 0.0
    currency: str = "BRL"
    description: Optional[str] = None

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    account_type: Optional[str] = None
    balance: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class AccountResponse(BaseModel):
    id: int
    name: str
    account_type: str
    balance: float
    initial_balance: float
    currency: str
    is_active: bool
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Category Schemas
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    color: str = "#4CAF50"
    icon: Optional[str] = None
    category_type: TransactionTypeEnum

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    is_active: Optional[bool] = None

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    color: str
    icon: Optional[str]
    category_type: TransactionTypeEnum
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# Transaction Schemas
class TransactionCreate(BaseModel):
    account_id: int
    category_id: int
    amount: float = Field(..., gt=0)
    description: Optional[str] = None
    transaction_type: TransactionTypeEnum
    transaction_date: datetime
    payment_method: Optional[str] = None
    tags: Optional[str] = None
    is_recurring: bool = False
    recurrence_frequency: Optional[str] = None
    notes: Optional[str] = None

class TransactionUpdate(BaseModel):
    account_id: Optional[int] = None
    category_id: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    transaction_type: Optional[TransactionTypeEnum] = None
    transaction_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    tags: Optional[str] = None
    notes: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    account_id: int
    category_id: int
    amount: float
    description: Optional[str]
    transaction_type: TransactionTypeEnum
    transaction_date: datetime
    payment_method: Optional[str]
    tags: Optional[str]
    is_recurring: bool
    notes: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

# Report Schemas
class FinancialSummary(BaseModel):
    total_income: float
    total_expenses: float
    net_balance: float
    account_count: int
    transaction_count: int
    last_transaction: Optional[datetime]

class CategoryReport(BaseModel):
    category: str
    type: TransactionTypeEnum
    total: float
    percentage: float
    count: int

class MonthlySummary(BaseModel):
    month: str
    income: float
    expenses: float
    balance: float

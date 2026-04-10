from typing import Optional

from sqlmodel import Field, SQLModel


class Repository(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    description: str | None = None
    language: str | None = None
    stars: int = 0
    forks: int = 0
    open_issues_count: int = 0
    health_score: float = 0.0


class Opportunity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    repo_id: int = Field(foreign_key="repository.id")
    issue_number: int
    title: str
    labels: str = ""
    score: float = 0.0
    difficulty: str = "unknown"
    status: str = "discovered"
    brief_markdown: str = ""

from sqlmodel import SQLModel, Session, create_engine, select

from app.models import Opportunity, Repository


def test_repository_and_opportunity_persist_to_sqlite():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        repository = Repository(
            full_name="MosslandOpenDevs/moss-contribution-radar",
            description="Contribution discovery platform",
            language="Python",
            stars=10,
            forks=2,
            open_issues_count=5,
            health_score=82.5,
        )
        session.add(repository)
        session.commit()
        session.refresh(repository)

        opportunity = Opportunity(
            repo_id=repository.id,
            issue_number=42,
            title="Build the first scoring pass",
            labels="good first issue,help wanted",
            score=91.0,
            difficulty="medium",
            status="shortlisted",
            brief_markdown="Start with repository activity heuristics.",
        )
        session.add(opportunity)
        session.commit()

        stored_repo = session.exec(select(Repository)).one()
        stored_opp = session.exec(select(Opportunity)).one()

    assert stored_repo.full_name == "MosslandOpenDevs/moss-contribution-radar"
    assert stored_opp.repo_id == repository.id
    assert stored_opp.issue_number == 42
    assert stored_opp.status == "shortlisted"

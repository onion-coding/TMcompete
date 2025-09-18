from session import Session
from models import Competition
from datetime import datetime, timezone

session = Session()

# Create a test competition
test_comp = Competition(
    title="Test Event",
    description="This is a test competition",
    date_start=datetime.now(timezone.utc),
    date_end=None,
    type="Tournament",
    created_by=1
)

session.add(test_comp)
session.commit()

print(f"Inserted competition with ID: {test_comp.id}")

session.close()

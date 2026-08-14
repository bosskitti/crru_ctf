import json
from CTFd import create_app
from CTFd.models import Challenges, db

app = create_app()

desc_21_add = """
    <div class="mt-3 p-3" style="background: rgba(0, 240, 255, 0.08); border: 1px dashed rgba(0, 240, 255, 0.3); border-radius: 4px; font-family: 'Outfit', sans-serif !important;">
        <p class="mb-0" style="color: var(--accent-cyan); font-size: 0.9rem; line-height: 1.5;">
            💡 <strong>Note</strong>: This container instance hosts all 3 Path Traversal Labs. You can use this single instance to solve Labs 1, 2, and 3.
        </p>
    </div>
"""

desc_22_add = """
    <div class="mt-3 p-3" style="background: rgba(168, 85, 247, 0.08); border: 1px dashed rgba(168, 85, 247, 0.3); border-radius: 4px; font-family: 'Outfit', sans-serif !important;">
        <p class="mb-0" style="color: var(--accent-purple); font-size: 0.9rem; line-height: 1.5;">
            💡 <strong>Note</strong>: Use the active container instance started in <strong>Lab 1: File Path Traversal (Simple Case)</strong> to solve this challenge.
        </p>
    </div>
"""

desc_23_add = """
    <div class="mt-3 p-3" style="background: rgba(255, 0, 127, 0.08); border: 1px dashed rgba(255, 0, 127, 0.3); border-radius: 4px; font-family: 'Outfit', sans-serif !important;">
        <p class="mb-0" style="color: var(--accent-pink); font-size: 0.9rem; line-height: 1.5;">
            💡 <strong>Note</strong>: Use the active container instance started in <strong>Lab 1: File Path Traversal (Simple Case)</strong> to solve this challenge.
        </p>
    </div>
"""

with app.app_context():
    # Update Challenge 21
    c21 = Challenges.query.get(21)
    if "Note:" not in c21.description:
        c21.description = c21.description + desc_21_add
        print("Updated Challenge 21 description.")

    # Update Challenge 22 (Convert to standard static challenge)
    c22 = Challenges.query.get(22)
    if c22.type != "standard":
        c22.type = "standard"
        print("Converted Challenge 22 to standard.")
    if "Note:" not in c22.description:
        c22.description = c22.description + desc_22_add
        print("Updated Challenge 22 description.")

    # Update Challenge 23 (Convert to standard static challenge)
    c23 = Challenges.query.get(23)
    if c23.type != "standard":
        c23.type = "standard"
        print("Converted Challenge 23 to standard.")
    if "Note:" not in c23.description:
        c23.description = c23.description + desc_23_add
        print("Updated Challenge 23 description.")

    # Optionally clean up Whale entries for 22 and 23 to avoid conflicts
    try:
        from CTFd.plugins.ctfd_whale.models import WhaleChallenge
        WhaleChallenge.query.filter(WhaleChallenge.id.in_([22, 23])).delete(synchronize_session=False)
        print("Removed WhaleChallenge entries for 22 and 23.")
    except Exception as e:
        print(f"Skipped WhaleChallenge deletion: {e}")

    db.session.commit()
    print("Database committed successfully!")

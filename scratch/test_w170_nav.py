import json
from CTFd import create_app
from CTFd.models import db, Users

app = create_app()
ctx = app.app_context()
ctx.push()

# Simulating logged in request using Flask test client
client = app.test_client()

# Let us find or create a user, log in, and fetch page
# (In CTFd, if we bypass login, we can also check if view_lesson renders next_position properly)
# To do it easily, we can inspect how next_position is contextually passed in flask render_template!
# Let us mock the route view_lesson directly using app.test_request_context:
with app.test_request_context("/tutorials/2/3"):
    from CTFd.plugins.tutorials import TutorialModule
    module = TutorialModule.query.filter_by(id=2).first()
    lessons = module.lessons.all()
    lesson_position = 3
    lesson = lessons[lesson_position - 1]
    
    prev_position = lesson_position - 1 if lesson_position > 1 else None
    next_position = lesson_position + 1 if lesson_position < len(lessons) else None
    
    print("Lesson ID:", lesson.id)
    print("Lesson Title:", lesson.title)
    print("next_position variable passed:", next_position)

# Let us also test fetch of raw response with a mock user session
user = Users.query.filter_by(id=1).first() # Usually id=1 is admin or first user
if user:
    with client.session_transaction() as sess:
        sess['id'] = user.id
        sess['name'] = user.name
        sess['type'] = user.type
        sess['nonce'] = 'testnonce'
        
    res = client.get("/tutorials/2/3")
    print("Response status code:", res.status_code)
    html = res.data.decode("utf-8", errors="ignore")
    print("Is 'Next Lesson' string in HTML output?", "Next Lesson" in html)
    
    # Print the exact navigation section of the HTML response
    if "Next Lesson" in html:
        idx = html.find("Next Lesson")
        print("HTML snippet around Next Lesson:")
        print(html[idx-150 : idx+150])
    else:
        # If not present, find 'Previous Lesson' instead to see the nav buttons block
        if "Previous Lesson" in html:
            idx = html.find("Previous Lesson")
            print("HTML snippet around Previous Lesson:")
            print(html[idx-100 : idx+500])
        else:
            print("Neither Next Lesson nor Previous Lesson found in HTML!")
            print("HTML Length:", len(html))
            print("First 200 chars of body:")
            print(html[:1000])

ctx.pop()

from datetime import datetime
from api.models.polls import Poll, PollAnswer, QuestionType


polls = {
    "1": Poll(
        id="1",
        question="Do you like your job ?",
        questionType=QuestionType.STANCE,
        options=[],
        answers=[
            PollAnswer(
                id="1",
                text="I don't really like my job, even though it pays well. The main reason is that I'm working for someone else's vision and goals, which leaves me feeling dependent and unfulfilled. While I appreciate that I'm improving my skills, I would prefer to pursue my own ideas and lead projects that reflect my vision. The French hiring system complicates things further since it tends to limit experimentation and openness to diverse backgrounds. This environment adds to my frustration, as it makes it harder to explore and implement my innovative ideas.",
                createdAt=datetime.now()
            ),
            PollAnswer(
                id="2",
                text="I love my job. I find it helps me becoming a better person, because the work i put into it and the desire to always strive for the best, along with some pressure, gave me a method i can apply in other areas of my life and I have become a high-agency person.",
                createdAt=datetime.now()
            ),
            PollAnswer(
                id="3",
                text="I like my job, or rather I have stopped asking me that question because I don't really feel like this is the matter. To me, job is mostly a social bond and whatever work I do, it only provides me something if I work with people I respect and that respect me.",
                createdAt=datetime.now()
            )
        ],
        isTextBased=True,
        createdAt=datetime.now()
    )
}
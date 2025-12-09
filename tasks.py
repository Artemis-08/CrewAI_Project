from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

## researcher task
research_task = Task(
    description="Research high-quality and relevant information for blog posts from YouTube videos on the topic {topic}.",
    expected_output="A summarized version of the relevant video content on the topic {topic} suitable for blog content creation.",
    tools=[yt_tool],
    agent=blog_researcher,
)

## writer task
writer_task = Task(
    description="Create a well-structured and captivating blog post on the topic {topic} from the researched YouTube content.",
    expected_output="A complete blog post on the topic {topic} that is engaging, informative, and well-organized.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="blog_post_{topic}.md",
)


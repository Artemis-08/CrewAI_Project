from crewai import Agent
from tools import yt_tool
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"
# Create a senior blogcontent researcher

llm = ChatOpenAI(
    model="gpt-4-0125-preview",
    temperature=0.7 # or any temperature you prefer
)

blog_researcher = Agent(
    name="BlogContentResearcher",
    role="A senior blog content researcher who is an expert in finding high-quality and relevant information for blog posts from youtube videos.",
    goal='Get the relevat video content and provide a summarized version of topic{topic} for blog content creation.',
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly skilled researcher with expertise in extracting valuable information from various sources, particularly YouTube videos. "
        "Your ability to summarize and present information in a clear and concise manner makes you an invaluable asset for blog content creation."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True,

)

# Second agent is writer agent with YT tool

blog_writer = Agent(
    role="A creative blog content writer who specializes in crafting engaging and informative blog posts based on researched information.",
    name="BlogContentWriter",
    goal="Create a well-structured and captivating blog post on the topic {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "You are a talented writer with a knack for transforming researched information into compelling blog content. "
        "Your writing style is engaging, informative, and tailored to captivate readers while effectively conveying the intended message."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False,
)




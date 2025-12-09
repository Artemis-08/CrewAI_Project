import patch_signal  # Windows compatibility patch
from crewai import Crew,Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writer_task

crew = Crew(
    agents=[blog_researcher, blog_writer],
    process=Process.sequential,
    tasks=[research_task, writer_task],
    memory = True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

## starrt the task executiuon process with enhanced feedback

result = crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})
print(result)
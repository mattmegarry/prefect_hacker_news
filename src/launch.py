from prefect import flow, task
from database.create_pg_schema import create_pg_schema

create_pg_schema()

@task
def scrape_ask_page_questions():
    return ["234123234", "23451435"]

@task
def scrape_response_page_responses(question_id):
    print(f"Scraping responses for question {question_id}")

@flow(name="scrape-hn")
def scrape(base_url):
    print(base_url + " is the url")
    questions = scrape_ask_page_questions()
    for question_id in questions:
        scrape_response_page_responses(question_id)

if __name__ == "__main__":
    scrape.serve(name="scrape-hn-deployment", tags=["hackernews"], parameters={"base_url": "https://news.ycombinator.com/ask"}, interval=10)
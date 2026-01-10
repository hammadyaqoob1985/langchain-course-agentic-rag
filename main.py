from dotenv import load_dotenv

from graph.graph import app
load_dotenv

def main():
    print("Hello from langchain-course-agentic-rag!")
    print(app.invoke(input={"question": "What is agent memory?"}))


if __name__ == "__main__":
    main()

import langchain

def get_prompt():

    prompt = """Translate the text that is delimited by triple backticks into {language}. \
    text: ```{text}```
    """
    from langchain.prompts import ChatPromptTemplate
    prompt_template = ChatPromptTemplate.from_template(prompt)
    print(prompt_template.format(language='english', text='aaa'))

    from langchain.prompts import PromptTemplate
    prompt_template = PromptTemplate.from_template("""Tell me a {adjective} joke about {content}""")
    print(prompt_template.format(adjective="funny", content="chickens"))

def invoke():
    from langchain.llms import OpenAI
    llm = OpenAI()
    print(llm('你是谁'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get_prompt()
    invoke()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

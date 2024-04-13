from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from .prompt import SystemPrompt


class LLM:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-pro", temperature=0.5, convert_system_message_to_human=True
        )
        self._template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=SystemPrompt.journal),
                HumanMessagePromptTemplate.from_template("{text}"),
            ]
        )
        self._parser = JsonOutputParser()

        self.__random_journal = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=SystemPrompt.random_journal),
                HumanMessagePromptTemplate.from_template("{text}"),
            ]
        )

    def user_prompt(self, text) -> list[BaseMessage]:
        chat_message = self._template.format_messages(text=text)
        return chat_message

    @property
    def chain(self):
        return self.model | self._parser

    def get_journal(self, chat_message: list[BaseMessage]) -> dict:
        journal = self.chain.invoke(chat_message)
        return journal

    def get_random_journal(self) -> dict:
        random_journal = self.chain.invoke(self.__random_journal.format_messages(text=""))
        return random_journal

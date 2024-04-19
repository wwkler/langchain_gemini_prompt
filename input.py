from langchain.prompts import PromptTemplate

class SystemPromptSetting:
    def __init__(self, text):
        self.text = text
        
    def promptSetting(self):
        #Create the retrieval chain
        template = """
        You are a helpful AI assistant.
        Answer based on the context provided.
        context: {context}
        input: {input}
        answer: """
        
        prompt = PromptTemplate.from_template(template) 
        return prompt
        
        
        
        
        
        
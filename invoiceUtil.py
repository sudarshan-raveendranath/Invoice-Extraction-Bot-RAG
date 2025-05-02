import tempfile

from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def create_docs(user_pdf_list):
    """This function is used to extract the invoice data from the given PDf files.
    it uses the langchain library to extract the data from given PDF files.
    """

    for uploaded_file  in user_pdf_list:

        #Extract PDF data
        print("Processing - ", uploaded_file.name)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file .read())
            tmp_path = tmp_file.name

        loader = PyPDFLoader(tmp_path)
        pages = loader.load_and_split()

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        vector = FAISS.from_documents(pages, embeddings)

        template = """Extract all the following values : invoice no., Description, Quantity, date, Unit price, Amount, Total, email, phone number
        and address from the following Invoice content (create a JSON output with the extracted fields only):
        {context}
        The fields and values in the above context may be jumbled up as they are extracted from a PDF. 
        Please extract the fields and values correctly based on the fields asked for in the question above.
        Expected JSON output format as follows:
        {{'Invoice no.':xxxxxxxx','Description':'xxxxxxxx','Quantity':'x','Date':'dd/mm/yyyy','Unit price':'xxx.xx','Amount':'xxx.xx',
        'Total':'xxx.xx','email':'xxx@xxx.xxx','phone number':'xxxxxxxx','address':'xxxxxxxx'}}
        Remove any dollar symbols or currency symbols from the extracted values."""

        prompt = ChatPromptTemplate.from_template(template)

        llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro", google_api_key = os.getenv("GOOGLE_API_KEY"), temperature = 0)
        retriever = vector.as_retriever()
        document_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        response = retrieval_chain.invoke({"input": ""})
        answer_content = response["answer"]
        print("Extracted Data:")
        print(answer_content)

        print("**********************************************")

    return answer_content
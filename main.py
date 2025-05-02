#This RAG application takes in an invoice PDF, loads the data into a vector database,
#send the invoice information as context to the gemini model and
#comes back with extracted details

import streamlit as st
from dotenv import load_dotenv
import invoiceUtil as iu

def main():
    load_dotenv()

    st.set_page_config(page_title="Invoice Extraction Bot")
    st.title("Invoice Extraction Bot...👨‍💻")
    st.subheader("I can help you extract information from invoices.")

    # Upload the PDF file
    pdf = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

    submit = st.button("Extract Invoice")

    if submit:
        with st.spinner('Wait for it...'):
            df = iu.create_docs(pdf)
            st.write(df)

        st.success("Hope this helps you extract the information you need from the invoice.")


#Invoking main function
if __name__ == "__main__":
    main()


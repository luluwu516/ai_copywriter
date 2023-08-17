import openaiimport streamlit as stfrom functions import copy_writerdef main():        st.set_page_config(        page_title="AI Copywriter",        page_icon="random",    )    st.header("AI Copywriter")        article = st.text_area("Please enter copy content: ",                          placeholder="Ex: Taiwanese boba tea")    platform = st.selectbox(        'Select a social media platform:',        ('Facebook',         'Instagram',         'Linkedln'         ))    optimization = st.selectbox(        'How would you like to optimize this copy?',        ('Extend',         'Condense',         'Paraphrase'         ))    style = st.multiselect(        'Select article style(s) (multiple selections possible): ',        ['Attractive',          'Enthusiastic',          'Emotional',         'Friendly',         'Lighthearted',         'Formal',         'Persuasive',          'Pragmatic',          'Professional',          ])        language = st.selectbox(        'Select a language: ',        ('English',         '繁體中文',         ))        length = st.number_input("Enter the maximum length of the article: ", 100, 1024)    if st.button("Generate"):        api_key = "sk-YOUR_API_KEY"        # call the function        response = copy_writer(api_key, article, platform, optimization, style, language, length)        results = st.text_area('Result:', response, height=300)if __name__ == '__main__':    main()
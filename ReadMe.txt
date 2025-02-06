### **Project: English to French Translator App**

#### **Description**
This Streamlit application translates English text to French. It uses a pre-trained transformer model from Hugging Face to perform the translation. Users can enter multiple lines of text, and the translated text will be shown line by line. The app also includes a reset button to clear both the input and output fields.

#### **Features**
- **English to French Translation**: Using the Hugging Face translation model to translate the input English text to French.
- **Line-by-Line Translation**: Preserves the original line breaks in the translation.
- **Reset Functionality**: Clears output after pressing the reset button.

---

### **Usage**

1. **Install Dependencies**: Install the required Python libraries using the `requirements.txt`.
   
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**:
   After installing the dependencies, run the Streamlit app with the following command:
   
   ```bash
   streamlit run main.py
   ```

3. **Interacting with the App**:
   - Enter your English text in the text area.
   - Click the "Translate" button to see the French translation of the input text.
   - Use the "Reset" button to clear the input and translated text.

---

### **Code Walkthrough**

1. **Importing the Libraries**: 
   - We import the necessary libraries, such as `pipeline` from Hugging Face and `streamlit` for the app interface.

2. **Session State**:
   - `input_text` and `translated_lines` are stored in `st.session_state` to preserve the text entered and translated across multiple interactions with the app.

3. **Text Area**:
   - The `input_text` is entered in a text area. This text is split by lines to preserve the line structure when translating.

4. **Translation Logic**:
   - On clicking the "Translate" button, the input text is passed to the model for translation. The translation result for each line is stored in a list and displayed line by line.

5. **Reset Button**:
   - The reset button clears the `translated_lines` in session state.

---

### **requirements.txt**

```txt
streamlit==1.10.0
transformers==4.12.5
sentencepiece==0.1.96
```

---

### **Troubleshooting**
- If you face issues with model loading or the translation, ensure you have an active internet connection to access the Hugging Face model.
- The "Reset" button works only if there is something written in the text area.

---

### **How to Contribute**
- If you'd like to contribute to the functionality of the reset button or improve the user interface, feel free to fork the repository and submit a pull request.

---

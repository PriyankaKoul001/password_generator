# Advanced Password Generator

Welcome to the **Advanced Password Generator** project! This app allows users to generate strong passwords based on customizable criteria, including the number of uppercase letters, lowercase letters, digits, and special characters. It uses **FastAPI** as the backend and **Streamlit** as the frontend to provide a smooth user experience.

## 🚀 Features

- Generate a secure password by specifying:
  - Length of the password
  - Number of uppercase letters
  - Number of lowercase letters
  - Number of digits
  - Number of special characters
- Copy the generated password to your clipboard with a single click.
- Easy-to-use UI with interactive sliders for customizing password strength.
- Built using **FastAPI** for the backend and **Streamlit** for the frontend.

## 🔧 Installation

Follow these steps to set up the project locally:

### 1. Clone the repository and Install Requirements:

```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

- Install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Set up the backend (FastAPI):

- Navigate to the backend folder:

```bash
cd backend
```

- Run the FastAPI server:

```bash
uvicorn main:app --reload
```

By default, the backend will be available at `http://localhost:8000`.

### 3. Set up the frontend (Streamlit):

- Navigate to the frontend folder:

```bash
cd ../frontend
```

- Run the Streamlit app:

```bash
streamlit run app.py
```

The Streamlit app will open at `http://localhost:8501`.

##Note 
In the frontend app.py change the backend api url to the local url while running in local.

## ⚙️ Configuration

Both the frontend and backend are designed to be customizable:

- **Frontend**: The `frontend/app.py` file allows you to configure the UI layout, password generation parameters, and other visual elements.
- **Backend**: The `backend/app.py` file handles the password generation logic. You can modify the algorithm or add additional rules for password complexity.

## 🖥️ Usage

1. Open the Streamlit app in your browser.
2. Customize the password settings by adjusting the sliders for length, uppercase letters, lowercase letters, digits, and special characters.
3. Click the **"Generate Password"** button to create a new password.
4. Copy the password to your clipboard using the **"Copy Password"** button.

## 🔗 Connect with Me

- [LinkedIn](https://www.linkedin.com/in/your-profile)
- [GitHub](https://github.com/your-profile)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 🎉 Happy password generating! 🎉

---

### Explanation:

- **Installation**: Instructions for setting up the **backend (FastAPI)** and **frontend (Streamlit)**.
- **Usage**: Describes how users can interact with the app.
- **Connect with Me**: Links to your LinkedIn and GitHub profiles.
- **License**: Included a standard MIT license statement (you can change it as per your requirements).

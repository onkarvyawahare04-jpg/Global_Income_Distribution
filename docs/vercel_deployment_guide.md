# 🚀 Detailed Vercel Deployment Guide

This guide provides a comprehensive, step-by-step walkthrough for deploying your restructured Global Income Distribution Analytics (GIDA) dashboard to Vercel.

---

## 📋 Prerequisites

Before you begin, ensure you have:
1.  **Vercel Account**: Sign up at [vercel.com](https://vercel.com) (Pro or Hobby).
2.  **GitHub Account**: Your project should be in a GitHub repository.
3.  **Local Project Ready**: All files moved to `frontend/`, `backend/`, etc.

---

## 🛠️ Step 1: Prepare Your Code

I have already initialized the following for you:
-   **`vercel.json`**: Acts as the project's brain on Vercel, mapping URLs and setting up the Python runtime.
-   **`requirements.txt` (root)**: Vercel looks for this specifically at the top level to install your Python dependencies (`Flask`, `pandas`, etc.).
-   **`backend/app.py`**: Refactored to handle the new directory structure.

### How to get and set your SECRET_KEY
A `SECRET_KEY` is a random string used to secure your user sessions. Here is how to get it and set it:

1.  **Generate a Key**: You can use this random key I generated for you:
    `1d2a879aeace023c2ce97e8e7be9e641b40f30d1958604bf`
2.  **Add to Vercel**:
    - Go to your project on the [Vercel Dashboard](https://vercel.com/dashboard).
    - Navigate to **Settings** -> **Environment Variables**.
    - **Key**: `SECRET_KEY`
    - **Value**: Paste the key from step 1 here.
    - Click **Add**.

---

## 📤 Step 2: Deployment Methods

### Method A: The GitHub Way (Recommended)
1.  **Push to GitHub**:
    ```bash
    git init
    git add .
    git commit -m "Restructure for deployment"
    git remote add origin YOUR_REPO_URL
    git push -u origin main
    ```
2.  **Import to Vercel**:
    - Go to [vercel.com/new](https://vercel.com/new).
    - Connect your GitHub account and select your repository.
    - **Configuration**: Vercel will automatically detect `vercel.json`.
    - **Environment Variables**: Click "Environment Variables" and add:
        - `SECRET_KEY`: (Any long random string)
    - Click **Deploy**.

### Method B: Vercel CLI (Quickest)
1.  Install CLI: `npm install -g vercel`
2.  In your project folder, run: `vercel`
3.  Follow the prompts (defaults are fine).
4.  To deploy to production later: `vercel --prod`

---

## 💾 Step 3: Handling the Database

> [!IMPORTANT]
> **Vercel is Serverless.** This means the filesystem is wiped every few minutes. 
> 
> - **Current Setup**: SQLite (`instance/database.db`) is read-only. It will work for showing the dashboard, but you cannot sign up new users or save feedback.
> - **Solution**: You MUST move to a persistent database for a "Real" deployment.

### Recommended Persistent Database: Vercel Postgres
1.  Go to your Vercel project dashboard.
2.  Click **Storage** -> **Postgres** -> **Create**.
3.  Connect it to your project.
4.  Update your `instance/database.db` connection in `app.py`:
    ```python
    # Update this line in backend/app.py:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL', 'sqlite:///database.db').replace("postgres://", "postgresql://")
    ```

---

## 🔍 Troubleshooting Common Issues

| Error | Cause | Fix |
| :--- | :--- | :--- |
| **500 Internal Server Error** | Missing dependency or code error. | Check "Logs" in Vercel Dashboard. |
| **Static files not loading** | `vercel.json` routing issue. | Ensure `static/` is inside `frontend/`. |
| **ModuleNotFoundError** | Dependency missing in `requirements.txt`. | Add the missing module to root `requirements.txt`. |
| **Read-only Database** | Trying to write to SQLite on Vercel. | Switch to Vercel Postgres as described above. |

---

## ✅ Deployment Checklist
- [ ] `vercel.json` is in the root directory.
- [ ] `requirements.txt` is in the root directory.
- [ ] `backend/app.py` has `template_folder` and `static_folder` correctly set.
- [ ] `SECRET_KEY` is set in Vercel Environment Variables.
- [ ] All `.xlsx` files are in the `dataset/` folder.

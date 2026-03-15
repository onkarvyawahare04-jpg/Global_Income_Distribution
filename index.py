from backend.app import app

# This entry point is required for Vercel deployment
# It allows Vercel to correctly identify the Flask application
# while maintaining your organized directory structure.

if __name__ == "__main__":
    app.run()

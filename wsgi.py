from app import app

# Gunicorn entry point: `wsgi:app`
# If you want to run this file directly for local tests:
if __name__ == '__main__':
    app.run()



# django-url-shortener

A simple Django-based URL shortener with a web interface.

## 1. Setup

**Create virtual environment:**
```
python -m venv venv
```

**Activate virtual environment (Windows):**
```
.\venv\Scripts\activate
```

**Deactivate:**
```
deactivate
```

**Install dependencies:**
```
pip install -r requirements.txt
```
## 2. Usage

1. Run migrations:
   ```
   python manage.py migrate
   ```

2. Create superuser:
   ```
   python manage.py createsuperuser
   ```

3. Start the server:
   ```
   python manage.py runserver
   ```
   
4. Open [http://localhost:8000](http://localhost:8000) in your browser.

## 3. Features

- **Shorten URLs:**  
  Enter a long URL to generate a short URL.  
  (Frontend powered by Alpine.js)

- **Expand URLs:**  
  Enter a short URL to retrieve the original long URL.  
  (Frontend powered by Alpine.js)

- **Redirection:**  
  Accessing `localhost/<10-character-hash>` redirects to the original URL.

- **Admin Panel:**  
  Django admin enabled.  
  Superuser: `admin` (set password as needed)

- **Prettified Forms:**  
  Uses Bootstrap and django-crispy-forms for better UI.  
  - [Bootstrap 4 Forms with Django](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
  - [YouTube Tutorial](https://www.youtube.com/watch?v=6-XXvUENY_8)

## 4. TODO

- [ ] Add user authentication
- [ ] Analytics for shortened URLs
- [ ] Custom short URL aliases

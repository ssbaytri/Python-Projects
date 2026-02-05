# Simple Social - FastAPI Social Media App

A simple social media application built with FastAPI and Streamlit that allows users to share images and videos with captions.

## Features

- 🔐 User authentication (register/login) with JWT tokens
- 📸 Image and video uploads
- 🖼️ Cloud storage with ImageKit
- 📱 Feed with posts from all users
- 🗑️ Delete your own posts
- 💬 Captions with text overlay on media

## Tech Stack

**Backend:**
- FastAPI - Modern web framework
- SQLAlchemy - ORM with async support
- SQLite - Database (with aiosqlite)
- FastAPI Users - Authentication system
- ImageKit - Cloud media storage

**Frontend:**
- Streamlit - Quick UI framework

## Prerequisites

- Python 3.8 or higher
- ImageKit account (free tier available)

## Setup Instructions

### 1. Clone or Download the Project

```bash
# If using git
git clone <your-repo-url>
cd simple-social

# Or just download and extract the files
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn[standard] sqlalchemy aiosqlite fastapi-users[sqlalchemy] python-multipart streamlit imagekitio python-dotenv
```

Or create a `requirements.txt` file with:

```
fastapi
uvicorn[standard]
sqlalchemy
aiosqlite
fastapi-users[sqlalchemy]
python-multipart
streamlit
imagekitio
python-dotenv
```

Then install:
```bash
pip install -r requirements.txt
```

### 4. Get ImageKit Credentials

1. Go to [ImageKit.io](https://imagekit.io/) and sign up for a free account
2. After logging in, go to **Developer Options** in the dashboard
3. You'll need three things:
   - **Private Key**
   - **Public Key** 
   - **URL Endpoint**

### 5. Create Environment File

Create a `.env` file in the project root:

```bash
# .env
IMAGEKIT_PRIVATE_KEY=your_private_key_here
IMAGEKIT_PUBLIC_KEY=your_public_key_here
IMAGEKIT_URL_ENDPOINT=https://ik.imagekit.io/your_id
SECRET=your_secret_key_for_jwt_here
```

**Generate a secure SECRET key:**
```bash
# Run in Python
python -c "import secrets; print(secrets.token_hex(32))"
```

### 6. Update imagekit_client.py

Make sure your `imagekit_client.py` includes all required fields:

```python
from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT")
)
```

## Project Structure

```
simple-social/
├── app/
│   ├── app.py              # Main FastAPI application
│   ├── db.py               # Database models and setup
│   ├── schemas.py          # Pydantic schemas
│   ├── users.py            # User authentication logic
│   └── imagekit_client.py  # ImageKit configuration
├── frontend.py             # Streamlit frontend
├── main.py                 # Entry point to run the app
├── .env                    # Environment variables (don't commit!)
├── .gitignore
├── requirements.txt
└── README.md
```

## Running the Application

### Option 1: Run Backend and Frontend Separately

**Terminal 1 - Start FastAPI Backend:**
```bash
python main.py
```
The API will be available at `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

**Terminal 2 - Start Streamlit Frontend:**
```bash
streamlit run frontend.py
```
The app will open in your browser at `http://localhost:8501`

### Option 2: Using Uvicorn Directly

```bash
uvicorn app.app:app --reload
```

Then in another terminal:
```bash
streamlit run frontend.py
```

## Usage

1. **Sign Up**: Enter your email and password, click "Sign Up"
2. **Login**: Use your credentials to login
3. **Upload**: Go to the Upload page, select an image or video, add a caption, and share
4. **Feed**: View all posts from all users
5. **Delete**: Click the 🗑️ button on your own posts to delete them

## Supported File Types

**Images:**
- PNG
- JPG/JPEG

**Videos:**
- MP4
- AVI
- MOV
- MKV
- WEBM

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/jwt/login` - Login and get JWT token
- `POST /auth/jwt/logout` - Logout
- `GET /users/me` - Get current user info

### Posts
- `POST /upload` - Upload a new post (requires auth)
- `GET /feed` - Get all posts (requires auth)
- `DELETE /posts/{post_id}` - Delete a post (requires auth + ownership)

## Database

The app uses SQLite with async support (aiosqlite). The database file `test.db` will be created automatically on first run.

**Tables:**
- `user` - User accounts
- `posts` - User posts with media URLs

## Security Notes

- JWT tokens expire after 1 hour (3600 seconds)
- Passwords are hashed using bcrypt
- Only post owners can delete their posts
- File uploads are validated by content type

## Troubleshooting

### "Failed to get user info" error
- Make sure the `/users/me` endpoint is correctly registered
- Check that the JWT token is being sent in headers

### ImageKit upload fails
- Verify your `.env` file has correct credentials
- Check that all three ImageKit variables are set (private_key, public_key, url_endpoint)
- Ensure your ImageKit account is active

### Database errors
- Delete `test.db` and restart to recreate the database
- Make sure you have write permissions in the project directory

### Port already in use
- Change the port in `main.py`: `uvicorn.run(..., port=8001)`
- Or kill the process using port 8000

## Future Improvements

- [ ] Add pagination to feed
- [ ] Add likes and comments
- [ ] User profiles with avatars
- [ ] Follow/unfollow users
- [ ] Search functionality
- [ ] Email verification
- [ ] Password reset via email
- [ ] Image/video size limits
- [ ] Better error handling

## Contributing

Feel free to fork this project and submit pull requests!

## License

MIT License - feel free to use this project for learning or building your own apps.

## Acknowledgments

- FastAPI Users library for authentication
- ImageKit for media storage
- Streamlit for quick frontend development
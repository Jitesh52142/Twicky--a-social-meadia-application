# ⚡ Twicky Quick Start Guide

Get Twicky up and running in under 5 minutes!

---

## 🚀 Local Development Setup

### 1️⃣ Clone & Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd twicky

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Configure Environment

Create a `.env` file in the project root:

```env
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
MONGODB_URI=mongodb+srv://Jitesh001:Jitesh001@twicky.fxotzly.mongodb.net/
```

### 3️⃣ Setup Database

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 4️⃣ Run Server

```bash
python manage.py runserver
```

Visit: `http://localhost:8000` 🎉

---

## 🌐 Quick Deploy to Vercel

### Prerequisites
- Vercel account
- MongoDB Atlas account (already configured)

### Deploy Steps

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel

# Follow prompts, then add environment variables
vercel env add SECRET_KEY
vercel env add DEBUG
vercel env add ALLOWED_HOSTS
vercel env add MONGODB_URI

# Deploy to production
vercel --prod
```

**Done!** Your app is live! 🚀

---

## 🎯 Essential URLs

- **Home:** `/`
- **Tweet Feed:** `/twicky/`
- **Login:** `/account/login/`
- **Register:** `/account/register/`
- **Create Tweet:** `/twicky/create/`
- **Admin Panel:** `/admin/`

---

## 🔑 Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `SECRET_KEY` | Yes | Django secret key | `django-insecure-...` |
| `DEBUG` | Yes | Debug mode | `True` or `False` |
| `ALLOWED_HOSTS` | Yes | Allowed domains | `localhost,127.0.0.1,.vercel.app` |
| `MONGODB_URI` | Yes | MongoDB connection | `mongodb+srv://...` |

---

## 🛠️ Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

---

## 📱 Test Features

After setup, test these features:

1. ✅ Register a new account
2. ✅ Login with your account
3. ✅ Create a tweet (with/without image)
4. ✅ Edit your tweet
5. ✅ Delete your tweet
6. ✅ Logout
7. ✅ Login again

---

## 🆘 Troubleshooting

### Issue: "Module not found"
```bash
pip install -r requirements.txt
```

### Issue: "Database connection failed"
- Check MongoDB URI is correct
- Verify internet connection
- Check MongoDB Atlas IP whitelist

### Issue: "Static files not loading"
```bash
python manage.py collectstatic --noinput
```

### Issue: "Port already in use"
```bash
python manage.py runserver 8001
```

---

## 📚 Need More Help?

- **Full Documentation:** See `README.md`
- **Deployment Guide:** See `DEPLOYMENT.md`
- **Changelog:** See `CHANGELOG.md`

---

## 🎉 You're Ready!

Start building amazing features with Twicky! 🚀

Happy coding! 💻


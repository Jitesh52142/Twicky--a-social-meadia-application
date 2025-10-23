# 🚀 Vercel Deployment Guide for Twicky

## ⚠️ Current Issue: 500 Internal Server Error

Your deployment is showing a `FUNCTION_INVOCATION_FAILED` error. This is common with Django on Vercel due to serverless limitations.

---

## 🔧 Quick Fix Steps

### 1. **Update Environment Variables in Vercel Dashboard**

Go to your Vercel project settings → Environment Variables and add:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.vercel.app
DJANGO_SETTINGS_MODULE=twiky_project.settings
VERCEL=1
```

**Generate a new SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. **Simplify requirements.txt for Vercel**

Vercel has limitations on package size. Use the minimal `requirements-vercel.txt`:

```
Django==4.2.11
dj-database-url==2.3.0
django-environ==0.12.0
gunicorn==23.0.0
pillow==11.1.0
python-decouple==3.8
whitenoise==6.9.0
```

### 3. **Update vercel.json**

The updated `vercel.json` is now simpler and more compatible.

### 4. **Redeploy**

```bash
vercel --prod
```

---

## 🚨 Important Vercel Limitations

### 1. **File Upload Issues**
Vercel's serverless functions are **ephemeral** - uploaded files won't persist between requests.

**Solution:** Use cloud storage for media files:
- AWS S3
- Cloudinary
- Vercel Blob Storage

### 2. **Database**
Vercel serverless functions need an external database.

**Options:**
- Vercel Postgres
- MongoDB Atlas
- PlanetScale
- Supabase

### 3. **Cold Starts**
First request after inactivity may be slow (5-10 seconds).

---

## 🎯 Recommended Alternative Platforms

Given Twicky's features (image uploads, database), consider these platforms instead of Vercel:

### 1. **Railway** (Recommended ⭐)

**Why Railway?**
- ✅ Persistent storage
- ✅ PostgreSQL included
- ✅ Easy file uploads
- ✅ No serverless limitations
- ✅ Free tier available

**Deployment:**
1. Sign up at [railway.app](https://railway.app)
2. Connect GitHub repository
3. Add PostgreSQL service
4. Set environment variables
5. Deploy automatically

**Environment Variables for Railway:**
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=.railway.app
DATABASE_URL=postgresql://... (auto-generated)
```

### 2. **Render** (Also Great ⭐)

**Why Render?**
- ✅ Persistent disk storage
- ✅ PostgreSQL included
- ✅ Easy deployment
- ✅ Free tier available

**Deployment:**
1. Sign up at [render.com](https://render.com)
2. Connect GitHub repository
3. Use existing `render-build.sh`
4. Set environment variables
5. Deploy

### 3. **PythonAnywhere**

**Why PythonAnywhere?**
- ✅ Django-specific hosting
- ✅ File uploads work perfectly
- ✅ SQLite or MySQL
- ✅ Free tier available

### 4. **DigitalOcean App Platform**

**Why DigitalOcean?**
- ✅ Full VPS control
- ✅ Managed databases
- ✅ No serverless limitations
- ✅ $200 credit for new users

---

## 🔄 If You Still Want to Use Vercel

### Step-by-Step Fix

#### 1. **Remove Heavy Dependencies**

Rename `requirements.txt` to `requirements-local.txt` and create new `requirements.txt`:

```bash
mv requirements.txt requirements-local.txt
cp requirements-vercel.txt requirements.txt
```

#### 2. **Configure External Storage (Cloudinary Example)**

Install cloudinary:
```bash
pip install django-cloudinary-storage
```

Update `settings.py`:
```python
# Add to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'cloudinary_storage',
    'cloudinary',
    # ...
]

# Configure Cloudinary
import cloudinary

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

#### 3. **Use Vercel Postgres or External Database**

Add to `settings.py`:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}
```

#### 4. **Update ALLOWED_HOSTS**

In Vercel dashboard, set:
```
ALLOWED_HOSTS=your-app-name.vercel.app,.vercel.app
```

#### 5. **Disable Admin Static Files**

The Django admin may not work properly on Vercel. Consider using Railway/Render for admin access.

---

## 📋 Deployment Checklist for Any Platform

- [ ] Database configured (external)
- [ ] Media storage configured (cloud)
- [ ] SECRET_KEY set (strong, unique)
- [ ] DEBUG=False
- [ ] ALLOWED_HOSTS configured
- [ ] Static files collected
- [ ] Migrations applied
- [ ] Environment variables set
- [ ] Test deployment

---

## 🎯 My Recommendation

**Use Railway or Render instead of Vercel** for this project because:

1. ✅ Image uploads work natively
2. ✅ Database included
3. ✅ Easier setup
4. ✅ No serverless limitations
5. ✅ Better for Django apps

### Quick Railway Deployment

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Add PostgreSQL
railway add

# Deploy
railway up
```

That's it! Your app will be live with persistent storage and database.

---

## 🐛 Common Vercel Errors & Fixes

### Error: FUNCTION_INVOCATION_FAILED

**Causes:**
- Large dependencies
- Missing environment variables
- Database connection issues
- django-extensions not compatible

**Fix:**
1. Use minimal requirements
2. Set all environment variables
3. Use external database
4. Remove django-extensions from production

### Error: 500 Internal Server Error

**Causes:**
- DEBUG=True shows actual error
- Missing SECRET_KEY
- Wrong ALLOWED_HOSTS

**Fix:**
1. Check Vercel logs
2. Set all environment variables
3. Ensure ALLOWED_HOSTS includes .vercel.app

### Error: Static files not loading

**Causes:**
- collectstatic not run
- Wrong STATIC_URL

**Fix:**
1. Run collectstatic during build
2. Use WhiteNoise (already configured)
3. Check STATIC_ROOT setting

---

## 📞 Need Help?

1. **Check Vercel Logs:** Vercel Dashboard → Your Project → Deployments → View Logs
2. **Enable DEBUG temporarily:** Set DEBUG=True to see actual error (don't forget to disable after)
3. **Check Settings:** Verify all environment variables are set correctly

---

## ✅ Recommended Solution

**Switch to Railway for the best experience:**

1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Add PostgreSQL service
4. Set environment variables (same as above)
5. Deploy!

Railway will automatically detect your Django app and deploy it correctly with persistent storage, database, and no serverless limitations.

---

**Good luck with your deployment! 🚀**

**Built with 💙 by Jitesh Bawaskar**


# ⚠️ Important: Vercel Deployment with SQLite

## Current Configuration

Due to Vercel's serverless architecture limitations, the application is currently configured to use **SQLite** instead of MongoDB for Vercel deployments.

### Why SQLite for Vercel?

1. **Serverless Environment**: Vercel runs on serverless functions which have limitations:
   - No persistent filesystem
   - Cold starts
   - Read-only filesystem after build

2. **Django + MongoDB Compatibility**: 
   - Djongo has compatibility issues with newer Python versions
   - Serverless environments don't work well with stateful database connections

### Current Setup

The application will work perfectly on Vercel with SQLite, but **data will not persist between deployments** due to Vercel's read-only filesystem.

---

## ✅ Recommended Solutions for Production

### Option 1: Use Railway (Recommended for MongoDB)

Railway supports full MongoDB integration with persistent storage:

1. **Sign up**: https://railway.app
2. **Deploy from GitHub**: Connect your repository
3. **Add MongoDB**: Use Railway's MongoDB addon
4. **Configure**: Set environment variables
5. **Deploy**: Automatic deployment

**Advantages:**
- Full MongoDB support
- Persistent storage
- Container-based (not serverless)
- Easy to use
- Free tier available

### Option 2: Use Render

Render provides persistent disk storage:

1. **Sign up**: https://render.com
2. **New Web Service**: Connect GitHub
3. **Build Command**: `pip install -r requirements.txt && python manage.py migrate`
4. **Start Command**: `gunicorn twiky_project.wsgi:application`
5. **Add Disk**: For media files
6. **Deploy**

**Advantages:**
- Persistent storage
- Full database support
- Container-based
- Free tier

### Option 3: Use PythonAnywhere

Traditional hosting with full database support:

1. **Sign up**: https://www.pythonanywhere.com
2. **Upload code**
3. **Set up virtual environment**
4. **Configure WSGI**
5. **Deploy**

**Advantages:**
- Traditional hosting
- Full control
- Easy setup
- Free tier

---

## 🔧 For Vercel with Persistent Data

If you want to use Vercel, you have two options:

### Option A: External MongoDB (Current)

Keep SQLite for local but use **MongoDB Atlas** for data:

1. Create custom MongoDB connector in views
2. Store tweets in MongoDB Atlas
3. Use SQLite only for Django auth

### Option B: Use Vercel Postgres

1. Add Vercel Postgres addon
2. Update `DATABASES` setting
3. Use PostgreSQL instead of MongoDB

---

## 🚀 Quick Deploy to Railway (MongoDB Support)

### Step 1: Prepare for Railway

Update `settings.py` to use MongoDB:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'twicky',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': config('MONGODB_URI'),
        }
    }
}
```

Update `requirements.txt`:
```
djongo==1.3.6
pymongo==3.12.3
```

### Step 2: Create `railway.json`

```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn twiky_project.wsgi:application",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Step 3: Create `Procfile`

```
web: gunicorn twiky_project.wsgi --log-file -
```

### Step 4: Deploy

1. Go to https://railway.app
2. **New Project** → **Deploy from GitHub**
3. Select your repository
4. Add MongoDB service
5. Connect MongoDB to your app
6. Deploy!

---

## 📊 Comparison

| Platform | MongoDB | Persistent | Free Tier | Ease |
|----------|---------|-----------|-----------|------|
| **Vercel** | ❌ Limited | ❌ | ✅ Yes | ⭐⭐⭐⭐⭐ |
| **Railway** | ✅ Yes | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐ |
| **Render** | ✅ Yes | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐ |
| **PythonAnywhere** | ✅ Yes | ✅ Yes | ✅ Yes | ⭐⭐⭐ |

---

## 🎯 Recommendation

**For this project with MongoDB:**

1. **Development**: Use SQLite locally (fast, simple)
2. **Production**: Deploy to **Railway** with MongoDB
3. **Alternative**: Use **Render** with PostgreSQL

**Current Vercel deployment** will work for:
- Demo purposes
- Portfolio showcase
- Testing functionality
- Non-persistent data

---

## 🔄 Switching from Vercel to Railway

1. **Update settings.py** - Switch back to MongoDB config
2. **Update requirements.txt** - Add djongo back
3. **Push to GitHub**
4. **Deploy on Railway** - Connect repository
5. **Add MongoDB service** - In Railway dashboard
6. **Configure environment variables**
7. **Deploy!**

See `RAILWAY_DEPLOYMENT.md` (I'll create this) for detailed instructions.

---

## ✅ Current Status

- ✅ Application works on Vercel
- ✅ All features functional
- ⚠️ Data not persistent (SQLite on read-only filesystem)
- ✅ Perfect for demos and portfolio
- ✅ Ready to switch to Railway/Render for production

---

## 📝 Note

The codebase maintains both configurations:
- **Vercel**: SQLite (current)
- **Railway/Render**: MongoDB (ready to enable)

Switch between them by updating `settings.py` and `requirements.txt`.

---

**For production with persistent MongoDB, deploy to Railway instead of Vercel.**

See detailed Railway deployment guide in `RAILWAY_DEPLOYMENT.md`.


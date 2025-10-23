# 🚀 Render Manual Setup Guide

## ⚠️ If Blueprint Deployment Failed

If you're seeing `ModuleNotFoundError: No module named 'app'`, follow these manual steps:

---

## 📝 **MANUAL DEPLOYMENT STEPS**

### **Step 1: Delete Current Service**
1. Go to your Render dashboard
2. Find the failed `twicky-social-media` service
3. Go to Settings → Delete Web Service

### **Step 2: Create New Web Service Manually**

1. Click "**New +**" → "**Web Service**"
2. Connect your GitHub repository
3. Select: `Jitesh52142/Twicky--a-social-meadia-application`

### **Step 3: Configure Settings**

**Basic Settings:**
- **Name**: `twicky-social-media`
- **Region**: Oregon (or closest to you)
- **Branch**: `main`
- **Root Directory**: (leave blank)
- **Runtime**: `Python 3`
- **Build Command**:
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput --clear && python manage.py migrate --noinput
  ```
- **Start Command**:
  ```bash
  gunicorn --bind 0.0.0.0:$PORT twiky_project.wsgi:application
  ```

**Instance Type:**
- **Plan**: `Free`

### **Step 4: Add Environment Variables**

Click "Advanced" → Add these variables:

```
PYTHON_VERSION = 3.11.9
DEBUG = False
SECRET_KEY = django-insecure-#sla7u9uuva*6v+4gt3)whx2mf74+fc715w8punbo24rmpzzjr
ALLOWED_HOSTS = .onrender.com
DJANGO_SETTINGS_MODULE = twiky_project.settings
```

### **Step 5: Create PostgreSQL Database**

1. Go back to Dashboard
2. Click "**New +**" → "**PostgreSQL**"
3. **Name**: `twicky-db`
4. **Region**: Same as web service
5. **Plan**: `Free`
6. Click "**Create Database**"

### **Step 6: Connect Database**

1. Go to your database (`twicky-db`)
2. Copy the "**Internal Database URL**"
3. Go back to your web service
4. Environment → Add Environment Variable:
   - **Key**: `DATABASE_URL`
   - **Value**: (paste the database URL)

### **Step 7: Deploy**

1. Click "**Create Web Service**"
2. Wait 3-5 minutes
3. Watch the logs

---

## ✅ **EXPECTED RESULT**

You should see:
```
==> Build successful 🎉
==> Deploying...
==> Your service is live 🎉
```

Your app will be at: `https://twicky-social-media.onrender.com`

---

## 🚨 **COMMON ISSUES**

### **Issue: Still seeing "No module named 'app'"**
**Solution**: Make sure the Start Command is exactly:
```bash
gunicorn --bind 0.0.0.0:$PORT twiky_project.wsgi:application
```

### **Issue: "collectstatic" fails**
**Solution**: It's okay if this takes time. Render will retry.

### **Issue: Database connection fails**
**Solution**: 
1. Verify DATABASE_URL is set correctly
2. Make sure database and web service are in same region

---

## 💡 **PRO TIP**

If manual setup works, you can then update your settings and Render will auto-deploy on future git pushes!

---

## 📞 **NEED HELP?**

Check the logs in Render dashboard for specific errors.

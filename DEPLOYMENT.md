# 🚀 Twicky Deployment Guide

This guide will help you deploy Twicky to Vercel with MongoDB Atlas.

---

## 📋 Prerequisites

Before deploying, make sure you have:

1. ✅ A [Vercel](https://vercel.com) account
2. ✅ A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account (free tier is fine)
3. ✅ [Git](https://git-scm.com/) installed
4. ✅ [Vercel CLI](https://vercel.com/cli) installed (optional but recommended)

---

## 🗄️ Step 1: Setup MongoDB Atlas

### 1.1 Create a MongoDB Cluster

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up or log in
3. Click "Build a Database"
4. Choose the **FREE** tier (M0 Sandbox)
5. Select your preferred cloud provider and region
6. Name your cluster (e.g., "twicky-cluster")
7. Click "Create"

### 1.2 Create Database User

1. Go to "Database Access" in the left sidebar
2. Click "Add New Database User"
3. Choose "Password" authentication
4. Set username and password (save these!)
5. Set privileges to "Read and write to any database"
6. Click "Add User"

### 1.3 Whitelist IP Addresses

1. Go to "Network Access" in the left sidebar
2. Click "Add IP Address"
3. Click "Allow Access from Anywhere" (0.0.0.0/0)
   - Note: For production, you should restrict this to Vercel's IPs
4. Click "Confirm"

### 1.4 Get Connection String

1. Go to "Database" in the left sidebar
2. Click "Connect" on your cluster
3. Choose "Connect your application"
4. Copy the connection string
5. Replace `<password>` with your database user's password
6. Replace `<dbname>` with `twicky` (or your preferred database name)

Example:
```
mongodb+srv://username:password@cluster.mongodb.net/twicky
```

---

## 🔐 Step 2: Prepare Environment Variables

Create a list of your environment variables:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.vercel.app
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/twicky
```

### Generate a Strong SECRET_KEY

Run this Python command to generate a secure secret key:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🌐 Step 3: Deploy to Vercel

### Option A: Using Vercel CLI (Recommended)

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Navigate to your project**:
   ```bash
   cd path/to/twicky
   ```

4. **Deploy**:
   ```bash
   vercel
   ```

5. **Follow the prompts**:
   - Set up and deploy? `Y`
   - Which scope? Choose your account
   - Link to existing project? `N`
   - Project name? `twicky` (or your preferred name)
   - Directory? `.` (current directory)
   - Override settings? `N`

6. **Add Environment Variables**:
   ```bash
   vercel env add SECRET_KEY
   vercel env add DEBUG
   vercel env add ALLOWED_HOSTS
   vercel env add MONGODB_URI
   ```
   
   Enter the values when prompted.

7. **Deploy to Production**:
   ```bash
   vercel --prod
   ```

### Option B: Using Vercel Dashboard

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Import to Vercel**:
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Click "Import"

3. **Configure Project**:
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: Leave empty (uses vercel.json)
   - Output Directory: Leave empty

4. **Add Environment Variables**:
   - Expand "Environment Variables"
   - Add each variable:
     - `SECRET_KEY` = your-secret-key
     - `DEBUG` = False
     - `ALLOWED_HOSTS` = .vercel.app
     - `MONGODB_URI` = your-mongodb-connection-string

5. **Deploy**:
   - Click "Deploy"
   - Wait for deployment to complete

---

## ✅ Step 4: Post-Deployment

### 4.1 Update ALLOWED_HOSTS

After deployment, update the `ALLOWED_HOSTS` environment variable with your actual domain:

```env
ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app,your-app-name.vercel.app
```

### 4.2 Create Superuser (Optional)

To access the Django admin panel:

1. Connect to your deployment via Vercel CLI:
   ```bash
   vercel env pull
   ```

2. Run migrations locally with production database:
   ```bash
   python manage.py createsuperuser
   ```

### 4.3 Test Your Deployment

Visit your Vercel URL:
```
https://your-app-name.vercel.app
```

Test the following:
- ✅ Homepage loads
- ✅ User registration works
- ✅ User login works
- ✅ Creating tweets works
- ✅ Editing tweets works
- ✅ Deleting tweets works
- ✅ Static files load correctly

---

## 🔧 Troubleshooting

### Issue: Application Error / 500 Error

**Solution**: Check Vercel logs
```bash
vercel logs
```

Common causes:
- Missing environment variables
- Incorrect MongoDB connection string
- Database connection issues

### Issue: Static Files Not Loading

**Solution**: Make sure WhiteNoise is configured correctly in `settings.py`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be after SecurityMiddleware
    # ... other middleware
]
```

### Issue: MongoDB Connection Fails

**Solution**: 
1. Check if your IP is whitelisted in MongoDB Atlas
2. Verify your connection string is correct
3. Make sure your MongoDB user has correct permissions

### Issue: CSRF Verification Failed

**Solution**: Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`:
```python
CSRF_TRUSTED_ORIGINS = [
    'https://your-app-name.vercel.app',
]
```

---

## 🔄 Updating Your Deployment

### Automatic Deployment (GitHub Integration)

If you connected via GitHub:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

Vercel will automatically redeploy.

### Manual Deployment (Vercel CLI)

```bash
vercel --prod
```

---

## 📊 Monitoring

### View Logs

```bash
vercel logs your-app-name.vercel.app
```

### View Deployments

```bash
vercel ls
```

### Check Build Status

Visit your Vercel dashboard to see:
- Build logs
- Deployment history
- Analytics
- Error tracking

---

## 🎯 Best Practices

1. **Never commit `.env` files** - They contain sensitive information
2. **Use environment variables** - For all sensitive data
3. **Enable HTTPS only** - Already configured in production
4. **Regular backups** - MongoDB Atlas provides automated backups
5. **Monitor logs** - Check Vercel logs regularly
6. **Use custom domain** - For professional appearance
7. **Enable analytics** - Monitor your app's performance

---

## 📱 Adding a Custom Domain

1. Go to your Vercel project dashboard
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Update DNS records as instructed
5. Update `ALLOWED_HOSTS` to include your custom domain

---

## 🆘 Need Help?

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **MongoDB Atlas Documentation**: [docs.mongodb.com](https://docs.mongodb.com)
- **Django Documentation**: [docs.djangoproject.com](https://docs.djangoproject.com)

---

## ✨ Success!

Your Twicky application should now be live and accessible at:
```
https://your-app-name.vercel.app
```

Happy deploying! 🚀


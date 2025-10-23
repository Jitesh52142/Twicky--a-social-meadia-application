# 🔐 Environment Variables Setup Guide

## Complete Guide for Secure Deployment

---

## 🎯 Quick Setup

### Step 1: Generate a New SECRET_KEY

Run this command in your terminal:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Copy the output** - This is your new SECRET_KEY!

Example output:
```
django-insecure-abc123xyz789-your-unique-key-here-do-not-share
```

---

## 🔧 Vercel Environment Variables Setup

### Method 1: Using Vercel Dashboard (Easiest)

1. **Go to your Vercel project:**
   - https://vercel.com/dashboard
   - Select your `twicky` project

2. **Navigate to Settings:**
   - Click **Settings** tab
   - Click **Environment Variables** in the sidebar

3. **Add Each Variable:**

#### Variable 1: SECRET_KEY
```
Name: SECRET_KEY
Value: [paste your generated secret key here]
Environments: ✅ Production, ✅ Preview, ✅ Development
```

#### Variable 2: DEBUG
```
Name: DEBUG
Value: False
Environments: ✅ Production
```

#### Variable 3: ALLOWED_HOSTS
```
Name: ALLOWED_HOSTS
Value: .vercel.app
Environments: ✅ Production, ✅ Preview
```

#### Variable 4: MONGODB_URI (Optional - not used in current Vercel setup)
```
Name: MONGODB_URI
Value: mongodb+srv://username:password@cluster.mongodb.net/twicky
Environments: ✅ Production, ✅ Preview, ✅ Development
```

4. **Click "Save"** for each variable

5. **Redeploy:**
   - Go to **Deployments** tab
   - Click **⋮** on latest deployment
   - Click **Redeploy**

---

### Method 2: Using Vercel CLI

```bash
# Install Vercel CLI if not already installed
npm i -g vercel

# Login to Vercel
vercel login

# Navigate to your project
cd "C:/Users/DELL/OneDrive/画像/Desktop/old projects/twicky/Twicky--a-social-meadia-application"

# Add environment variables
vercel env add SECRET_KEY production
# [Paste your generated secret key when prompted]

vercel env add DEBUG production
# Enter: False

vercel env add ALLOWED_HOSTS production
# Enter: .vercel.app

# Redeploy
vercel --prod
```

---

## 🏠 Local Development Setup

### Create `.env` File

1. **Copy the example file:**
   ```bash
   # Windows Command Prompt
   copy env.example .env
   
   # Windows PowerShell
   Copy-Item env.example .env
   
   # Git Bash / Linux / Mac
   cp env.example .env
   ```

2. **Edit `.env` file:**
   ```env
   # Django Settings
   SECRET_KEY=your-generated-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   MONGODB_URI=mongodb+srv://Jitesh001:Jitesh001@twicky.fxotzly.mongodb.net/twicky
   ```

3. **Save the file**

4. **Verify it's in .gitignore:**
   ```bash
   # Check if .env is ignored
   git status
   # You should NOT see .env in the list
   ```

---

## 🔒 Security Best Practices

### ✅ DO:

1. **Use Different Keys for Different Environments**
   - Development: One SECRET_KEY
   - Production: Different SECRET_KEY

2. **Generate Strong SECRET_KEY**
   ```bash
   # Always use Django's built-in generator
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Keep DEBUG=False in Production**
   - Never set DEBUG=True on Vercel
   - Only use DEBUG=True locally

4. **Use Environment-Specific Hosts**
   - Local: `localhost,127.0.0.1`
   - Vercel: `.vercel.app,your-app-name.vercel.app`

5. **Rotate Keys Regularly**
   - Change SECRET_KEY every 3-6 months
   - Change immediately if exposed

### ❌ DON'T:

1. **Never commit .env files**
   - Already in .gitignore
   - Double-check with `git status`

2. **Never share SECRET_KEY**
   - Don't post in issues
   - Don't share in screenshots
   - Don't commit to GitHub

3. **Never use default keys in production**
   - The key in the example file is just an example
   - Always generate a new one

4. **Never set DEBUG=True in production**
   - Security risk
   - Exposes sensitive information

---

## 📋 Complete Environment Variables Reference

### Required Variables:

| Variable | Description | Local Example | Production Example |
|----------|-------------|---------------|-------------------|
| `SECRET_KEY` | Django secret key | `django-insecure-local-dev-key-123` | `django-insecure-prod-abc-xyz-789` |
| `DEBUG` | Debug mode | `True` | `False` |
| `ALLOWED_HOSTS` | Allowed domains | `localhost,127.0.0.1` | `.vercel.app,your-app.vercel.app` |

### Optional Variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGODB_URI` | MongoDB connection | `mongodb+srv://user:pass@cluster.net/db` |
| `DATABASE_URL` | Database URL (alternative) | `postgresql://user:pass@host/db` |

---

## 🔄 After Updating Environment Variables

### On Vercel:

1. **Trigger Redeploy:**
   ```bash
   vercel --prod
   ```
   Or use the Vercel Dashboard

2. **Verify Deployment:**
   - Check deployment logs
   - Visit your site
   - Test functionality

### Locally:

1. **Restart Development Server:**
   ```bash
   # Stop server (Ctrl+C)
   # Start again
   python manage.py runserver
   ```

2. **Clear Cache (if needed):**
   ```bash
   python manage.py collectstatic --clear --noinput
   ```

---

## 🧪 Testing Your Configuration

### Local Testing:

```bash
# Start server
python manage.py runserver

# Check in browser
# Visit: http://localhost:8000

# You should see:
# ✅ Site loads
# ✅ No debug toolbar (if DEBUG=False)
# ✅ Static files load
# ✅ No errors in console
```

### Production Testing (Vercel):

```bash
# Deploy
vercel --prod

# Check your site
# Visit: https://your-app-name.vercel.app

# Test:
# ✅ Homepage loads
# ✅ Login works
# ✅ Register works
# ✅ Static files load
# ✅ No DEBUG information visible
```

---

## 🚨 Troubleshooting

### Issue: "SECRET_KEY not found"

**Solution:**
```bash
# Verify .env file exists
ls -la .env

# Check if variable is set in Vercel
vercel env ls

# Add it if missing
vercel env add SECRET_KEY production
```

### Issue: "ALLOWED_HOSTS invalid"

**Solution:**
```env
# Make sure format is correct (comma-separated, no spaces)
ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app

# NOT:
ALLOWED_HOSTS=localhost, 127.0.0.1, .vercel.app  ❌
```

### Issue: "DEBUG errors showing in production"

**Solution:**
```bash
# Check DEBUG setting in Vercel
vercel env ls

# Should be False, not True
# Update if needed
vercel env rm DEBUG production
vercel env add DEBUG production
# Enter: False
```

### Issue: "Static files not loading"

**Solution:**
```bash
# Collect static files
python manage.py collectstatic --noinput

# Verify STATIC_ROOT and STATIC_URL in settings
# Check WhiteNoise is in MIDDLEWARE
```

---

## 📝 Environment Variables Checklist

Before deploying, verify:

### Local Development:
- [ ] `.env` file created
- [ ] `SECRET_KEY` generated and added
- [ ] `DEBUG=True` for development
- [ ] `ALLOWED_HOSTS` includes localhost
- [ ] `.env` is in `.gitignore`
- [ ] `.env` is NOT committed to git

### Vercel Production:
- [ ] `SECRET_KEY` added to Vercel
- [ ] `DEBUG=False` set in Vercel
- [ ] `ALLOWED_HOSTS` includes `.vercel.app`
- [ ] All variables saved
- [ ] Redeployed after adding variables
- [ ] Tested deployment

---

## 🎯 Quick Reference Commands

### Generate SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Check Environment Variables (Vercel):
```bash
vercel env ls
```

### Add Variable (Vercel):
```bash
vercel env add VARIABLE_NAME production
```

### Remove Variable (Vercel):
```bash
vercel env rm VARIABLE_NAME production
```

### Deploy with New Variables:
```bash
vercel --prod
```

### View Deployment Logs:
```bash
vercel logs your-deployment-url
```

---

## 🔐 Example Configuration Files

### `.env` (Local Development):
```env
SECRET_KEY=django-insecure-local-dev-key-abc123xyz789
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
MONGODB_URI=mongodb+srv://user:pass@cluster.net/twicky
```

### Vercel Environment Variables (Production):
```
SECRET_KEY=django-insecure-prod-key-xyz789abc123
DEBUG=False
ALLOWED_HOSTS=.vercel.app,twicky-app.vercel.app
```

---

## ✅ Verification

After setup, your configuration should be:

**Local:**
- `.env` file exists in project root
- Contains all required variables
- NOT tracked by git
- DEBUG=True for development

**Vercel:**
- All variables set in dashboard
- DEBUG=False for production
- ALLOWED_HOSTS includes your domain
- Site works correctly

---

## 📞 Need Help?

- **Vercel Docs:** https://vercel.com/docs/environment-variables
- **Django Docs:** https://docs.djangoproject.com/en/4.2/topics/settings/
- **python-decouple Docs:** https://github.com/henriquebastos/python-decouple

---

## 🎉 You're All Set!

Your environment variables are now configured securely for both local development and production deployment!

**Next Steps:**
1. Generate your SECRET_KEY
2. Add it to Vercel dashboard
3. Set DEBUG=False for production
4. Deploy and test!

🚀 Happy deploying!


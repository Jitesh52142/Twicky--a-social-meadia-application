# 🔐 Vercel Environment Variables - REQUIRED!

## ⚠️ IMPORTANT: Set These in Vercel Dashboard

Go to: **Vercel Dashboard → Your Project → Settings → Environment Variables**

---

## Required Environment Variables

### 1. SECRET_KEY (REQUIRED ⚠️)
```
SECRET_KEY=<your-secret-key-here>
```

**Generate one NOW:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Example output:
```
django-insecure-abc123xyz789...
```

Copy that and paste it in Vercel!

---

### 2. DEBUG (REQUIRED)
```
DEBUG=False
```

**MUST be False in production!**

---

### 3. ALLOWED_HOSTS (REQUIRED)
```
ALLOWED_HOSTS=.vercel.app
```

This allows your Vercel domain to access the app.

---

### 4. VERCEL (REQUIRED)
```
VERCEL=1
```

This tells Django it's running on Vercel.

---

## 📋 Quick Copy-Paste Template

Go to Vercel → Settings → Environment Variables and add these ONE BY ONE:

| Variable | Value | Environment |
|----------|-------|-------------|
| `SECRET_KEY` | `<generate-using-command-above>` | Production, Preview, Development |
| `DEBUG` | `False` | Production, Preview, Development |
| `ALLOWED_HOSTS` | `.vercel.app` | Production, Preview, Development |
| `VERCEL` | `1` | Production, Preview, Development |

---

## 🎯 Step-by-Step Instructions

### Step 1: Generate SECRET_KEY

**On Windows (PowerShell):**
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Copy the output!** It will look like:
```
django-insecure-q8$5f@h3k9l2m#n4p6r&s7t*v9w1x!y2z3
```

### Step 2: Add to Vercel

1. Go to https://vercel.com/dashboard
2. Click on your project (twicky-a-social-meadia-application)
3. Click **Settings** tab
4. Click **Environment Variables** in sidebar
5. Add each variable:
   - **Key:** `SECRET_KEY`
   - **Value:** Paste the generated key
   - **Environment:** Check all three (Production, Preview, Development)
   - Click **Save**

6. Repeat for:
   - **Key:** `DEBUG` → **Value:** `False`
   - **Key:** `ALLOWED_HOSTS` → **Value:** `.vercel.app`
   - **Key:** `VERCEL` → **Value:** `1`

### Step 3: Redeploy

After adding environment variables:
- Go to **Deployments** tab
- Click the **"..."** menu on latest deployment
- Click **Redeploy**

---

## ✅ Verification

After setting environment variables and redeploying:

1. Check deployment logs for errors
2. Visit your Vercel URL
3. Should see the Twicky homepage!

---

## 🐛 Still Getting 500 Error?

### Check These:

1. **All 4 environment variables set?**
   - SECRET_KEY ✓
   - DEBUG=False ✓
   - ALLOWED_HOSTS=.vercel.app ✓
   - VERCEL=1 ✓

2. **Check Vercel Logs:**
   - Go to Deployments → Click latest → View Function Logs
   - Look for actual error messages

3. **SECRET_KEY not empty?**
   - Make sure you actually generated and pasted a real key
   - Not just the example text!

---

## 💡 Pro Tip

After you set the environment variables, Vercel will automatically redeploy. Wait 1-2 minutes for the deployment to complete, then check your URL again.

---

## 🎯 Expected Result

Once environment variables are set correctly, you should see:
- ✅ Twicky homepage loads
- ✅ No 500 error
- ✅ Can view tweets
- ⚠️ Image uploads won't persist (Vercel limitation)
- ⚠️ Admin might not work well

---

## 🚀 Better Alternative: Railway

If you're tired of Vercel's limitations:

```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

Railway works perfectly with Django - no environment variable headaches, images work, database included!

---

**Need help? The deployment should work after setting these environment variables!**

**Built with 💙 by Jitesh Bawaskar**


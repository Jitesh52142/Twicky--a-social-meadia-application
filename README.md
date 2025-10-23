# 🚀 **Twicky - A Social Media Platform**

**Twicky** is a modern and dynamic **social media web application** built with **Django, HTML, CSS, and Bootstrap**. It allows users to **create, edit, and delete tweets**, upload images, and manage their accounts with **secure authentication**. The platform offers a **smooth and responsive UI**, making it easy for users to share their thoughts, images, and engage with the platform.

🌐 **Now with MongoDB support and ready for Vercel deployment!**

---

## ✅ **Key Features**

### 🔥 **1. User Authentication**
- **Register & Login:** Users can create an account, log in, and securely access their profile.  
- **Authentication Handling:**  
  - Only authenticated users can create, edit, and delete their own tweets.  
  - Unauthenticated users can only view the tweet list.  
- **Session Management:** Ensures secure handling of user sessions and redirects after login/logout.

---

### 📝 **2. Tweet Management**
- **Create Tweets:** Users can compose tweets with text and optional image uploads.  
- **Edit Tweets:** Users can modify their existing tweets.  
- **Delete Tweets:** Users can delete their tweets with confirmation prompts.  
- **Image Upload:** Each tweet supports an optional image upload.  
- **Dynamic Sorting:** Tweets are displayed in reverse chronological order, with the latest tweet appearing first.

---

### 🌟 **3. Professional Responsive UI**
- **Modern and Responsive Design:**  
  - Built with **Bootstrap 5** with professional gradients and animations.  
  - Fully responsive on **desktop, tablet, and mobile** devices.  
- **Enhanced Dark Mode:**  
  - Beautiful gradient backgrounds and glassmorphism effects.  
  - Professional card designs with hover animations.  
  - Smooth transitions and modern UI components.  
- **Interactive Elements:**  
  - Gradient buttons with hover effects.  
  - Animated cards and smooth transitions.  
  - Professional form designs with modern styling.

---

### 📁 **4. File Management**
- **Media Upload:**  
  - Users can upload images with their tweets.  
  - **MEDIA_URL** and **MEDIA_ROOT** configurations manage the uploaded files.  
- **Static Files:**  
  - The app handles static files (CSS, JS, images) through **whitenoise** for optimized performance.  

---

## 🔥 **Tech Stack**
- **Backend:** Django 4.2 (Python)  
- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Database:** MongoDB (via Djongo)  
- **Styling:** Bootstrap 5 with custom gradients and animations  
- **Deployment:** Vercel-ready  

---

## 🚀 **Setup Instructions**

### **Prerequisites**
- Python 3.9 or higher
- Git
- (Optional) MongoDB Atlas account for MongoDB deployment

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/twicky.git
cd twicky
```

### **2. Create Virtual Environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Environment Configuration**
Create a `.env` file in the root directory (use `env.example` as reference):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
```

### **5. MongoDB Setup**
1. Create a free MongoDB Atlas cluster at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a database named `twicky`
3. Get your connection string and add it to `.env`
4. Make sure to whitelist your IP address in MongoDB Atlas

### **6. Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **7. Create Superuser (Optional)**
```bash
python manage.py createsuperuser
```

### **8. Run Development Server**

**For HTTP (standard):**
```bash
python manage.py runserver
```

**For HTTPS (with SSL):**
```bash
python manage.py runserver_plus --cert-file cert
```

Visit `http://localhost:8000` (or `https://localhost:8000` for SSL) to see your application!

---

## 🌐 **Deployment**

### ⚠️ **Important: Vercel Limitations**

Vercel has serverless limitations that make it challenging for Django apps with file uploads:
- No persistent file storage (uploaded images won't persist)
- Large dependency size limits
- Cold start delays

### **Recommended Platforms:**

#### 1. **Railway** (Best Choice ⭐)
```bash
# Install Railway CLI
npm i -g @railway/cli

# Deploy
railway login
railway init
railway up
```

**Why Railway?**
- ✅ Persistent storage for images
- ✅ PostgreSQL included free
- ✅ No serverless limitations
- ✅ Automatic HTTPS

See `VERCEL_DEPLOYMENT_GUIDE.md` for detailed instructions.

#### 2. **Render**
- Easy deployment with `render-build.sh`
- PostgreSQL included
- Persistent disk storage
- See `DEPLOYMENT_CHECKLIST.md`

#### 3. **Vercel (With Limitations)**
If you still want to use Vercel:
1. Use external storage (Cloudinary, AWS S3)
2. Use Vercel Postgres or MongoDB Atlas
3. Use `requirements-vercel.txt` instead of `requirements.txt`
4. See `VERCEL_DEPLOYMENT_GUIDE.md` for fixes

### **Environment Variables (All Platforms)**
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=your-database-url (if not SQLite)
```

---

## 📦 **Project Structure**
```
twicky/
├── twicky/                  # Main app
│   ├── templates/          # App templates
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── forms.py            # Django forms
│   └── urls.py             # App URLs
├── twiky_project/          # Project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Main URLs
│   └── wsgi.py             # WSGI config
├── templates/              # Global templates
│   ├── layout.html         # Base template
│   └── registration/       # Auth templates
├── media/                  # User uploads
├── staticfiles/            # Collected static files
├── vercel.json            # Vercel configuration
├── build_files.sh         # Build script
├── requirements.txt       # Dependencies
└── manage.py              # Django management
```

---

## 🛠️ **Future Enhancements**
- **Like & Comment Functionality:** Allowing users to engage with tweets.  
- **Search & Filter:** Adding a tweet search functionality by content or date.  
- **User Profiles:** Customizable user profiles with avatars and bios.  
- **Real-Time Features:** Implementing WebSockets for real-time updates.
- **Cloud Media Storage:** Integration with AWS S3 or Cloudinary for production media files.
- **Follow/Unfollow System:** Social networking features.

---

## 🔒 **Security Features**
- CSRF protection enabled
- Secure password hashing
- Session security
- SQL injection prevention via Django ORM
- XSS protection
- HTTPS enforcement in production

---

## 📝 **License**
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 **Developer**
Built with 💙 by [Jitesh Bawaskar](https://github.com/Jitesh52142)

---

## 🚀 **Why Twicky?**
Twicky offers a **seamless and intuitive social media experience** with clean design, responsive layout, and essential social media features. With its **secure authentication**, MongoDB cloud database, modern UI, and Vercel deployment support, it provides a solid foundation for building a full-fledged social media platform.

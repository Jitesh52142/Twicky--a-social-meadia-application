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
- MongoDB Atlas account (or local MongoDB)
- Git

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
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your application!

---

## 🌐 **Vercel Deployment**

### **1. Install Vercel CLI**
```bash
npm i -g vercel
```

### **2. Configure Environment Variables**
In your Vercel dashboard, add these environment variables:
- `SECRET_KEY` - Your Django secret key
- `DEBUG` - Set to `False` for production
- `ALLOWED_HOSTS` - Your Vercel domain
- `MONGODB_URI` - Your MongoDB connection string

### **3. Deploy to Vercel**
```bash
vercel --prod
```

### **4. Important Notes**
- The `vercel.json` file is already configured
- Static files are handled by WhiteNoise
- Media files should be served from a cloud service (AWS S3, Cloudinary) in production
- MongoDB Atlas handles the database

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

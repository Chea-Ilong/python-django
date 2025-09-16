# JingJang - Journal-Style Task Management App 📔✨

A beautifully designed Django web application for task management with a unique journal/scrapbook aesthetic. Transform your daily tasks into achievements with an intuitive, visually appealing interface that feels like writing in your personal notebook.

> **Live Demo**: Experience the magic of digital journaling with task management!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.23-green.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **🎨 Journal-Style Design**: Beautiful scrapbook/notebook aesthetic with handwritten fonts, tape effects, and spiral binding
- **📝 Task Management**: Create, complete, and delete tasks with intuitive controls
- **🔐 User Authentication**: Secure login, signup, and profile management system
- **📧 Password Recovery**: Username and password recovery via email notifications
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **⚡ Real-time Updates**: Dynamic task statistics and instant status updates
- **🎭 Playful Animations**: Smooth hover effects and delightful page transitions

## 🎨 Design Highlights

- **Custom Tailwind CSS**: Journal-themed animations and interactive elements
- **Google Fonts**: Kalam and Caveat fonts for authentic handwritten feel
- **Paper Textures**: Realistic lined paper backgrounds and aging effects
- **Decorative Elements**: Playful tape, stickers, spiral binding, and hand-drawn doodles
- **Smooth Animations**: Page turns, ink drops, and floating elements
- **Color Palette**: Warm amber, orange, and yellow tones for cozy feel

## 🛠️ Tech Stack

- **Backend**: Django 4.2.23
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Database**: SQLite (default) / MySQL (configurable)
- **Authentication**: Django's built-in auth system
- **Email**: SMTP support for notifications

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chea-Ilong/python-django.git
   cd python-django
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your actual values
   ```

5. **Run database migrations**
   ```bash
   cd Testing
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Visit `http://127.0.0.1:8000` in your browser to start using JinLong Journal! 📚

## ⚙️ Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure the following:

| Variable | Description | Required |
|----------|-------------|----------|
| `EMAIL_HOST` | SMTP server host | Yes (for email features) |
| `EMAIL_PORT` | SMTP server port | Yes |
| `EMAIL_USE_TLS` | Use TLS encryption | Yes |
| `EMAIL_HOST_USER` | Your email address | Yes |
| `EMAIL_HOST_PASSWORD` | Your email app password | Yes |
| `DEFAULT_FROM_EMAIL` | Default sender email | Yes |

### Database Configuration

**SQLite (Default)**
No additional configuration needed. Database file will be created automatically.

**MySQL (Optional)**
Uncomment and configure the database variables in `.env`:
```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

## 📱 Usage

### Getting Started
1. **Sign up** for a new account or **log in** with existing credentials
2. **Create tasks** from the home dashboard by clicking "Add New Task"  
3. **Mark tasks complete** by checking them off your list
4. **View your profile** to see account information and activity
5. **Browse your journal** to see all tasks in a beautiful, organized layout

### Navigation
- **Home** 🏠 - Dashboard with task overview and quick actions
- **Profile** 👤 - User account management and statistics  
- **Tasks** ✅ - Complete task management interface
- **Settings** ⚙️ - Application preferences and configuration

### User Registration & Authentication
1. Visit the homepage and explore the journal-themed interface
2. Click "Sign Up" to create a new account with journal aesthetics
3. Or use "Sign In" if you already have an account
4. Use "Username Recovery" if you forget your username

### Task Management  
1. **View Tasks**: Navigate to see all your todos in journal format
2. **Add Task**: Use the beautiful forms to add new tasks
3. **Complete Task**: Check off tasks with satisfying animations
4. **Delete Task**: Remove tasks you no longer need

### Profile Management
1. Go to "Profile" to view/edit your account information
2. Update username and email in the styled interface
3. Access password change functionality

## 🎯 Project Structure

```
Testing/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── .env                     # Environment variables (not in repo)
├── .env.example            # Environment variables template
├── myapp/                  # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   ├── forms.py            # Form definitions
│   └── migrations/         # Database migrations
├── Testing/                # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
└── theme/                  # Templates and static files
    ├── templates/          # HTML templates
    │   ├── base.html       # Base template
    │   ├── home.html       # Homepage
    │   ├── todos.html      # Tasks page
    │   ├── profile.html    # Profile page
    │   └── registration/   # Auth templates
    └── static/             # CSS, JS, images
```

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## 🚀 Deployment

### Local Development
The project is configured for local development with Django's built-in server:
```bash
python manage.py runserver
```

### Production Deployment
For production deployment, consider:

1. **Environment Variables**: Ensure all production values are set in `.env`
2. **Database**: Migrate to PostgreSQL or MySQL for production
3. **Static Files**: Run `collectstatic` and serve via nginx or Apache
4. **HTTPS**: Configure SSL certificates for secure connections
5. **Email**: Set up proper SMTP configuration for email features

### Recommended Production Stack
- **Web Server**: nginx or Apache
- **WSGI Server**: Gunicorn or uWSGI
- **Database**: PostgreSQL or MySQL
- **Cache**: Redis or Memcached
- **Process Manager**: Supervisor or systemd

### Production Checklist
- [ ] Set `DEBUG=False` in settings
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up a production database (PostgreSQL recommended)
- [ ] Configure email settings
- [ ] Set up static file serving
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS

### Environment Variables for Production
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-production-secret-key
```

## 🤝 Contributing

We welcome contributions! Here's how you can help make JinLong Journal even better:

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow Django best practices and PEP 8 style guide
- Add tests for new features
- Update documentation as needed
- Ensure your code works with the journal theme
- Test on multiple screen sizes for responsive design

### Areas for Contribution
- 🎨 UI/UX improvements and new journal themes
- � New features and functionality
- 🐛 Bug fixes and performance optimizations
- 📚 Documentation improvements
- 🌐 Internationalization and accessibility
- 🧪 Test coverage improvements

## �📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎨 Design Credits

- **Fonts**: Google Fonts (Kalam, Caveat) for handwritten aesthetic
- **Icons**: Unicode emoji characters for visual appeal
- **Design Inspiration**: Hand-drawn journals, scrapbooks, and vintage notebooks
- **CSS Framework**: Tailwind CSS with custom journal-themed configurations
- **Animations**: Custom CSS animations (ink-drop, page-turn, float effects)

## 📞 Support & Contact

- **GitHub Issues**: Report bugs or request features
- **Email**: For general inquiries and support
- **Documentation**: Check this README and inline code comments
- **Community**: Join discussions in GitHub Discussions

---

<div align="center">

**Made with ❤️ and ☕ by JinLong**

*Turn your tasks into a beautiful journal experience* ✨

</div>

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/jingjiang-task-manager/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the problem

## 🔄 Changelog

### v1.0.0 (Current)
- Initial release
- Journal-style UI design
- Basic task management functionality
- User authentication system
- Email-based password recovery
- Responsive design

---

**Made with ❤️ by [Your Name]**

*Transform your productivity journey with JingJang!* 📓✨
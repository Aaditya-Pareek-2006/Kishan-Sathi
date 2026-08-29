// frontend/auth.js

function showToastAuth(message, type) {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) return;
    const toast = document.createElement('div');
    toast.className = `p-3 rounded shadow-md text-white text-sm font-bold ${type === 'success' ? 'bg-green-500' : 'bg-red-500'} mb-2`;
    toast.innerText = message;
    toastContainer.appendChild(toast);
    setTimeout(() => { toast.remove(); }, 3000);
}

// 1. LOGIN LOGIC
const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', async(e) => {
        e.preventDefault();

        // Safety check taaki null error na aaye
        const phoneInput = document.getElementById('loginPhone');
        const pinInput = document.getElementById('loginPin');
        const btn = document.getElementById('loginBtn');

        if (!phoneInput || !pinInput) {
            console.error("HTML IDs match nahi ho rahi hain!");
            return;
        }

        const phone = phoneInput.value;
        const pin = pinInput.value;

        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Checking...';
        btn.disabled = true;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ phone: phone, pin: pin })
            });
            const data = await response.json();

            if (response.ok) {
                showToastAuth("Login Successful!", "success");
                localStorage.setItem('kisan_user', JSON.stringify(data.user));
                setTimeout(() => { window.location.href = 'index.html'; }, 1000);
            } else {
                showToastAuth(data.detail || "Galat details", "error");
            }
        } catch (error) {
            showToastAuth("Server se connection nahi hua!", "error");
            console.error(error);
        } finally {
            btn.innerHTML = 'Login Karein';
            btn.disabled = false;
        }
    });
}

// 2. SIGNUP LOGIC
const signupForm = document.getElementById('signupForm');
if (signupForm) {
    signupForm.addEventListener('submit', async(e) => {
        e.preventDefault();

        const payload = {
            name: document.getElementById('signName').value,
            phone: document.getElementById('signPhone').value,
            village: document.getElementById('signVillage').value,
            district: document.getElementById('signDistrict').value,
            pin: document.getElementById('signPin').value
        };
        const btn = document.getElementById('signupBtn');
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Registering...';
        btn.disabled = true;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/auth/signup', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await response.json();

            if (response.ok) {
                showToastAuth("Account ban gaya!", "success");
                localStorage.setItem('kisan_user', JSON.stringify(data.user));
                setTimeout(() => { window.location.href = 'index.html'; }, 1000);
            } else {
                showToastAuth(data.detail || "Error in signup", "error");
            }
        } catch (error) {
            showToastAuth("Server connection error!", "error");
        } finally {
            btn.innerHTML = 'Register Karein';
            btn.disabled = false;
        }
    });
}

// 3. PROFILE CHECK
function checkAuth() {
    const userString = localStorage.getItem('kisan_user');
    const currentPage = window.location.pathname;

    // Login protection
    if (!userString && !currentPage.includes('login.html') && !currentPage.includes('admin.html')) {
        window.location.href = 'login.html';
        return;
    }

    // Profile page populate
    if (currentPage.includes('profile.html') && userString) {
        const user = JSON.parse(userString);
        document.getElementById('profile-name').innerText = user.name;
        document.getElementById('profile-phone').innerText = "+91 " + user.phone;
        document.getElementById('profile-location').innerText = `${user.village}, ${user.district}`;

        document.getElementById('logoutBtn').addEventListener('click', () => {
            localStorage.removeItem('kisan_user');
            window.location.href = 'login.html';
        });
    }
}
document.addEventListener("DOMContentLoaded", checkAuth);
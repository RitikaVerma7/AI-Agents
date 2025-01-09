from flask import Flask, request, jsonify

app = Flask(__name__)

# Vulnerable JavaScript file that will be served
VULNERABLE_JS = """
// API Configuration
const API_CONFIG = {
    userInfo: '/api/v1/user-info',  // Leaks sensitive data without auth
    adminPanel: '/api/v1/admin',    // Requires specific admin key
    userProfile: '/api/v1/profile', // Requires X-User-Id header
};

// Admin key hardcoded (security vulnerability)
const ADMIN_KEY = 'super_secret_admin_key_123';

// Function to fetch user info (no auth required - vulnerability)
async function fetchUserInfo() {
    const response = await fetch('/api/v1/user-info');
    return response.json();
}

// Function to access admin panel
async function accessAdminPanel() {
    const headers = {
        'Content-Type': 'application/json',
        'X-Admin-Key': ADMIN_KEY  // Hardcoded admin key usage
    };
    
    const response = await fetch('/api/v1/admin', {
        headers: headers
    });
    return response.json();
}

// Function to get user profile
async function getUserProfile(userId) {
    const headers = {
        'X-User-Id': userId  // Required custom header
    };
    
    const response = await fetch('/api/v1/profile', {
        headers: headers
    });
    return response.json();
}

"""

@app.route('/main.js')
def serve_js():
    return VULNERABLE_JS, 200, {'Content-Type': 'application/javascript'}

@app.route('/api/v1/user-info')
def user_info():
    # Vulnerable: Returns sensitive information without authentication
    return jsonify({
        "users": [
            {"id": "1", "name": "John Doe", "ssn": "123-45-6789", "salary": 75000},
            {"id": "2", "name": "Jane Smith", "ssn": "987-65-4321", "salary": 82000}
        ],
        "database_connection": "mongodb://admin:password@localhost:27017",
        "api_keys": {
            "stripe": "sk_test_123456789",
            "aws": "AKIA1234567890EXAMPLE"
        }
    })

@app.route('/api/v1/profile')
def user_profile():
    # Requires X-User-Id header
    user_id = request.headers.get('X-User-Id')
    if not user_id:
        return jsonify({"error": "X-User-Id header is required"}), 401
    
    return jsonify({
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
        "role": "user"
    })

@app.route('/api/v1/admin')
def admin_panel():
    # Requires specific admin key value
    admin_key = request.headers.get('X-Admin-Key')
    if not admin_key:
        return jsonify({"error": "X-Admin-Key header is required"}), 401
    
    if admin_key != 'super_secret_admin_key_123':  # Hardcoded key check
        return jsonify({"error": "Invalid admin key"}), 403
    
    return jsonify({
        "sensitive_data": "This is sensitive admin data",
        "internal_keys": {
            "database": "root:password123",
            "api_gateway": "private_key_xyz"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

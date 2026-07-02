import Layout from "../components/Layout";

export default function Settings() {
  return (
    <Layout>
      <h1
        style={{
          fontSize: "32px",
          marginBottom: "25px",
        }}
      >
        Settings
      </h1>

      <div
        style={{
          display: "grid",
          gap: "20px",
        }}
      >
        {/* Account Settings */}
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>👤 Account Settings</h2>

          <p>Name: Sanika Gharat</p>
          <p>Email: user@email.com</p>

          <button
            style={{
              padding: "10px 18px",
              borderRadius: "8px",
              border: "none",
              background: "#2563eb",
              color: "white",
              cursor: "pointer",
            }}
          >
            Edit Profile
          </button>
        </div>

        {/* Preferences */}
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>🎨 Preferences</h2>

          <label>
            <input type="checkbox" />
            Enable Dark Mode
          </label>

          <br />
          <br />

          <label>
            <input type="checkbox" />
            Enable Notifications
          </label>
        </div>

        {/* Legal Research */}
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>⚖️ Legal Research Defaults</h2>

          <p>Preferred Court:</p>

          <select>
            <option>Supreme Court</option>
            <option>High Court</option>
            <option>District Court</option>
          </select>

          <br />
          <br />

          <p>Preferred Language:</p>

          <select>
            <option>English</option>
            <option>Hindi</option>
            <option>Marathi</option>
          </select>
        </div>

        {/* Security */}
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>🔒 Security</h2>

          <button
            style={{
              padding: "10px 18px",
              borderRadius: "8px",
              border: "none",
              background: "#f59e0b",
              color: "white",
              marginRight: "10px",
            }}
          >
            Change Password
          </button>

          <button
            style={{
              padding: "10px 18px",
              borderRadius: "8px",
              border: "none",
              background: "#10b981",
              color: "white",
            }}
          >
            Enable 2FA
          </button>
        </div>

        {/* Data */}
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>📂 Data Management</h2>

          <button
            style={{
              padding: "10px 18px",
              borderRadius: "8px",
              border: "none",
              background: "#2563eb",
              color: "white",
              marginRight: "10px",
            }}
          >
            Export Data
          </button>

          <button
            style={{
              padding: "10px 18px",
              borderRadius: "8px",
              border: "none",
              background: "#ef4444",
              color: "white",
            }}
          >
            Delete All Documents
          </button>
        </div>

        {/* Logout */}
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>🚪 Session</h2>

          <button
            style={{
              padding: "10px 20px",
              borderRadius: "8px",
              border: "none",
              background: "#dc2626",
              color: "white",
              cursor: "pointer",
            }}
          >
            Logout
          </button>
        </div>
      </div>
    </Layout>
  );
}
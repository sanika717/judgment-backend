import { Link } from "react-router-dom";

export default function Sidebar() {
  const menuItems = [
    "Dashboard",
    "Documents",
    "Upload",
    "Chat",
    "Analytics",
    "Bookmarks",
    "Profile",
    "Settings",
  ];

  return (
    <div
      style={{
        width: "260px",
        height: "100vh",
        background: "#0f172a",
        color: "white",
        position: "fixed",
        left: 0,
        top: 0,
        padding: "24px",
        boxSizing: "border-box",
      }}
    >
      <h2
        style={{
          fontSize: "28px",
          marginBottom: "30px",
        }}
      >
        ⚖️ Legal AI
      </h2>

      {menuItems.map((item) => (
        <Link
          key={item}
          to={`/${item.toLowerCase()}`}
          style={{
            display: "block",
            color: "white",
            textDecoration: "none",
            padding: "12px",
            borderRadius: "8px",
            marginBottom: "8px",
            backgroundColor: "#1e293b",
          }}
        >
          {item}
        </Link>
      ))}
    </div>
  );
}
import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-64 h-screen bg-slate-900 text-white fixed p-6">

      <h1 className="text-2xl font-bold mb-8">
        Legal AI
      </h1>

      <nav className="flex flex-col gap-4">

        <Link to="/dashboard">Dashboard</Link>

        <Link to="/documents">Documents</Link>

        <Link to="/upload">Upload</Link>

        <Link to="/chat">Chat</Link>

        <Link to="/analytics">Analytics</Link>

        <Link to="/bookmarks">Bookmarks</Link>

        <Link to="/profile">Profile</Link>

        <Link to="/settings">Settings</Link>

      </nav>

    </div>
  );
}
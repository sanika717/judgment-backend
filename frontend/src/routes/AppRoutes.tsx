import { Routes, Route } from "react-router-dom";

import Dashboard from "../pages/Dashboard";
import Documents from "../pages/Documents";
import Upload from "../pages/Upload";
import Analytics from "../pages/Analytics";
import Profile from "../pages/Profile";
import Chat from "../pages/chat";
import Bookmarks from "../pages/Bookmarks";
import Settings from "../pages/Settings";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/documents" element={<Documents />} />
      <Route path="/upload" element={<Upload />} />
      <Route path="/analytics" element={<Analytics />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/chat" element={<Chat />} />
      <Route path="/bookmarks" element={<Bookmarks />} />
      <Route path="/settings" element={<Settings />} />
    </Routes>
  );
}
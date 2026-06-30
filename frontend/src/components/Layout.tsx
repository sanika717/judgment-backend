import React from 'react';
import { Outlet, Link, useLocation } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

function Navbar(){
  const { user, logout } = useAuth();
  return (
    <div className="flex items-center justify-between bg-white px-6 py-4 shadow-sm">
      <div className="flex items-center gap-4">
        <div className="text-2xl font-extrabold text-primary">Legal RAG</div>
        <div className="text-sm text-slate-500">Document-first RAG for lawyers</div>
      </div>
      <div className="flex items-center gap-3">
        {user ? <>
          <div className="text-sm text-slate-700">Hi, {user.username}</div>
          <button onClick={logout} className="px-3 py-1 rounded bg-slate-100 text-sm">Logout</button>
        </> : <Link to="/login" className="px-3 py-1 rounded bg-slate-100 text-sm">Sign in</Link>}
      </div>
    </div>
  );
}

function Sidebar(){
  const loc = useLocation();
  return (
    <aside className="w-72 bg-white border-r p-4 space-y-3">
      <div className="mb-4">
        <div className="text-xs uppercase text-slate-400">Navigation</div>
      </div>
      <Nav to="/" label="Home" active={loc.pathname === '/'} />
      <Nav to="/upload" label="Upload & Index" active={loc.pathname.startsWith('/upload')} />
      <Nav to="/files" label="Files" active={loc.pathname.startsWith('/files')} />
      <Nav to="/chat" label="Chat" active={loc.pathname.startsWith('/chat')} />
      <div className="mt-6 text-xs text-slate-400">Tips: Upload court judgments and ask questions in Chat.</div>
    </aside>
  );
}

function Nav({to,label,active}:{to:string,label:string,active?:boolean}){
  return <Link to={to} className={`block px-3 py-2 rounded-lg ${active ? 'bg-accent text-white' : 'text-slate-700 hover:bg-slate-50'}`}>{label}</Link>;
}

export default function Layout(){
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1">
        <Sidebar />
        <main className="flex-1 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

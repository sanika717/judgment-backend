import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

export default function Login(){
  const [u,setU] = useState(''); const [p,setP] = useState('');
  const { login } = useAuth(); const nav = useNavigate();

  async function submit(e:any){
    e.preventDefault();
    const res = await login(u,p);
    if (res?.ok) nav('/');
    else alert('Login failed: ' + (res?.error?.detail || res?.error || JSON.stringify(res)));
  }

  return (
    <div className="max-w-md mx-auto mt-20">
      <div className="card">
        <h2 className="text-2xl font-semibold mb-4">Sign in</h2>
        <form onSubmit={submit} className="space-y-3">
          <input value={u} onChange={e=>setU(e.target.value)} placeholder="Username" className="w-full border p-3 rounded" />
          <input value={p} onChange={e=>setP(e.target.value)} placeholder="Password" type="password" className="w-full border p-3 rounded" />
          <button className="w-full bg-accent text-white py-3 rounded-lg">Sign in</button>
        </form>
        <div className="mt-3 text-sm">New? <Link to="/signup" className="text-blue-600">Create an account</Link></div>
      </div>
    </div>
  );
}

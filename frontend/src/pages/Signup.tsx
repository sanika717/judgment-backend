import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

export default function Signup(){
  const [u,setU] = useState(''); const [p,setP] = useState('');
  const { register } = useAuth(); const nav = useNavigate();
  async function submit(e:any){
    e.preventDefault();
    const res = await register(u,p);
    if (res?.ok) nav('/login');
    else alert('Signup failed: ' + (res?.error?.detail || res?.error || JSON.stringify(res)));
  }
  return (
    <div className="max-w-md mx-auto mt-20">
      <div className="card">
        <h2 className="text-2xl font-semibold mb-4">Create account</h2>
        <form onSubmit={submit} className="space-y-3">
          <input value={u} onChange={e=>setU(e.target.value)} placeholder="Username" className="w-full border p-3 rounded" />
          <input value={p} onChange={e=>setP(e.target.value)} placeholder="Password" type="password" className="w-full border p-3 rounded" />
          <button className="w-full bg-accent text-white py-3 rounded-lg">Sign up</button>
        </form>
      </div>
    </div>
  );
}

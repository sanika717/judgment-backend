import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import * as api from '../apis/api';

export default function ChatPage(){
  const { user } = useAuth();
  const [msg, setMsg] = useState('');
  const [history, setHistory] = useState<{role:string,text:string}[]>([]);

  async function send(){
    if (!user) return alert('Login');
    const sessionId = sessionStorage.getItem('session_id') ?? '';
    const res = await api.chat(user.username, sessionId, msg);
    if (res?.reply) {
      setHistory(h=>[...h, {role:'user', text:msg}, {role:'ai', text: res.reply}]);
      setMsg('');
    } else alert('Error: ' + JSON.stringify(res));
  }

  return (
    <div className="max-w-3xl">
      <h2 className="text-2xl font-semibold mb-4">Chat</h2>
      <div className="space-y-3 mb-4">
        {history.map((m,i)=>(
          <div key={i} className={`p-3 rounded-lg ${m.role==='user' ? 'bg-slate-100 text-right' : 'bg-white'}`}>
            <div className="text-sm">{m.text}</div>
          </div>
        ))}
      </div>

      <div className="flex gap-3">
        <input value={msg} onChange={e=>setMsg(e.target.value)} className="flex-1 border p-3 rounded-lg" placeholder="Ask a question about uploaded documents..." />
        <button onClick={send} className="px-4 py-3 bg-accent text-white rounded-lg">Send</button>
      </div>
    </div>
  );
}

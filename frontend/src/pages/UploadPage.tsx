import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import * as api from '../apis/api';

export default function UploadPage(){
  const { user } = useAuth();
  const [file, setFile] = useState<File | null>(null);
  const [sessionId, setSessionId] = useState<string | null>(sessionStorage.getItem('session_id'));

  async function createSession(){
    if (!user) return alert('Login first');
    const res = await api.createSession(user.username);
    if (res?.session_id) { sessionStorage.setItem('session_id', res.session_id); setSessionId(res.session_id); alert('Session created'); }
    else alert('Failed to create session: ' + JSON.stringify(res));
  }

  async function doUpload(){
    if (!file) return alert('Select a file');
    if (!user) return alert('Login first');
    const s = sessionId ?? (await api.createSession(user.username)).session_id;
    if (!s) return alert('Session required');
    const res = await api.uploadFile(user.username, s, file);
    if (res?.message) alert('Uploaded and indexed');
    else alert('Upload error: ' + JSON.stringify(res));
  }

  return (
    <div className="max-w-2xl">
      <h2 className="text-2xl font-semibold mb-4">Upload Document</h2>
      <div className="mb-4 flex items-center gap-3">
        <button onClick={createSession} className="px-4 py-2 bg-accent text-white rounded-lg">Create Session</button>
        <div className="text-sm text-slate-600">Session stored locally for this browser.</div>
      </div>

      <div className="card">
        <input type="file" onChange={e=>setFile(e.target.files?.[0] ?? null)} />
        <div className="mt-4 flex gap-3">
          <button onClick={doUpload} className="px-4 py-2 bg-blue-600 text-white rounded-lg">Upload & Index</button>
          <div className="text-sm text-slate-500">Selected: {file ? file.name : 'none'}</div>
        </div>
      </div>
    </div>
  );
}

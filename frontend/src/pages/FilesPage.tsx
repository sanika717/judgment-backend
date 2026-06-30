import React, { useEffect, useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import * as api from '../apis/api';

export default function FilesPage(){
  const { user } = useAuth();
  const [files, setFiles] = useState<string[]>([]);
  useEffect(() => {
    (async () => {
      if (!user) return;
      const sessionId = sessionStorage.getItem('session_id') ?? undefined;
      const res = await api.listFiles(user.username, sessionId);
      if (res?.files) setFiles(res.files);
    })();
  }, [user]);

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Files</h2>
      <div className="space-y-3">
        {files.length === 0 && <div className="text-slate-500">No files found for this session.</div>}
        {files.map((f)=>(
          <div key={f} className="p-3 bg-white rounded-lg shadow-sm flex justify-between items-center">
            <div className="font-medium">{f}</div>
            <div className="text-sm text-slate-400">Uploaded</div>
          </div>
        ))}
      </div>
    </div>
  );
}

import React, { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import * as api from '../apis/api';

type User = { username: string } | null;
type AuthCtx = { user: User; login: (u:string,p:string)=>Promise<any>; register: (u:string,p:string)=>Promise<any>; logout: ()=>void };

const AuthContext = createContext<AuthCtx | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User>(null);
  useEffect(()=> {
    const raw = localStorage.getItem('user');
    if (raw) setUser(JSON.parse(raw));
  }, []);
  const login = async (username:string, password:string) => {
    const res = await api.loginUser(username, password);
    if (res?.ok) { setUser({ username }); localStorage.setItem('user', JSON.stringify({ username })); }
    return res;
  };
  const register = async (username:string, password:string) => {
    return await api.registerUser(username, password);
  };
  const logout = () => { setUser(null); localStorage.removeItem('user'); sessionStorage.removeItem('session_id'); };
  return <AuthContext.Provider value={{ user, login, register, logout }}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used inside AuthProvider');
  return ctx;
}

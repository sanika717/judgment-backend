import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import UploadPage from './pages/UploadPage';
import FilesPage from './pages/FilesPage';
import ChatPage from './pages/ChatPage';
import Login from './pages/Login';
import Signup from './pages/Signup';
import { useAuth } from './contexts/AuthContext';

export default function App(){
  const { user } = useAuth();
  return (
    <Routes>
      <Route path='/' element={<Layout />}>
        <Route index element={<Home />} />
        <Route path='upload' element={user ? <UploadPage /> : <Navigate to='/login' />} />
        <Route path='files' element={user ? <FilesPage /> : <Navigate to='/login' />} />
        <Route path='chat' element={user ? <ChatPage /> : <Navigate to='/login' />} />
      </Route>

      <Route path='/login' element={<Login />} />
      <Route path='/signup' element={<Signup />} />
    </Routes>
  );
}

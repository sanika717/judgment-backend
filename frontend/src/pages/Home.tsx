import React from 'react';

export default function Home(){
  return (
    <div className="space-y-6">
      <header className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Welcome to Legal RAG</h1>
          <p className="text-slate-600 mt-1">Upload legal documents, index them, and ask precise legal questions.</p>
        </div>
        <div className="hidden md:block">
          <div className="card">
            <h4 className="font-semibold">Quick Tips</h4>
            <ul className="mt-3 text-sm text-slate-600 space-y-2">
              <li>Upload PDFs (scanned or born-digital).</li>
              <li>Create a session before uploading to group files.</li>
              <li>Ask focused questions in Chat for better answers.</li>
            </ul>
          </div>
        </div>
      </header>

      <section className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="card">
          <h3 className="text-lg font-semibold">Upload & Index</h3>
          <p className="text-sm text-slate-500 mt-2">Add case PDFs to create a searchable knowledge base.</p>
        </div>

        <div className="card">
          <h3 className="text-lg font-semibold">Ask (RAG)</h3>
          <p className="text-sm text-slate-500 mt-2">Ask legal questions based on your uploaded documents.</p>
        </div>

        <div className="card">
          <h3 className="text-lg font-semibold">Files</h3>
          <p className="text-sm text-slate-500 mt-2">Manage uploaded files and sessions.</p>
        </div>
      </section>
    </div>
  );
}

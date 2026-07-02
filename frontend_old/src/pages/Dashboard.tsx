import Layout from "../components/Layout";

export default function Dashboard() {
  return (
    <Layout>

      <h1 className="text-3xl font-bold mb-6">
        Dashboard
      </h1>

      <div className="grid grid-cols-4 gap-5">

        <div className="bg-white p-5 rounded shadow">
          <h3>Total Documents</h3>
          <p className="text-2xl font-bold">0</p>
        </div>

        <div className="bg-white p-5 rounded shadow">
          <h3>Sessions</h3>
          <p className="text-2xl font-bold">0</p>
        </div>

        <div className="bg-white p-5 rounded shadow">
          <h3>Questions</h3>
          <p className="text-2xl font-bold">0</p>
        </div>

        <div className="bg-white p-5 rounded shadow">
          <h3>Bookmarks</h3>
          <p className="text-2xl font-bold">0</p>
        </div>

      </div>

    </Layout>
  );
}
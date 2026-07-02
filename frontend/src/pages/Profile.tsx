import Layout from "../components/Layout";

export default function Profile() {
  return (
    <Layout>
      <h1>Profile</h1>

      <div
        style={{
          background: "white",
          padding: "25px",
          borderRadius: "12px",
        }}
      >
        <p>Name: Sanika Gharat</p>
        <p>Role: Intern</p>
        <p>Documents: 12</p>
        <p>Sessions: 15</p>
      </div>
    </Layout>
  );
}
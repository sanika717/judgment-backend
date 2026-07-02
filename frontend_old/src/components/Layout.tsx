import { ReactNode } from "react";
import Sidebar from "./Sidebar";

interface Props {
  children: ReactNode;
}

export default function Layout({
  children,
}: Props) {
  return (
    <div className="flex">

      <Sidebar />

      <div className="ml-64 p-8 w-full min-h-screen bg-gray-100">
        {children}
      </div>

    </div>
  );
}
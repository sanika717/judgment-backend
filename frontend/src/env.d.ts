/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string;
  readonly VITE_ANOTHER_KEY?: string; // add more if needed
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
